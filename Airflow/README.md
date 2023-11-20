# Airflow

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

Para poder realizar esta actividad fue necesario instalar ***Docker Desktop***, para Windows desde la pagina principal de [***Docker***](https://docs.docker.com/desktop/install/windows-install/). Una vez instalado la aplicacion (y verificado que funcione correctamente, iniciando el programa), procederemos a probar esta herramienta desde terminal de ***Visual Studio***, cabe destacar que es necesario ubicarse en la direccion de la aplicacion Web para que funcione correctamente.

Además para poder realizarlo deberas de conocer los comando básicos que nos ofrece ***Docker Desktop***, por lo que deberas de ver la inofrmación de [Docker de mi GitHub](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/tree/main/Docker).

A continuación, desde terminal tendremos que acceder a la misma ubicacion del archivo ***yaml***, para despues utilizar el comando de `docker compose up` que nos generará los contenedores de las respectivas imagenes de ***Airflow***.

Despues podras acceder desde tu navegador, con el url: ***http://localhost:8080/home***. Veras un login de Airflow, como usuario y contraseña, introduciras **Airflow**.

![login](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/4.PNG)

Luego podras aplicar tu programa en donde lo colocaremos en la carpeta de `/dags`.

![carpetas](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/8.PNG)

Despues tendremos que activar el volume de docker en la interfaz, para asi ejecutar el codigo:

![Ui](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/4.12.png) 
![On](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/8.1.png)

Asi ahora podemos acceder a los datos que nos ha generado el programa, que nos registrara su funcionamiento, fallas y otras cosas.

![Data](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/4.1.PNG)
![Data](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/4.2.PNG)
![Data](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/4.3.PNG)
![Console](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/4.4.PNG)

Finalmente podremos finalizar el docker con airflow con el comando `docker compose down` o si queires borrar todo seria `docker compose down --volumes --rmi all`

![Docker compose down](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/5.PNG)
![Docker compose down --all](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Airflow/Images/6.PNG)

## Conclución
Al usar Docker con Airflow, los desarrolladores pueden crear flujos de trabajo que son portables y escalables. Los contenedores pueden ejecutarse en cualquier máquina que tenga Docker instalado, lo que facilita la implementación de flujos de trabajo en diferentes entornos. Además, los contenedores pueden escalarse fácilmente para satisfacer las necesidades cambiantes de los flujos de trabajo. Esto se puede hacer agregando o eliminando contenedores según sea necesario. 
Al usar Docker con Airflow nos ofrece una serie de ventajas para los desarrolladores. Los contenedores hacen que los flujos de trabajo sean portables, escalables y eficientes. Esto los hace ideales para una variedad de propósitos, incluyendo el procesamiento de datos, la automatización de tareas y la creación de aplicaciones web. Finalmente, Airflow es una herrameinta poderosa que puede ser utilizada para una variedad de propósitos, incluyendo el procesamiento de datos, la automatización de tareas y la creación de aplicaciones web.