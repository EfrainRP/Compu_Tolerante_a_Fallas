# Orthogonal Defect Classification (ODC)

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

Se trata de un esquema desarrollado por IBM para clasificar defectos con el fin de proveer retroalimentación sobre el progreso de un proyecto, a través del mismo. Su objetivo es obtener un paradigma para medir las relaciones causa-efecto de los defectos, donde se pudiera encontrar la causa raíz de un defecto. Al mismo tiempo se deseaba desarrollar una clasificación de defectos que fuera simple y que estuviera lo más libre posible de errores humanos.

ODC (Orthogonal Defect Classification) _es una técnica utilizada para categorizar los defectos encontrados en el proceso de desarrollo de software, que permite medir de manera cuantitativa y con recursos mínimos los aspectos que deben ser tomados en consideración de forma prioritaria durante la etapa de desarrollo, con el fin de tomar medidas correctivas que eviten la aparición de defectos similares en el futuro_.

Su principal aplicación es para la mejora del desarrollo del software, ya que los defectos son clasificados en distintas clases que colectivamente apuntan al área del proceso de desarrollo en específico que requiere de atención.

Esta clasificación debe cumplir con los siguientes requerimientos:
- Ortogonalidad, es decir, sin superposición de las clases, esto es, que un defecto solo puede estar bajo una única clase
- Consistencia a través de las fases
- Uniformidad a través de los productos

ODC puede ser usada para mejorar el círculo de calidad del proceso de prevención de defectos, lo cual se ha demostrado que resulta en un alto grado de ahorro en costos de análisis, ya que el proceso de clasificación permite encontrar de forma retrospectiva la causa y efecto en un muy corto tiempo en lo que se refiere al tiempo que toma a un grupo de analistas efectuar un detallado análisis de la causa raíz del defecto.

ODC proporciona un sistema para convertir esa información en métricas que proporcionen estadísticas que permitan definir de manera más acertada los puntos que necesitan ser tratados, resultando así ser un instrumento para detallar mejor y recibir la retroalimentación más oportunamente. 

El primer paso es crear clases de defectos en función de las especificaciones del proyecto, el objetivo es que dichas clases puedan explicar el progreso del producto a través del proceso y que puedan ser utilizadas a lo largo de ciclo de desarrollo del proyecto.

## Declaración de clases o tipos de defectos

Los tipos de defectos deben definir o deben capturar, en su nombre, el significado de lo que se arregló.

Una vez definidos los tipos de defecto deben analizarse y para ello se debe mapear el tipo de defecto con el proceso, independientemente del estado en el que se encuentre y del producto que se utiliza, lo importante es encontrar la relación entre los tipos de defecto y la etapa del proceso en la que se podría detectar.

Los pasos para definir una clase son:
1. Definir las métricas necesarias
1. Validar los puntos a corregir tomando en consideración la experiencia en otros proyectos
1. Mejorar el sistema de mediciones cuando se aprenden nuevos métodos a través de los experimentos

Una vez definidas las clases, deben determinarse los atributos o condiciones que se usarán para definir los defectos puntuales, deben ser adecuados para poder categorizar cada uno de ellos de manera correcta y mapearlos a la etapa en la que pudo haberse prevenido el error.

## Definición de atributos

Existen dos tipos de atributos que se recomiendan para la definición de errores:

***Tipo de defecto***: Se declaran los tipos donde un programador pueda categorizar un defecto de manera sencilla y sin confusiones. Es recomendable usar los siguientes tipos de defecto:
- **Código faltante**: Se refiere a que la funcionalidad no fue implementada, por lo que la verificación encontró el defecto.
- **Código incorrecto**: Hace referencia cuando el código fue implementado pero tiene errores que llevaron a encontrar el defecto.
- **Errores de función**: Se refiere a problemas de capacidad, configuración o comunicación entre capas de la arquitectura.
- **Asignación**: Pocas líneas de código, como inicialización de variables.
- **Interface**: Errores con la interfaz final del usuario o interacción con otros componentes.
- **Validación**: Lógica del sistema que falló en validar configuración errónea.
- **Sincronización**: Manejo de recursos compartidos.
- **Build, empaquetado y merge**: Errores con librerías externas utilizadas, manejo de cambios o control de versiones.

***Tipo de disparadores***: Son condiciones que saca a la superficie un defecto. Idealmente, la distribución de los disparadores para los defectos de campo debe ser similar al encontrado en las pruebas del sistema. Una discrepancia puede indicar deficiencias en el ambiente de pruebas.

## Clasificación de Causas y Efectos

