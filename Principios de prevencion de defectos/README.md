# Principios de prevención de defectos

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

La prevención de defectos es fundamental para garantizar la calidad y fiabilidad del software que se desarrolla. Los defectos, también conocidos como errores o "bugs" pueden tener un impacto significativo en la funcionalidad y seguridad de una aplicación. Para abordar este desafío, se han desarrollado una serie de métodos y enfoques que ayudan a prevenir la aparición de defectos desde las etapas iniciales del ciclo de desarrollo. Estos métodos se centran en la identificación temprana, la corrección oportuna y la mitigación de riesgos asociados con la programación. 

![Image](https://www.softwaretestinghelp.com/wp-content/qa/uploads/2017/10/Defect-Prevention.jpg)

Por lo tanto, se pueden utilizar algunos métodos y prácticas comunes para prevenir defectos como:

1. ***Revisión de código***: Los desarrolladores revisan el código de sus colegas en busca de errores, malas prácticas y oportunidades de mejora. Esto se puede hacer de manera formal a través de revisiones planificadas o de manera informal mediante pares de programadores trabajando juntos.
Muchos defectos, como pérdidas de memoria, paso incorrecto de argumentos, código inalcanzable, falta de legibilidad, alta complejidad y problemas de mantenimiento, se pueden identificar mediante la revisión del código.
Encontrar defectos en la etapa de codificación y solucionarlos allí mismo resultaría menos costoso que encontrarlos en la etapa de prueba.

1. ***Pruebas unitarias***: Las pruebas unitarias implican escribir pruebas automatizadas para cada unidad de código (generalmente una función o método) para asegurarse de que funcionen correctamente. La implementación de pruebas unitarias puede ayudar a detectar defectos temprano y garantizar que las modificaciones futuras no rompan el código existente.
Se pueden utilizar los tutoriales para más o menos hacer una revisión, pero se relaciona principalmente es comparar el sistema con el prototipo, lo que le dará una mejor idea sobre la corrección y / o la apariencia del sistema.

1. ***Análisis estático de código***: Herramientas de análisis estático, como linters y analizadores de código estático, escanean el código en busca de posibles problemas, como variables no utilizadas, declaraciones redundantes o prácticas de codificación inconsistentes.

1. ***Buenas prácticas de codificación***: Adherirse a buenas prácticas de codificación, como la nomenclatura de variables coherente, la estructuración del código legible y el uso de comentarios descriptivos, puede ayudar a prevenir defectos relacionados con la calidad del código.

1. ***Pruebas de integración***: Las pruebas de integración verifican la interacción entre diferentes componentes del software para detectar problemas de comunicación o de funcionamiento en conjunto.

1. ***Control de versiones y gestión de cambios***: Utilizar sistemas de control de versiones como Git y llevar un registro de los cambios realizados en el código puede ayudar a identificar y solucionar problemas causados por cambios no deseados.
Es bueno dejar que alguien de su equipo revise su código y lo revise. Todos los miembros deben revisar los cambios de código con respecto a otros módulos y dar su opinión en caso de que se sospeche algún efecto secundario.

1. ***Revisión de requisitos***: Es importante asegurarse de que los requisitos del proyecto estén bien definidos y comprensibles para evitar malentendidos y cambios de último minuto que puedan introducir defectos. 
Por lo que el primer nivel de revisión debe estar dentro del equipo, seguido de otro nivel de revisión externa (por un desarrollador o BA o cliente) para asegurarse de que todas las perspectivas estén sincronizadas.

1. ***Capacitación y formación***: Mantener a los desarrolladores actualizados con respecto a las mejores prácticas de programación y las nuevas tecnologías puede mejorar la calidad del código producido.

1. ***Pruebas de regresión***: Realizar pruebas de regresión después de realizar cambios en el código para asegurarse de que las nuevas modificaciones no hayan introducido defectos en áreas previamente funcionales.

1. ***Automatización de pruebas***: Automatizar las pruebas funcionales y de rendimiento puede ayudar a identificar rápidamente defectos a medida que se desarrolla el software.

1. ***Uso de estándares y directrices***: Seguir estándares de codificación y directrices específicas para el lenguaje o el marco que estás utilizando puede ayudar a mantener la consistencia y prevenir defectos.

Al implementar uno y/o combinaciones de estos métodos y prácticas, se pueden reducir significativamente la existencia de defectos y mejorar la calidad general del software. Por lo cual se puede implementar diferentes análisis para la prevención de defectos, como:

* ***Análisis de Pareto***: Siendo una técnica formal y simple que ayuda a priorizar el orden de resolución del problema para lograr el máximo impacto. Por lo tanto, los problemas una vez identificados se priorizan de acuerdo con la frecuencia y se realiza un análisis estadístico detallado para encontrar qué 20% de las razones atribuyen al 80% de los problemas. Simplemente centrándose en esas razones del 20% y eliminándolas, los resultados están garantizados mientras se optimiza la extensión del trabajo involucrado.

* ***Análisis de espina de pescado***: También conocido como ***Análisis de Ishikawa*** este método es una técnica de análisis de causa raíz más visual. No hay estadísticas involucradas, ya que este método se basa en una lluvia de ideas de todo el equipo.
El problema se escribe primero en el lado más a la derecha y en la línea horizontal que lo atraviesa, se enumeran las diversas causas. La rama que tiene más huesos de causa-subcláusula (o líneas / ramas) es el problema más grave y que se debe trabajar para su eliminación. Esta técnica también se llama a veces ***análisis de causa y efecto***.

![Análisis de causa y efecto](https://myservername.com/img/bug-defect-tracking/07/defect-prevention-methods-3.jpg)

# Conclusión
Al investigar los diversos métodos y prácticas para prevenir los futuros defectos, me ha dado cuenta que pueden ser muy efectivos si los aplicamos en nuestro trabajo diariamente, ya que nos permitirá tener una mejora de calidad de proyecto significativo. Permitiéndonos tener diversos enfoques, evaluación constante y entre otros beneficios. Puesto que estas técnicas y métodos deberían ser una práctica cultural y de gestión para cada uno de los desarrolladores para reducir costos y entregar productos más confiables y satisfactorios para los usuarios.


# Bibliografia
Follow, M. (2020, septiembre 5). Defect prevention methods and techniques. GeeksforGeeks. https://www.geeksforgeeks.org/defect-prevention-methods-and-techniques/

V., S., & Gopalakrishnan Nair, T. R. (s/f). Effective defect prevention approach in software process for achieving better quality levels. Arxiv.org. Recuperado el 4 de septiembre de 2023, de https://arxiv.org/pdf/1001.3552.pdf

Walia, G. S., & Carver, J. C. (2009). A systematic literature review to identify and classify software requirement errors. Information and Software Technology, 51(7), 1087–1109. https://doi.org/10.1016/j.infsof.2009.01.004

(S/f-a). Embedded.com. Recuperado el 4 de septiembre de 2023, de https://www.embedded.com/techniques-for-software-defect-prevention-and-identification/

(S/f-b). Myservername.com. Recuperado el 4 de septiembre de 2023, de https://spa.myservername.com/software-testing-templates

(S/f-c). Softwaretestinghelp.com. Recuperado el 4 de septiembre de 2023, de https://www.softwaretestinghelp.com/defect-prevention-methods/#Defect_Prevention_Methods_and_Techniques
