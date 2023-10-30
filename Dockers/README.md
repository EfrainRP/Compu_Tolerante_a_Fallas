# Dockers

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

Para poder realizar esta actividad fue necesario instalar ***Docker Desktop***, para Windows desde la pagina principal de [Docker](https://docs.docker.com/desktop/install/windows-install/).
Una vez instalado la aplicacion (y verificado que funcione correctamente, iniciando el programa), procederemos a probar esta herramienta desde terminal de ***Visual Studio***, cabe destacar que es necesario ubicarse en la direccion de la aplicacion Web para que funcione correctamente.
Empezando a utilizar los comandos basicos de Docker para esta aplicacion Web sencilla.
- `docker images` enlista todas las imagenes que se tienen descargado en el dispositivo.
- `docker pull node` permite descargar la imagen de la tecnologia a utilizar, por lo que podemos cambiar la tecnologia a usar, en este cado se descargara la ultima version de NodeJs disponible de [Docker](https://hub.docker.com/_/node), para escoger una version es necesario usar la etiqueta de la pagina oficial para descargarlo.
- `docker image rmi node` permite eliminar la imagen descargada del dispositivo, mediante su ID para eliminarlo.
![docker images](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/pull.PNG)
- `docker network ls` enlista todas las redes que tenemos en los contenedores, util para la comunicacion entre contenedores.
- `docker container create baseDatos` permite crear el contenedor con el nombre 'baseDatos'.
- `docker container rm baseDatos` permite eliminar el contenedor con el nombre 'baseDatos' o mediante su ID.
- `docker ps` permite enlistar los contenedoer que se estan corriendo, con el atributo `-a` enlistara todo.
- `docker network create skillUp` crea una red con el nombre 'skillUp' para la comunicacion entre contenedores.
- `docker network rm skillUp` permite eliminar el contenedor con el nombre 'skillUp' o mediante su ID.
![docker network create skillUp](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/network.PNG)
- `docker run -d -p 3000:3000 -name nodeapp -network mired node` permite correr (si no existe, se creara) el contenedor, (`-d`, detached) en forma de segundo , luego la `-p` permite mapear el puerto del "PuertoAnfitrion:PuertoContenedor", el contenedor tendra el nombre 'nodeapp' y finalmente se especifica el tipo de imagen que se utilizara para el contenedor, en este caso sera de NodeJs. Cabe recalcar que tendremos que haber crado la red previamente.
- `docker build -t node-app:1.0 .` iniciara el proceso de contruccion de una imagen Docker, `-t` nos permite colocar una etiqueta a la imagen resultatne con nombre `node-app` y la version `1.0` para referenciar la imagen con un nombre mas comodo que la ID. y el `.` nos idicara que utilizara el ***Dockerfile*** por lo que previamente deberemos de crearlo antes. Por lo cual tendremos que crear sus respectivos contenedores con sus puertos, variables de entornos y etc.
![docker build -t node-app:1.0 .](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/build.PNG)
![docker image, network](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/run%2Cbuild.PNG)
![docker images](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/create%20image.PNG)

A continucacion se aplico los volumes, que nos permitira mantener los datos que vayamos almacenando en la aplicacion Web, por lo que en los .yml se especifica donde se trabajara para manejar esos datos.
Asi que para evitar mas commandos, se puede utilizar el archivo **docker-compose.yml**, que nos permitira crear los contenedores. Por lo que en cada archivo se explica como funciona cada parametro del .yml.
- `docker compose up` por lo que construira los contenedores segun a las especificaciones del docker-compose.yml y el dockerfile, por lo que creara una red para esta comunicacion entre contenedores.
- `docker compose down` por lo que eliminara los contenedores que se crearon con el anterior comando.
![docker compose up](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/composeUP.PNG)
![docker compose down](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/composeDOWN.PNG)

Ademas se tiene otro tipo de docker-compose-dev y Dockerfile.dev que se puede decir que es para el desarrollo de la misma aplicacion Web ya que contiene el uso del nodemon para poder realizar los cambios deseados y se muestren en el paso del tiempo de prueba. Por lo que se explica detalladamente cada parametro utilizado en sus respectivos archivos.
- `docker compose -f docker-compose-dev.yml up` por lo que construira los contenedores segun a las especificaciones del docker-compose-dev.yml y el dockerfile.dev, por lo que creara una red para esta comunicacion entre contenedores.
- `docker compose -f docker-compose-dev.yml down` por lo que eliminara los contenedores que se crearon con el anterior comando.
![docker compose -f docker-compose-dev.yml up](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/compose-devUP.PNG)
![docker compose -f docker-compose-dev.yml down](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Dockers/Images/compose-devDOWN.PNG)