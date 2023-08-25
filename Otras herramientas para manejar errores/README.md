# Herramientas para el manejar errores

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](data:image/png;base64,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)

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

Los **asserts** pueden llevar ( ) como funcion: 
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

- No se deben usar para comprobar argumentos en métodos públicos: ***los asserts pueden habilitarse o deshabilitarse***, comprobar los argumentos se considera parte de las responsabilidades del método y su especificación.

- No se deben usar para realizar tareas: ya que los asserts pueden deshabilitarse las tareas dejarían de ejecutarse y de proporcionar la funcionalidad del programa.

Nos pueden entrar dudas de cuando emplear un assert y cuando un if o una excepción. Las excepciones se encargan de hacer que el programa sea robusto controlando las situaciones inesperadas pero posibles, los assert se encargan de que el programa sea correcto. Los **assert** deberían ser usados para asegurar algo, mientras que las excepciones deberían usarse para comprobar algo que podría ocurrir. Los **assert** son una herramienta en tiempo de desarrollo, las excepciones además son una herramienta para la ejecución en producción.

## Try Exception

Es una herramienta muy potente que la gran mayoría de lenguajes de programación modernos tienen. Se trata de una ***forma de controlar el comportamiento de un programa cuando se produce un error***. Esto es muy importante ya que salvo que tratemos este error, **el programa se parará**, y esto es algo que en determinadas aplicaciones no es una opción válida. La sentencia try en python funciona de la siguiente manera:

- Primero, se ejecuta la cláusula **try** (la(s) linea(s) entre las palabras reservadas try y la except).

- Si no ocurre ninguna excepción, la cláusula ***except*** se omite y la ejecución de la cláusula try finaliza.

- Si ocurre una excepción durante la ejecución de la cláusula try, se omite el resto de la cláusula. Luego, si su tipo coincide con la excepción nombrada después de la palabra clave ***except***, se ejecuta la cláusula except, y luego la ejecución continúa después del bloque try/except.

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

# Conclusion

Esta investigacion me ayudo a como manejar errores que pudiera encontrar en la programacion asi como los que produzcan los mismos usuarios, por lo que debemos de siempre conocer los errores que se pudieran presentar, además de conocer el contexto para manejar de la mejor forma el error para identificar la tecnica o herramienta a utilizar para evitar que falle el sistema o programa. Ya que no siempre podremos probar el programa a pruba y error para identifiacr lo problemas que se presenten por lo que esta investigacion em ayugo a idenfiticar los errores que se no puedan presentar y poder abarcar estos errores sin que nuestro sistema o programa falle por mal diseño de codigo.

# Bibliografia

📗Uso del assert(). (s/f). El Libro De Python. Recuperado el 25 de agosto de 2023, de https://ellibrodepython.com/assert-python

8.Errores y excepciones. (s/f). Python documentation. Recuperado el 25 de agosto de 2023, de https://docs.python.org/es/3/tutorial/errors.html

12.2.Excepciones. (s/f). Uniwebsidad.com. Recuperado el 25 de agosto de 2023, de https://uniwebsidad.com/libros/algoritmos-python/capitulo-12/excepciones

Assertions. (Afirmaciones) Un primer acercamiento. (s/f). SG Buzz. Recuperado el 25 de agosto de 2023, de https://sg.com.mx/content/view/562

Carbonell, L. (2023, abril 5). Trabajar con errores en Python de forma eficiente. atareao con Linux. https://atareao.es/pyldora/captura-de-errores/

Excepciones en python. (s/f). El Libro De Python. Recuperado el 25 de agosto de 2023, de https://ellibrodepython.com/excepciones-try-except-finally

Franciscomelov. (2022, febrero 4). Sentencias Try y Except de Python: Cómo manejar excepciones en Python. freecodecamp.org. https://www.freecodecamp.org/espanol/news/sentencias-try-y-except-de-python-como-menejar-excepciones-en-python/

La palabra clave assert de Java y un ejemplo. (2015, febrero 13). Blog Bitix. https://picodotdev.github.io/blog-bitix/2015/02/la-palabra-clave-assert-de-java-y-un-ejemplo/

Manejo de excepciones — Fundamentos de Programación en Python. (s/f). Uva.es. Recuperado el 25 de agosto de 2023, de https://www2.eii.uva.es/fund_inf/python/notebooks/07_Manejo_de_excepciones/Manejo_de_excepciones.html

Tratamiento de errores. (s/f). Jtech.ua.es. Recuperado el 25 de agosto de 2023, de http://www.jtech.ua.es/j2ee/publico/lja-2012-13/sesion03-apuntes.html