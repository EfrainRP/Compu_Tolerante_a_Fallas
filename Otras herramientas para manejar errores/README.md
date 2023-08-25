# Herramientas para el manejar errores

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

En el proceso de creación de aplicaciones, sistemas y programas, es inevitable que ocurran situaciones inesperadas que puedan interrumpir el flujo normal de ejecución. Estas situaciones, son conocidas como errores o excepciones, que se originan por diversos motivos, como datos incorrectos, condiciones imprevistas o problemas en el entorno de ejecución.

El manejo de errores busca anticiparse y controlar estos escenarios no deseados de manera organizada y efectiva. En lugar de permitir que los errores detengan por completo la ejecución del programa, el manejo de errores permite identificar, capturar y gestionar estas situaciones de manera que la aplicación pueda recuperarse o finalizar de manera controlada, brindando a los usuarios una experiencia más satisfactoria y evitando fallos catastróficos.

A través de varias técnicas los desarrolladores pueden detectar y abordar errores desde diferentes ángulos. Es por eso es mecesario conocer para que situaciones podemos utilizar ciertas tecnicas para manejar los errores.

1. ***Excepciones (Exception Handling)***:
Las excepciones son eventos que ocurren durante la ejecución de un programa que interrumpen el flujo normal de ejecución. Puedes utilizar bloques try-catch para capturar y manejar estas excepciones de manera controlada.

1. ***Declaración de errores (Error Statements)***:
Algunos lenguajes de programación proporcionan declaraciones específicas para manejar errores, como "throw" en Java o "raise" en Python. Estas declaraciones permiten generar manualmente excepciones o errores cuando ocurre una condición no deseada.

1. ***Asserts***:
Las afirmaciones (asserts) son declaraciones que verifican si una determinada condición es verdadera o falsa. Se utilizan principalmente para realizar verificaciones de control durante el desarrollo y detener la ejecución si una condición no se cumple como se esperaba.

1. ***Gestión de errores personalizados***:
En ocasiones, es útil definir los propios códigos de error y mensajes para manejar situaciones específicas en tus programas. Esto puede hacerse mediante el uso de constantes, enumeraciones o incluso clases personalizadas para representar diferentes tipos de errores.

1. ***Depuradores (Debuggers)***:
Los depuradores son herramientas integradas en muchos entornos de desarrollo que permiten rastrear el flujo de ejecución de tu programa y examinar variables en diferentes momentos. Esto es especialmente útil para identificar y resolver errores.

## Asserts

Los Assertions (afirmaciones) son aquellas booleanas colocadas en punto específico de un programa, las cuales serán verdaderas hasta que se demuestre lo contrario.
Este tipo de sentencias se utlizan como ayuda en las correciones de un programa. Si la expresión contenida dentro del mismo es **False**, se lanzará una *excepción*, concretamente ***AssertionError***.

Los **asserts** pueden llevar () como funcion: 
```python 
assert(1==2) # AssertionError
```
o usarse sin parentesis:

```python
x = "ElLibroDePython"
assert x == "ElLibroDePython"
``` 
Son utilizados como:
- ***Precondicion***: Colocada al inicio de una sección de código, determinando el conjunto de sentencias bajo las cuáles se espera que el código sea ejecutado.

- ***Postcondicion***: Colocada al final, describiendo la sentencia esperada al final de la ejecución.

- ***Class invariants***: para validar el estado de una clase según está definido en su contrato, siempre se debe cumplir independientemente de las operaciones que se realicen.
- ***Código no alcanzable en tiempo de ejecución***: partes del programa que se espera que no sea alcanzable, como cláusulas else o default en sentencias switch.

```python
def divide(a, b):
    assert b != 0, "Divisor no puede ser cero"  # Precondición
    result = a / b
    assert result * b == a, "La postcondición no se cumple"  # Postcondición
    return result

# Ejemplo de uso
numerator = 10
denominator = 2

# Verificar precondición
assert denominator != 0, "El denominador no puede ser cero"

# Realizar la operación
result = divide(numerator, denominator)

# Verificar postcondición
assert result * denominator == numerator, "La postcondición no se cumple"

print("Resultado:", result)
```

Y no deben usarse para:

- No se deben usar para comprobar argumentos en métodos públicos: los asserts pueden habilitarse o deshabilitarse, comprobar los argumentos se considera parte de las responsabilidades del método y su especificación.

- No se deben usar para realizar tareas: ya que los asserts pueden deshabilitarse las tareas dejarían de ejecutarse y de proporcionar la funcionalidad del programa.

