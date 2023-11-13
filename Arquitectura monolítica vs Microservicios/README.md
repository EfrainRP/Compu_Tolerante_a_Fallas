# Arquitectura monolítica vs Microservicios

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

## Monolitico
En una arquitectura monolitica, toda la aplicación reside en un único código base y se ejecuta como un solo proceso en un único entorno. Ofrecienndonos varias caracteristicas:

- ***Acoplamiento Estrecho***: Los diferentes módulos o componentes de la aplicación están fuertemente acoplados, lo que significa que hay una interdependencia significativa entre ellos. Cambios en una parte del sistema pueden tener un impacto directo en otras partes.

- ***Despliegue Único***: Todas las actualizaciones o nuevas versiones de la aplicación se despliegan como una única unidad. Esto implica que si se realiza una modificación en una parte de la aplicación, se debe implementar y desplegar toda la aplicación.

- ***Lenguaje y Tecnología Únicos***: Por lo general, una aplicación monolítica se desarrolla utilizando un único lenguaje de programación y un conjunto de tecnologías coherentes.

- ***Escala Vertical***: La escalabilidad se logra principalmente a través de la adición de más recursos (escalabilidad vertical) en lugar de distribuir la carga en varios servidores (escalabilidad horizontal).

- ***Gestión Centralizada de Datos***: La aplicación monolítica suele compartir una única base de datos centralizada entre sus módulos.

- ***Desarrollo y Mantenimiento Centralizados***: El desarrollo, la implementación y el mantenimiento de la aplicación se gestionan centralmente como un solo proyecto.

Aunque las aplicaciones monolíticas han sido el enfoque tradicional para el desarrollo de software, han surgido desafíos con respecto a la escalabilidad, la flexibilidad y la velocidad de desarrollo en entornos empresariales modernos. Con el tiempo, ha habido un movimiento hacia arquitecturas más distribuidas, como los microservicios, que buscan abordar algunas de las limitaciones asociadas con las aplicaciones monolíticas, permitiendo una mayor agilidad, escalabilidad y mantenimiento.

## Microservicio
Los microservicios son una arquitectura de diseño de software en la que una aplicación se compone de pequeños servicios independientes y autocontenidos, llamados microservicios. Cada microservicio es responsable de una función de negocio específica y se ejecuta como un proceso separado, comunicándose con otros servicios a través de mecanismos ligeros como API HTTP/REST o mensajes. Ofreciendonos caracteristicas como:

- ***Descentralización***: Cada microservicio es una unidad independiente que puede ser desarrollada, desplegada y escalada de forma independiente. Esto permite a los equipos trabajar en diferentes partes de la aplicación de manera autónoma.

- ***Independencia Tecnológica***: Los microservicios pueden estar implementados utilizando diferentes lenguajes de programación, tecnologías y bases de datos según los requisitos específicos de cada servicio.

- ***Escalabilidad Independiente***: Cada microservicio puede escalar de forma independiente según sus propias necesidades, lo que mejora la eficiencia en el uso de recursos.

- ***Despliegue Continuo***: La arquitectura de microservicios facilita la implementación continua, permitiendo actualizaciones y despliegues frecuentes de servicios individuales sin afectar a la aplicación en su conjunto.

- ***Resiliencia y Tolerancia a Fallos***: Los microservicios están diseñados para ser resistentes a fallos. Si un microservicio falla, no debería afectar la funcionalidad general de la aplicación.

- ***Comunicación a Través de Interfaces Bien Definidas***: La comunicación entre microservicios se realiza generalmente a través de interfaces bien definidas, como API RESTful o mensajes, facilitando la interoperabilidad.

- ***Gestión de Datos Descentralizada***: Cada microservicio puede gestionar su propia base de datos, lo que reduce la complejidad de la gestión de datos en comparación con las aplicaciones monolíticas con una única base de datos centralizada.

- ***Organización Ágil***: Los equipos pueden organizarse en torno a los microservicios, lo que mejora la responsabilidad y la agilidad organizativa.

Aunque los microservicios ofrecen ventajas significativas en términos de agilidad, escalabilidad y mantenimiento, también presentan desafíos, como la gestión de la comunicación entre servicios, la coordinación de transacciones distribuidas y la necesidad de una infraestructura adecuada para implementar y gestionar la arquitectura de microservicios. La adopción exitosa de microservicios requiere una cuidadosa consideración de estos desafíos.

### Actividad de Microservicios
Para poder realizar esta actividad fue necesario instalar ***Docker Desktop***, para Windows desde la pagina principal de [**Docker**](https://docs.docker.com/desktop/install/windows-install/).
Una vez instalado la aplicacion (y verificado que funcione correctamente, iniciando el programa), utilizado en la [practica anterior](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/tree/main/Dockers).

En esta ocasion nuestro **microservicio** sea relizado en 4 diferentes contenedores para que con la ayuda del balanceador de carga de nginx pueda direccionarnos a cada contenedor, por lo que en nuestro navegador nos mostrara un mensaje con el puerto del contenedor en el que se direccionó. 

Asi que nuestro *balanceador de carga de Nginx* distribuira el *trafica/peticiones de los clientes* hacia los multiples contenedores.

Si descargas estos archivos de esta carpeta, y ejecutas los comandos:
1. `docker build -t node-app .` 
1. `docker compose up`

Podras probar por ti mismo la pagina microservicio que se realizo. En donde podremos verificarlo al entrar a nuestro navegador con el url: ***localhost:8080***, en el que podremos observar la ID del puerto que se esta usando del contenedor definido en estos archivos, de '1111', '2222,'3333','4444','5555' de los contenedores creados, los cuales tienen una misma "pagina" en donde se podrá observar el ID del contendor web utilizado. 

## Conclución
Los microservicios con Docker nos ofrecen una arquitectura flexible y escalable para el desarrollo y despliegue de aplicaciones. Con Docker, nos ofrece un entorno ligero y portátil que facilito la creación y ejecución de microservicios de manera consistente en diferentes entornos. Me tomo un poco de tiempo poder aplicar el balanceador de carga para el microservicio, ya que no conocia muy bien como usar la herramienta de Nginx.