# Application Checkpoint

Este programa permite al usuario ingresar datos y los respalda automáticamente cada cierto intervalo de tiempo. Mientras tanto, otro hilo se encarga de realizar el respaldo periódico en segundo plano. 

[Programa (example_pickle.py)](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Principios%20de%20prevencion%20de%20defectos/Application%20checkpoiting/example_pickle.py)

En este programa tenmos como bibliotecas:
- Pickle para la serializacion de datos
- Time para controlar el tiempo
- Threading para crear subprocesos.

Como funciones principales tenemos: 
- Esta función se encarga de guardar (serializado) los datos de un diccionario de estado utilizando el pickle. Si el archivo no se encuentra, muestra un mensaje de error.
```python
def guardar_estado(filename, estado):
    try: 
        with open(filename, 'wb') as archivo:
            pickle.dump(estado, archivo)    
    except FileNotFoundError:
        print("El archivo de estado no se encontró. No se serializo (guardo) nada")
```

- Esta función se encarga de cargar (deserializa) a un diccionario desde el archivo utilizando el pickle. Si el archivo no se encuentra, crea un diccionario vacío y muestra un mensaje informativo.
```python
def cargar_estado(filename):
    try:
        with open(filename, 'rb') as archivo:
            estado = pickle.load(archivo)
            return estado
    except FileNotFoundError:
        print("El archivo de estado no se encontró. Creando un nuevo estado vacío.")
        return {}
```

- Esta función ejecuta en un bucle infinito y se encarga de guardar constantemente el diccionario info en el archivo de estado. También muestra los datos actuales del archivo de respaldo. El intervalo entre las operaciones de respaldo se define por intervalo (10 segundos).
```python
def restaurar_estado_periodicamente(archivo_estado, intervalo, info):
    while True:
        guardar_estado(archivo_estado,info) #Almacenamos constantemente lo que tengamos en 'info' del hilo principal
        
        print("\nRegistro/s guardados")
        # Mostramos los datos del archivo respaldo
        print("\t\tArchivo respaldo actual:")
        for clave, valor in info.items():
            print(f"\t\t\t{clave}: {valor}")

        time.sleep(intervalo) # Guardamos el respaldo cada 5 segundos
```

Para el bloque principal del programa se establece el nombre del archivo de estado, el intervalo de respaldo y la bandera flag para controlar si se deben introducir más datos. Despues de cargara la información previamente respaldada desde el archivo mediante la función "cargar_estado". 

A continuación, se inicia un hilo ("hilo_restaudra_estado") que estará ejecutando la funcion "restaurar_estado_periodicamente" en segundo plano para realizazr los respaldos.

En el bucle principal, el programa solicita al usuario ingresar datos (nombre, carrera y semestre) y los almacena en el diccionario info. Luego, actualiza el archivo de respaldo con los nuevos datos.
El programa pregunta al usuario si desea introducir más datos a través de la bandera flag. Si la respuesta es 0 (no), el bucle principal termina y el programa se cierra.

## RunTime
![RunTime 1](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Principios%20de%20prevencion%20de%20defectos/Application%20checkpoiting/Images/RunTime1.PNG)

![RunTime 2](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Principios%20de%20prevencion%20de%20defectos/Application%20checkpoiting/Images/RunTime2.PNG)
