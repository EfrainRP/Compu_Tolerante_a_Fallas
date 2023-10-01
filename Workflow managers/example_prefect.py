from prefect import flow, task
import random
from datetime import timedelta

# Tarea que implementara el QuickSort
@task(cache_expiration= timedelta(minutes=2))#Teniendo un tiempo limite de ejecucion
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

# Flujo para ejecutar QuickSort
@flow(name="Quicksort",retries=2, retry_delay_seconds=5,log_prints=True)#Teniendo 2 intentos de 5 s de retraso y que se imprima un mensaje de ejecucion
def crear_quicksort():
    datos_a_ordenar=[]
    for i in range(0,100):
        datos_a_ordenar.append(random.randint(1,456))

    return quicksort(datos_a_ordenar)

if __name__ == "__main__":
    crear_quicksort.serve(name="quicksort", #Ejecucion del flujo quicksort en un intervalo de 60s
                    tags=["onboarding"],
                    interval=60)
