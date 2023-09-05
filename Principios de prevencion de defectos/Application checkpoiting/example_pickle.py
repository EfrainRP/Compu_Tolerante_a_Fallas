import pickle
import time
import threading

# Función para guardar el estado en un archivo
def guardar_estado(filename, estado):
    try: 
        with open(filename, 'wb') as archivo:
            pickle.dump(estado, archivo)    
    except FileNotFoundError:
        print("El archivo de estado no se encontró. No se serializo (guardo) nada")

# Función para cargar el estado desde un archivo
def cargar_estado(filename):
    try:
        with open(filename, 'rb') as archivo:
            estado = pickle.load(archivo)
            return estado
    except FileNotFoundError:
        print("El archivo de estado no se encontró. Creando un nuevo estado vacío.")
        return {}
    
# Función que se ejecutará cada cierto tiempo para restaurar el estado
def restaurar_estado_periodicamente(archivo_estado, intervalo, info):
    while True:
        guardar_estado(archivo_estado,info) #Almacenamos constantemente lo que tengamos en 'info' del hilo principal
        
        print("\nRegistro/s guardados")
        # Mostramos los datos del archivo respaldo
        print("\t\tArchivo respaldo actual:")
        for clave, valor in info.items():
            print(f"\t\t\t{clave}: {valor}")

        time.sleep(intervalo) # Guardamos el respaldo cada 5 segundos

if __name__ == "__main__":
    archivo_estado = "Principios de prevencion de defectos\Application checkpoiting\estado.pkl"
    intervalo_segundos = 10  # Intervalo de tiempo en segundos para restaurar el estado
    flag = 1   # Bandera para seguir almacenando x cantidad de elementos en el diccionario

    info = cargar_estado(archivo_estado) # Cargamos la informacion que tenemos respaldada

    # Iniciar un hilo para restaurar el estado cada cierto tiempo
    hilo_restaurar_estado = threading.Thread(target=restaurar_estado_periodicamente, args=(archivo_estado, intervalo_segundos, info))
    hilo_restaurar_estado.daemon = True  # El hilo se detendrá cuando el programa principal se cierre
    hilo_restaurar_estado.start()

    while flag:
        # Solicitamos al usuario que ingrese los datos del registro
        # Vamos "guardando" los datos constantemente para que se guarden automaticamente por el otro hilo
        nombre = input("Ingrese el nombre: ")
        info[nombre] = ['','']
        carrera = input("Ingrese la carrera: ")  
        info[nombre] = [carrera,'']
        semestre = input("Ingrese el semestre: ")

        # Actualizamos el archivo respaldo con los nuevos datos
        info[nombre] = [carrera,semestre]

        flag = int(input("Deseas introducir mas datos?\n    0)No   1)Si\n"))
