# Estatus

CARRERA: **Ingeniería en Computación**

**Efrain Robles Pulido** CÓDIGO: **221350095**

**Computación Tolerante a Fallas**

MAESTRO: **Michel Emanuel Lopez Franco**

SECCIÓN: **D06**    CALENDARIO: **2023B**

**UNIVERSIDAD DE GUADALAJARA**

![CUCEI Logo](https://static.wixstatic.com/media/689543_e867e5de31ce49e7a2c28f84eb1bacf8~mv2.png/v1/fill/w_560,h_150,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/logoudggris.png)

[Programa (exampleService.py)](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Estatus/exampleService.py)

Este programa nos permitira cerrar alguna aplicacion ".exe", previamente seleccionada desde consola, lo cual tambien se le agrego la funcionalidad de que este mismo programa este siempre ejecutandose en nuestro sistema operativo. Lo cual estara cerrando las aplicaciones seleccionadas en el programa si el mismo usuario las abre manualmente.

Una vez escrito el codigo, pasamos a descargar el Non-Sucking Service Manager y realizar sus respectivas instalaciones para luego ejecutar desde CMD, para abrir la siguiente ventana para configurar el servicio deseado.

![Non-Sucking Service Manager](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Estatus/Images/config.PNG)

Una vez configurado, pasamos a activarlo con el comando nssm.exe start proclocker desde el CMD. Por lo que podremos observar en el administrador de servicios y sus efectos de que ya esta funcionando.

![Administrador de Servicio](https://github.com/EfrainRP/Computacion_tolerante_a_fallas/blob/main/Estatus/Images/service.png)

En mi experiencia, al primer intento de la creacion del servicio funciono correctamente el codigo, pero una vez que queria crear otro o modificarlo dejo de funcionar, puedo suponer que puede sr debido a las ubicaciones de mis PATHs de mi equipo por lo que no funciono correctamente despues de la prube inicial.

En este programa tenmos como bibliotecas:
- ***sys*** para acceder a la consola del sistema operativo.
- ***psutil*** nos permite tener acceso a informacion de procesos que corren asi como del sistema.

Como funciones tenemos: 
- Permite verificar que tengamos argumentos en la consola (aplicaciones) seleccionados por el usuario.
```python
def check_arguments(): 
    if len(sys.argv) == 1:
        print('Este programa no funciona sin argumentos')
        sys.exit(0)
```

- Convierte la lista de las aplicaciones seleccionadas con el formato .exe
```python
def get_targets():
    targets = sys.argv[1:]

    i = 0
    while i < len(targets):
        if not targets[i].endswith('.exe'):
            targets[i] = targets[i] + '.exe'
        i += 1
    return targets
```

- Localizara de todos los procesos, los programas seleccionados para cerrarlos
```python
def lock(target):
    for proc in psutil.process_iter():
        if proc.name().lower() == target.lower():
            proc.kill()
```

Para el bloque principal del programa una vez verificado la entrada de las aplicaciones seleccionadas, pasaremos a un ciclo "infinito" en donde estaremos cerrando las aplicaciones seleccionadas repetidamente.

Cabe resaltar que existe otras formas de crear servicios, pero se utilizan otra librerias para tener acceso al mismo sistema operativo para que se incluyan en sus propios servicios. Como este codigo, que crea un servicio para monitorear si se abre Notepad (notepad.exe) y se registra un mensaje en el registro de eventos de Windows cuando esto sucede:

```python
import os
import servicemanager
import sys
import win32event
import win32service
import win32serviceutil
import time
import subprocess

# Nombre del servicio
SERVICE_NAME = "ProgramMonitor"

# Ruta al programa que deseas monitorear
PROGRAM_TO_MONITOR = "notepad.exe"

class ProgramMonitorService(win32serviceutil.ServiceFramework):
    _svc_name_ = SERVICE_NAME
    _svc_display_name_ = "Program Monitor Service"

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        self.is_program_running = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.is_program_running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED, (self._svc_name_, ''))
        self.main()

    def main(self):
        while True:
            if not self.is_program_running:
                if self.is_program_open(PROGRAM_TO_MONITOR):
                    servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, 0, f"{PROGRAM_TO_MONITOR} se ha abierto.")
                    self.is_program_running = True
            else:
                if not self.is_program_open(PROGRAM_TO_MONITOR):
                    servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, 0, f"{PROGRAM_TO_MONITOR} se ha cerrado.")
                    self.is_program_running = False

            # Espera durante un intervalo antes de verificar nuevamente
            time.sleep(5)

    @staticmethod
    def is_program_open(program_name):
        try:
            subprocess.check_output(["tasklist", "/FI", f"IMAGENAME eq {program_name}"])
            return True
        except subprocess.CalledProcessError:
            return False

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(ProgramMonitorService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(ProgramMonitorService)
```

Para que se instale a travez del CMD,(comando: python servicio_monitor.py install) para despues activarlo,(python servicio_monitor.py start).

## Bibliografia:
(S/f). Tecnobillo.com. Recuperado el 15 de septiembre de 2023, de https://tecnobillo.com/sections/python-en-windows/servicios-windows-python/servicios-windows-python.html

