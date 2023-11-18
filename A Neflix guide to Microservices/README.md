# A Netflix guide to Microservices

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

La arquitectura de microservicios de Netflix se basa en dividir programas de software extensos en componentes más pequeños, lo que facilito la escalabilidad y el aislamiento de posibles problemas. Lo que le permitio a Netflix poder escalar rápidamente servicios individuales de manera independiente y aislar problemas de rendimiento.

Se hablo detalladamente sobre la arquitectura de Netflix, incluyendo la gestión de datos en AWS, servicios personalizados y especializados para lógica empresarial, herramientas de procesamiento de video y **CDN (Content Delivery Network)** de Open Connect para almacenamiento y transmisión de videos a gran escala.

Se explico la definición y estructura de un ***microservicio***, siendo una aplicación independiente que proporciona una funcionalidad específica. Los microservices están diseñados para ser pequeños, autónomos y fáciles de mantener.

![microservicioInfraesctructura](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/A%20Neflix%20guide%20to%20Microservices/Images/microservice.PNG)

Lo cual consiste en tres componentes un microservicio:
- ***Código***: El código fuente del microservice.
- ***Datos***: Los datos que utiliza el microservice.
- ***Conexiones***: Las conexiones que el microservice tiene con otros microservices.

Los ***microservicios*** se basan en la arquitectura de sistemas distribuidos. Los sistemas distribuidos son sistemas que consisten en múltiples componentes que se comunican entre sí a través de una red. Ofreciendonos beneficios como:
- Flexibilidad: Permiten fácilmente a los cambios en los requisitos del negocio.
- Escalabilidad: Pueden adaptarse a las demandas cambiantes.
- Resistencia: Son más resistentes a fallos que los sistemas monolíticos.

![redMicroservicio](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/A%20Neflix%20guide%20to%20Microservices/Images/infra.PNG)

Ademas, en el video se nos habla de que se pueden usar en los microservicio diferentes herramientas como:
- ***API***, interfaz de programación de aplicaciones, es un conjunto de definiciones y protocolos que permiten a dos aplicaciones de software comunicarse entre sí. Las API permiten a los desarrolladores reutilizar el código y las funcionalidades de otras aplicaciones. Las API se pueden clasificar en dos tipos principales:

    * API públicas: Son API que están disponibles para cualquier desarrollador que quiera utilizarlas. Las API públicas suelen ser proporcionadas por empresas tecnológicas, como Google, Amazon o Facebook.
    * API privadas: Son API que solo están disponibles para un grupo específico de desarrolladores, como los empleados de una empresa o los socios de un proyecto.

    Las API nos ofrecen una serie de beneficios, entre los que se incluyen:

    * Reutilización: Las API permiten a los desarrolladores reutilizar el código y las funcionalidades de otras aplicaciones. Esto ahorra tiempo y esfuerzo a los desarrolladores.
    * Escalabilidad: Las API pueden utilizarse para escalar aplicaciones. Por ejemplo, una aplicación web puede utilizar una API para acceder a datos de un servidor externo. Si el servidor externo se escala, la aplicación web también se escalará.
    * Interoperabilidad: Las API permiten que aplicaciones de diferentes proveedores se comuniquen entre sí. Esto facilita el desarrollo de aplicaciones que utilizan componentes de diferentes proveedores.
- ***ZUL***, es una librería de código abierto desarrollada por Netflix que proporciona un punto de entrada único para un sistema de microservicios. Zuul se puede utilizar para realizar una serie de tareas, entre las que se incluyen:
    - Enrutamiento: Zuul puede utilizarse para enrutar las solicitudes a los microservicios correspondientes. Esto permite a los desarrolladores de microservicios concentrarse en la lógica de su negocio sin preocuparse por el enrutamiento de las solicitudes.
    - Filtrado: Zuul puede utilizarse para aplicar filtros a las solicitudes antes de que se envíen a los microservicios. Esto permite a los desarrolladores realizar tareas de seguridad, auditoría o registro.
    - Monitorización: Zuul puede utilizarse para recopilar información de las solicitudes que se envían a los microservicios. Esta información puede utilizarse para monitorizar el rendimiento del sistema y detectar problemas.
    
    Zuul está diseñado para ser escalable y tolerante a fallos. Zuul puede utilizarse para manejar un gran número de solicitudes y puede seguir funcionando incluso si uno o más microservicios no están disponibles.
    Actualmente, los microservicios necesitan un cambio cultural en la forma en que las empresas desarrollan y operan softwares. Ya que las empresas deben de adoptar un enfoque descentralizado y colaborativo para el desarrollo de software.
- ***NCCP***, Netflix Circuit Breaker Pattern, es un patrón de diseño de microservicios que ayuda a proteger los sistemas de microservicios de fallos. El patrón funciona mediante la creación de un circuito que puede abrirse y cerrarse. Cuando el circuito está abierto, las solicitudes no se envían a los microservicios afectados. El NCCP se puede utilizar para proteger los sistemas de microservicios de una serie de fallos, entre los que se incluyen:
    * Fallos de hardware
    * Fallos de software
    * Tráfico excesivo

    El NCCP funciona de la siguiente manera:
    1. Cuando una solicitud llega a un microservicio, el microservicio comprueba si el circuito está abierto. Si el circuito está abierto, el microservicio no envía la solicitud al backend.
    1. Si el circuito está cerrado, el microservicio envía la solicitud al backend.
    1. Si el backend responde con un error, el microservicio cierra el circuito.


### Consejos especificos
En el video se nos dio algunos consejos para implementar cada tema mencionado.

Para el enfoque cultural:
-  Establecer una cultura de autonomía y responsabilidad.
- Promover la colaboración entre equipos.
- Utilizar herramientas y procesos que faciliten la comunicación y la colaboración.

Para la arquitectura:
- Diseñar los microservices para que sean pequeños, autónomos y fáciles de mantener.
- Utilizar un modelo de arquitectura basado en eventos para facilitar la comunicación entre microservices.
- Utilizar una infraestructura que sea escalable y resiliente.

Para las operaciones, Evans recomienda:
- Automatizar el despliegue y la gestión de los sistemas.
- Utilizar herramientas y procesos que faciliten la supervisión y el diagnóstico de problemas.

Asi que los ***micorservicios*** son un estilo de arquitectura de sistemas distribuidos en el que cada servicio es una aplicación autónoma que se comunica con otros servicios a través de un conjunto bien definido de API. Lo cual nos ofrece muchas ventajas al implementarlo, ya que nos da una respuesta a los desafíos de la arquitectura monolítica, arquitectura tradicional en el que todo el código de la aplicación se implementa como una sola unidad. 

Asi que los microservicios tienen sus ventajas como:

- ***Modularidad***: se pueden desarrollar, implementarse y escalarse de forma independiente. Esto hace que las aplicaciones de microservicios sean más fáciles de mantener y actualizar.
- ***Escalabilidad***: permiten agregar más instancias de un servicio para manejar más tráfico. Esto hace que las aplicaciones de microservicios sean más escalables que las aplicaciones monolíticas.
- ***Resiliencia***: son resistentes, por lo que pueden continuar funcionando incluso si algunos de los servicios no funcionan. 

Pero también presentan algunos desafíos como:

- ***Complejidad***: requieren que se administre múltiples servicios y sus dependencias.
- ***Comunicación***: necesitan comunicarse entre sí, lo que puede resultar difícil de gestionar.
- ***Coherencia de los datos***: deben mantener la coherencia de los datos en todos los servicios.

En el video tambien mencionan algunas soluciones para que sea mas facil el manejo de los microservicios como:

- ***Hystrix***: Hystrix es una biblioteca que se puede utilizar para manejar tiempos de espera y reintentos para microservicios.
- ***FIT***: FIT es una herramienta que se puede utilizar para probar la disponibilidad y coherencia de los microservicios.
- ***Bibliotecas de cliente***: las bibliotecas de cliente se pueden utilizar para simplificar el proceso de comunicación con microservicios.
- ***Escalado automático***: el escalado automático se puede utilizar para escalar y reducir automáticamente los microservicios según la demanda.
- ***Chaos Monkey***: Chaos Monkey es una herramienta que se puede utilizar para inyectar fallas aleatoriamente en microservicios para probar su resiliencia.

Asi que los microservicios son un estilo de arquitectura poderoso que se puede utilizar para crear aplicaciones complejas, escalables y resistentes. Sin embargo, los microservicios también presentan algunos desafíos que es necesario abordar. Al comprender los desafíos y las soluciones de los microservicios, podrá tomar decisiones informadas sobre si utilizar o no este estilo de arquitectura para su próxima aplicación.

Los ***microservicios*** son una abstracción, significando que no es necesario utilizar alguna tecnología en específico para implementar microservicios.
Los ***microservicios*** son una arquitectura compleja y orgánica, se necesita mucha disciplina y caos para tener éxito.
Los ***microservicios*** se centran primero en las soluciones y en segundo lugar en los equipos, por lo que se concentran en resolver el problema en cuestión y luego preocuparse por cómo organizar sus equipos para respaldar esa solución.

## Conclución
Los ***microservicios*** son una arquitectura de sistemas distribuidos que nos ofrece ventajas, como la modularidad, la escalabilidad y la resiliencia. Sin embargo, también presentan algunos desafíos, como la complejidad, la comunicación y la consistencia de datos. Ya que para Netflix implementar esta arquitectura de microservicio les permitio escalar hasta donde esta hoy en día, ademas de ser tolerante a fallas mediante la palicacion de esta tecnología. Pero usar los microservicios puede ser complejo, no significa que todos sean iguales, ya que la ventaja de los microservicio es que lo podemos adecuar segun a nuestras necesidads e implementar diferentes tecnologias como el uso de bibliotecas como Hystrix, herramientas como FIT o client libraries. Además, es importante implementar prácticas de ingeniería de operaciones adecuadas, como el uso de autoescalado y Chaos Monkey.

En el video se nos recomendo algunos consejos para la implementación de los microservicios como:
* Empezar con un pequeño número de microservices. Ayudará a aprender los conceptos básicos de la arquitectura y a identificar los desafíos potenciales.
* Utiliza una plataforma de orquestación de microservices. Permitirá gestionar el despliegue, la escalabilidad y la comunicación entre los microservices.
* Implementa prácticas de ingeniería de operaciones adecuadas. Garantizará la disponibilidad y la resistencia de la aplicación.

## Bibliografía
Akbary, K. (s/f). Mastering Chaos: A Netflix Guide to Microservices. Recuperado el 18 de noviembre de 2023, de https://github.com/keyvanakbary/learning-notes/blob/master/talks/mastering-chaos-a-netflix-guide-to-microservices.md

InfoQ [@infoq]. (2017, febrero 22). Mastering chaos - A Netflix guide to microservices. Youtube. https://www.youtube.com/watch?v=CZ3wIuvmHeM

Mastering Chaos - A Netflix Guide to Microservices. (s/f). Slideshare.net. Recuperado el 18 de noviembre de 2023, de https://es.slideshare.net/JoshEvans2/mastering-chaos-a-netflix-guide-to-microservices

¿Qué es una API? (s/f). Amazon.com. Recuperado el 18 de noviembre de 2023, de https://aws.amazon.com/es/what-is/api/#:~:text=API%20significa%20“interfaz%20de%20programación,de%20servicio%20entre%20dos%20aplicaciones.

Understanding design of microservices architecture at Netflix. (2021, diciembre 15). TechAhead. https://www.techaheadcorp.com/blog/design-of-microservices-architecture-at-netflix/

What is Zuul? (s/f). Recuperado el 18 de noviembre de 2023, de https://github.com/Netflix/zuul/wiki/Home