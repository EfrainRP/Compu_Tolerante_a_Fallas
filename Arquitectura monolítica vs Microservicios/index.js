const express = require('express');
const app = express()
const appId = process.env.APPID;

app.get('/', (req, res) => { res.send(`Opening app : ${appId}`)}) //Ruta raiz de nuestra pagina

app.get('/crear', (req, res) => {res.send(`Opening app : ${appId}      ok`)}) //Ruta secundaria que simulara otro servicio

app.listen(appId, () => console.log(`App listening on port ${appId}!`)) //Mensaje de puertos activos