Es importante recolectar la información no solo de los disparadores, sino también de todos aquellos inconvenientes derivados del error que afectan directamente al desempeño del aplicativo. 

***Causa***: Atributo de clasificación ortogonal que describe un defecto para:
- El proceso de desarrollo
- El proceso de verificación

***Efecto***: Atributos o métricas que están afectando al producto o a los procesos, por ejemplo:
- Áreas de impacto
- Densidad de defectos
- Rehacer arreglos de código

## Planteamiento general del método
En el contexto de la metodología, un defecto se refiere a _un cambio necesario en el software_, básicamente categoriza los defectos en clases, y señala que parte del proceso requiere atención. 

Al corregir un defecto, el programador le asigna un "tipo" (en el sistema de seguimiento de errores), que es trazado a una o varias fases del proceso de desarrollo (diseño, programación y pruebas). Añadir una nueva característica (defecto funcional) es distinto a cambiar un par de líneas de código para corregir el valor de una variable (defecto de asignación).
_Al ser la clasificación un proceso manual_, se busca que el conjunto de tipos de defectos sean ortogonales (es decir, que no se junten entre ellos) para minimizar los errores y evitar confusiones. Además, los tipos de defectos deben ser generales para que sean independientes del tipo de desarrollo, de las fases del mismo e incluso del producto.

Los tipos de defectos se asocian a una o más fases del proceso de desarrollo, como se muestra en la Tabla 1. De esta manera, la asociación indica donde se espera un pico en defectos de tipo funcional. Por tanto, la tabla de mapeo describe el perfil de defectos en cada una de las fases.

![Tabla 1](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Principios%20de%20prevencion%20de%20defectos/ODD(Orthogonal%20Defect%20Classification)/Images/Tabla1.png)

El objetivo de los tipos de defectos también es poder relacionar cada tipo con algunas de las fases del proceso de desarrollo. Se trata de determinar dónde fueron inyectados los defectos en el sistema. Se encontró que cada tipo de defecto tiende a ser inyectado en relativamente pocas áreas o fases de desarrollo.

La asociación encontrada entre los tipos de defectos y el proceso de desarrollo se muestra en la siguiente tabla: 

![Tabla 2](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Principios%20de%20prevencion%20de%20defectos/ODD(Orthogonal%20Defect%20Classification)/Images/Tabla2.PNG)

Al final de cada fase de desarrollo, se generan gráficas que muestran el número de defectos de cada tipo encontrados en esa fase. Al comparar el número de ocurrencias de un tipo de defecto por fase, el cambio en la distribución da una retroalimentación sobre el estado del proceso de desarrollo.

Dado que las distribuciones de los tipos de defectos cambian con el tiempo, proveen una forma de medir la madurez del producto. Cuando una desviación del proceso se identifica a través de una desviación de las curvas de distribución de defectos, el tipo de defecto encontrado apunta a la parte del proceso que necesita atención.

La piedra angular de este proceso son los análisis causales. En éstos cada desarrollador aporta datos objetivos sobre cada defecto. Estos datos son registrados en una base de datos, y al final de cada fase, se realiza una junta para analizar los datos colectivamente para determinar sus causas.


# Conclusion
Gracias a esta norma de clasificación desarrollada, podemos clasificar y determinar que acciones se deberán de tomar para su debida corrección. Para lograrlo, fue necesario implementar categorías que nos ayudan a determinar principalmente qué errores son los que deberemos de arreglar, pero para eso es necesario su identificación en determinadas circunstancias. Y mediante estos valores se podrá realizar tanto graficas y acciones para determinar la priorización de los errores a reparar.


# Bibliografia
De código cuyo objetivo principal es detectar e identificar, I. de C. E. U. T. F. de R. (s/f). Clasificación Ortogonal de Defectos Atributo Valores. Www.uv.mx. Recuperado el 4 de septiembre de 2023, de https://www.uv.mx/personal/ermeneses/files/2017/08/Clasificacion-Ortogonal-de-Defectos.pdf

De Ingenieria, F., Ana, I., Coronel, P. O., Christian, I., & Barquero, H. (s/f). UNIVERSIDAD DE CUENCA. Edu.ec. Recuperado el 4 de septiembre de 2023, de http://dspace.ucuenca.edu.ec/bitstream/123456789/26245/1/Tesis.pdf

Página, G., Izcóatl, G., Romero, H., Técnico, R., & De, J. (s/f). Maestría en Ingeniería de Software CIMAT Reporte Técnico. Repositorioinstitucional.mx. Recuperado el 4 de septiembre de 2023, de https://cimat.repositorioinstitucional.mx/jspui/bitstream/1008/104/2/TE%20264.pdf
