import threading
import multiprocessing
import random
import time

# Diccionario para almacenar los registros
registros = {}
lock = threading.Lock()  # Bloqueo para evitar condiciones de carrera

# Función para generar datos aleatorios y registrarlos
def generar_datos():
    while True:
        try:
            # Generar datos aleatorios (simulación)
            nombre = f"Estudiante{random.randint(1, 100)}"
            carrera = f"Carrera{random.randint(1, 5)}"
            semestre = random.randint(1, 10)
            time.sleep(2)
            with lock:
                registros[nombre] = (carrera, semestre)
                print(f"Registro guardado: {nombre}, {carrera}, Semestre {semestre}")
        except Exception as e:
            print(f"Error en la generación de datos: {str(e)}")

# Función para procesar los datos registrados
def procesar_datos():
    while True:
        try:
            with lock:
                if registros:
                    nombre, (carrera, semestre) = registros.popitem()
                    print(f"Procesando registro: {nombre}, {carrera}, Semestre {semestre}")
        except Exception as e:
            print(f"Error en el procesamiento de datos: {str(e)}")

if __name__ == "__main__":
    # Crear un hilo para generar datos en paralelo
    hilo_generar = threading.Thread(target=generar_datos)
    hilo_generar.daemon = True
    hilo_generar.start()

    # Crear un proceso demonio para procesar datos en paralelo
    proceso_procesar = multiprocessing.Process(target=procesar_datos)
    proceso_procesar.daemon = True
    proceso_procesar.start()

    try:
        while True:
            # Realizar otras tareas en el programa principal si es necesario
            time.sleep(1)
    except KeyboardInterrupt:
        print("El programa fue interrumpido.")

    print("Registros finales:")
    print(registros)