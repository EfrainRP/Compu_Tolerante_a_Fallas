# Se intenta abrir un fichero y se captura una posible excepción
extraStr = "\tPrograma prueba"
try: #Codigo a ejecutar donde tal vez no se encuentre el archivo
    print(extraStr + " iniciando")
    file = open("Otras herramientas para manejar errores\myfile.txt",'r')
except FileNotFoundError: #Error de Archivo no Encontrado
    # Se entra aquí si no se encontro el archivo
    print('No se pudo abrir el archivo, debido a que no se encontro el archivo')
except: #Se generaliza otras errores o podemos poner errores especificas para ser atrapadas
    print('Se encontro algun otro error')    
else:   #Codigo a ejecutar si no tenemos errores
    mensage = file.read()
    print(mensage)
    file.close()
finally: #Bloque que siempre se ejecutara si hay o no errores
    #Generalmente usado para liberar recursos o regresar valores a su estdo inicial
    print(extraStr + " finalizado")
    extraStr = " " #Limpiando variable