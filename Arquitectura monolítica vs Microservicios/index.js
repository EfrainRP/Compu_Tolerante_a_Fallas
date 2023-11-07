//Importa los modulos dependencias necesarios para este codigo, sitio web simple
import mongoose from 'mongoose' //Dependencia para MongoDB
import express from 'express' //Dependencia de NodeJs

const Animal = mongoose.model('Animal', new mongoose.Schema({ //Crea un modelo de una base de datos ANIMAL en MongoDB
  tipo: String,
  estado: String,
}))

const appVersion1 = express()// Crea una instancia para tener una aplicacion web principal 
const appVersion2 = express()// Crea una instancia para tener una aplicacion web principal 

mongoose.connect('mongodb://efra:password@mongodb:27017/miapp?authSource=admin') //Se especifica la conexion a la DB(base de datos) de Mongo de acuerdo al docker
//El cual se le asigna un usuario y contraseña, despues se conectara al contenedor de la BD a usar

//Primera ruta raiz
appVersion1.get('/', async (_req, res) => {//Del metodo GET, empezara a listar los animales en la base de datos de mongo
  console.log('listando... animales...')//Imprimira en consola el mensaje
  const animales = await Animal.find();//Obtienen todos los animales en la BD
  return res.send(animales)//Regresara la lista de los animales encontrados
})
appVersion1.listen(3000, () => console.log("listening..."))

//Segunda ruta raiz
appVersion2.get('/', async (_req, res) => {//Del metodo GET, empezara a listar los animales en la base de datos de mongo
    console.log('listando... animales...')//Imprimira en consola el mensaje
    const animales = await Animal.find();//Obtienen todos los animales en la BD
    return res.send(animales)//Regresara la lista de los animales encontrados
  })
appVersion2.listen(3000, () => console.log('listening...'))//mensaje que estara escuchando la WEB, en el puerto 3000
