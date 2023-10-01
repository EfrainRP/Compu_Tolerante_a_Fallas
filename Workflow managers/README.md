# Workflow managers

Este programa implementa la libreria/API para ejecutar el algoritmo de ordenamiento Quicksort en el que estaremos creando un arreglo de 100 valores aleatorios. Por lo que estaremos utilizando los decoradores de Prefect para incluir las ventajas que nos ofrece como el manejo de errores, el tiempo de duracion maximo, y entre otros.
Permitiendonos registrar los datos manejados para poder observar el comportamiento de nuestro codigo mediante el ***Dashboard*** de la pagina de Prefect. 

[Programa (example_prefect.py)](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Principios%20de%20prevencion%20de%20defectos/Application%20checkpoiting/example_pickle.py)

En este programa tenmos como bibliotecas:
- ***prefect*** para utilizar los **tasks y flows**
- ***random*** para generar los numeros aleatorios
- ***datetime*** para generar el valor de tiempo para la libreria de prefect

Como funciones principales tenemos: 
- El cual es una tarea a realizar del flujo pricipal del codigo, por lo que si se pasa de los 2 minutos ordenando, automaticamennnte se parara el codigo mandando un error debido a su tiempo excedido. Siendo esta funcion la de ordenamiento principal.
```python
@task(cache_expiration= timedelta(minutes=2))
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
```

- Esta funcion es nuestro flujo principal que usara prefect para poder registrar los valores de errores del codigo, en el que tenemos el nombre como se llamara en el dashboard, los intentos que hara cuando falle, el intervalo de intentos, y el valor que imprimira un mensaje de ejecucion.
```python
@flow(name="Quicksort",retries=2, retry_delay_seconds=5,log_prints=True)
def crear_quicksort():
    datos_a_ordenar=[]
    for i in range(0,100):
        datos_a_ordenar.append(random.randint(1,456))

    return quicksort(datos_a_ordenar)
```
- En el codigo principal tenemos como se ejecuta el flujo principal para poder estar ejecutando varias veces para realizar el registro de los valores en la pagina principal, teniendo intervaloes de 60 segundos para que se vaya ejecutando el codigo completo.
```python
if __name__ == "__main__":
    crear_quicksort.serve(name="quicksort",
                    tags=["onboarding"],
                    interval=60)
```

## Dashboard
![Dashboard]()

![Flows]()
