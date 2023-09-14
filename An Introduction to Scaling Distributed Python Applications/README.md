# An Introduction to Scaling Distributed Python Applications

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

Este programa es un simulador de registro de datos que se estaran guardando en un diccionario para su respectivo procesamiento de los datos por lo que se estara extrayendo los del diccionario a otras variables.
Se utiliza el bloque "lock" para garantizar que las operaciones de lectura y escritura en el diccionario se realicen de manera segura y eviten condiciones de carrera.

[Programa (example.py)](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/An%20Introduction%20to%20Scaling%20Distributed%20Python%20Applications/example.py)

En este programa tenmos como bibliotecas:
- ***multiprocessing*** para crear un proceso.
- ***random*** para generar datos aleatorios.
- ***Time*** para controlar el  y tener retrasos de tiempo.
- ***Threading*** para crear subprocesos.

Como funciones tenemos: 
- Para generar datos de ID de estudiantes, de la carrera y del semestre. Para asi registrarlos en el diccionario.
```python
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
```

- Esta función de simular que se esta procesando los datos, pasando los datos a otras variables desde el diccionario.
```python
def procesar_datos():
    while True:
        try:
            with lock:
                if registros:
                    nombre, (carrera, semestre) = registros.popitem()
                    print(f"Procesando registro: {nombre}, {carrera}, Semestre {semestre}")
        except Exception as e:
            print(f"Error en el procesamiento de datos: {str(e)}")
```

Para el bloque principal del programa se inicia un hilo ("hilo_generar") que estará ejecutando la funcion "generar_datos" en segundo plano para generar los datos. Despues se iniciara el proceso ("proceso_procesar") que estará ejecutando la funcion "procesar_datos" en segundo plano para procesar los datos. Como el hilo y el proceso se iniciaran como demonios para que una que se termine el programa con alguna interrupcion de teclado tambine lo hara el hilo y el proceso.

En el bucle principal, el programa podra ejecutar otro programa por lo tanto por lo que podemos realizar aun más tareas en un mismo codigo.