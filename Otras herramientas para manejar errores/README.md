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

1. Excepciones (Exception Handling):
Las excepciones son eventos que ocurren durante la ejecución de un programa que interrumpen el flujo normal de ejecución. Puedes utilizar bloques try-catch para capturar y manejar estas excepciones de manera controlada.

1. Declaración de errores (Error Statements):
Algunos lenguajes de programación proporcionan declaraciones específicas para manejar errores, como "throw" en Java o "raise" en Python. Estas declaraciones permiten generar manualmente excepciones o errores cuando ocurre una condición no deseada.

1. Asserts:
Las afirmaciones (asserts) son declaraciones que verifican si una determinada condición es verdadera o falsa. Se utilizan principalmente para realizar verificaciones de control durante el desarrollo y detener la ejecución si una condición no se cumple como se esperaba.

1. Gestión de errores personalizados:
En ocasiones, es útil definir los propios códigos de error y mensajes para manejar situaciones específicas en tus programas. Esto puede hacerse mediante el uso de constantes, enumeraciones o incluso clases personalizadas para representar diferentes tipos de errores.

1. Depuradores (Debuggers):
Los depuradores son herramientas integradas en muchos entornos de desarrollo que permiten rastrear el flujo de ejecución de tu programa y examinar variables en diferentes momentos. Esto es especialmente útil para identificar y resolver errores.

## Asserts

Los Assertions (afirmaciones) son aquellas booleanas colocadas en punto específico de un programa, las cuales serán verdaderas hasta que se demuestre lo contrario.
Este tipo de sentencias se utlizan como ayuda en las correciones de un programa. Como:

- Precondicion: Colocada al inicio de una sección de código, determinando el conjunto de sentencias bajo las cuáles se espera que el código sea ejecutado.
'''
private void setRefreshInterval(int interval) {
        // Confirma la precondición en un método no público.
    assert interval > 0 && interval <= 1000/MAX_REFRESH_RATE : interval;
    ... // Define interval
}
'''
- Postcondicion: Colocada al final, describiendo la sentencia esperada al final de la ejecución.
'''
public BigInteger modInverse(BigInteger m) {
if (m.signum <= 0)
throw new ArithmeticException(“Negativos: “ + m);
... // Se realizan los cálculos
assert this.multiply(result).mod(m).equals(ONE) : this;
return result;
}
'''

Algunos lenguajes de programación modernos incluyen sentencias de tipo “assertions”, que son analizadas en tiempo de ejecución. Como Java:
