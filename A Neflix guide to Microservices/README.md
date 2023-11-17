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
- ***API***, interfaz de programación de aplicaciones, es un conjunto de definiciones y protocolos que permiten a dos aplicaciones de software comunicarse entre sí. Las API permiten a los desarrolladores reutilizar el código y las funcionalidades de otras aplicaciones.
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

## Conclución
