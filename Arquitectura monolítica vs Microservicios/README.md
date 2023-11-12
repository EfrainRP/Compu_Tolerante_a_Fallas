# Arquitectura monolítica vs Microservicios

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

Para poder realizar esta actividad fue necesario instalar ***Docker Desktop***, para Windows desde la pagina principal de **[Docker]**(https://docs.docker.com/desktop/install/windows-install/).
Una vez instalado la aplicacion (y verificado que funcione correctamente, iniciando el programa), utilizado en la [practica anterior](link del git anterior).

## Microservicio
En esta ocasion nuestro microservicio sea relizado en 4 diferentes contenedores para que con la ayuda del balanceador de carga de nginx pueda direccionarnos a cada contenedor, por lo que en nuestro navegador nos mostrara un mensaje con el puerto del contenedor en el que se direcciono. 

Asi que nuestro balanceador de carga de Nginx distribuira el trafica/peticines de los clientes hacia los multiples contenedores.

Si descargas estos archivos de esta carpeta, y ejecutas primero el comando `docker build -t node-app .` y despues el comando `docker compose up`, podras probar por ti mismo la pagina microservicio que se realizo.

## Conclución