Nos pueden entrar dudas de cuando emplear un assert y cuando un if o una excepción. Las excepciones se encargan de hacer que el programa sea robusto controlando las situaciones inesperadas pero posibles, los assert se encargan de que el programa sea correcto. Los **assert** deberían ser usados para asegurar algo, mientras que las excepciones deberían usarse para comprobar algo que podría ocurrir. Los **assert** son una herramienta en tiempo de desarrollo, las excepciones además son una herramienta para la ejecución en producción.

## Try Exception

La sentencia try en python funciona de la siguiente manera:

- Primero, se ejecuta la cláusula **try** (la(s) linea(s) entre las palabras reservadas try y la except).

- Si no ocurre ninguna excepción, la cláusula ***except*** se omite y la ejecución de la cláusula try finaliza.

- Si ocurre una excepción durante la ejecución de la cláusula try, se omite el resto de la cláusula. Luego, si su tipo coincide con la excepción nombrada después de la palabra clave except, se ejecuta la cláusula except, y luego la ejecución continúa después del bloque try/except.

- Si ocurre una excepción que no coincide con la indicada en la cláusula except se pasa a los try más externos; si no se encuentra un gestor, se genera una unhandled exception (excepción no gestionada) y la ejecución se interrumpe con un mensaje como el que se muestra arriba.

Con la cláusula **except**, podemos especificar diferentes excepciones a atrapar, asi como tener múltiples excepciones como:

```python
try:
    x = int(input("Please enter a number: "))
    break
except (RuntimeError, TypeError, ValueError):
    print("Oops!  That was no valid number.  Try again...")
```

Si no sabemos que excepción hay que saltar, podemos utiliza la clausula **Exception**, que controla cualquier tipo de excepcion.

Ademas podemos utilizar el bloque de **else**, que va despues de *try* y *except*, para ejecutar si no ha ocurrido ninguna excepción.

Además de los bloques de ***try, except*** y ***else*** se puede añadir el bloque ***finally***. En donde se ejecutar **siempre**, sin importar si hubo una excepcion. Utilizado normalmente como accion de limpieza.

```python
try:
# Codigo a ejecutar
# Pero podria haber errores en este bloque

except <tipo de error>:
# Haz esto para manejar la excepcion
# El bloque except se ejecutara si el bloque try lanza un error

else:
# Esto se ejecutara si el bloque try se ejecuta sin errores

finally:
# Este bloque se ejecutara siempre
```
#Conclusion
Esta investigacion me ayudo a como manejar errores que pudiera encontrar en la programacion asi como los que produzcan los mismos usuarios, por lo que debemos de siempre conocer los errores que se pudieran presentar, ademas de conocer el contexto para el cual manejaremos el error para identificar la tecnica o herramienta a utilizar para evitar que falle el sistema o programa.

#Bibliografia
📗 Uso del assert(). (s/f). El Libro De Python. Recuperado el 25 de agosto de 2023, de (https://ellibrodepython.com/assert-python)

8. Errores y excepciones. (s/f). Python documentation. Recuperado el 25 de agosto de 2023, de (https://docs.python.org/es/3/tutorial/errors.html
)
12.2. Excepciones. (s/f). Uniwebsidad.com. Recuperado el 25 de agosto de 2023, de (https://uniwebsidad.com/libros/algoritmos-python/capitulo-12/excepciones)

Assertions. (Afirmaciones) Un primer acercamiento. (s/f). SG Buzz. Recuperado el 25 de agosto de 2023, de (https://sg.com.mx/content/view/562)

Carbonell, L. (2023, abril 5). Trabajar con errores en Python de forma eficiente. atareao con Linux. (https://atareao.es/pyldora/captura-de-errores/)

Excepciones en python. (s/f). El Libro De Python. Recuperado el 25 de agosto de 2023, de (https://ellibrodepython.com/excepciones-try-except-finally)

Franciscomelov. (2022, febrero 4). Sentencias Try y Except de Python: Cómo manejar excepciones en Python. freecodecamp.org. (https://www.freecodecamp.org/espanol/news/sentencias-try-y-except-de-python-como-menejar-excepciones-en-python/)

La palabra clave assert de Java y un ejemplo. (2015, febrero 13). Blog Bitix. (https://picodotdev.github.io/blog-bitix/2015/02/la-palabra-clave-assert-de-java-y-un-ejemplo/)

Manejo de excepciones — Fundamentos de Programación en Python. (s/f). Uva.es. Recuperado el 25 de agosto de 2023, de (https://www2.eii.uva.es/fund_inf/python/notebooks/07_Manejo_de_excepciones/Manejo_de_excepciones.html)

Tratamiento de errores. (s/f). Jtech.ua.es. Recuperado el 25 de agosto de 2023, de (http://www.jtech.ua.es/j2ee/publico/lja-2012-13/sesion03-apuntes.html)