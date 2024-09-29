//modulos
const express = require('express');
const routes = express.Router();

//Controlers
const home = require('./src/controllers/login');
const create = require('./src/controllers/createUser')
const update = require('./src/controllers/updateUser')

routes.get("/", home.get);
routes.post("/", home.post);

routes.get('/createUsr', create.get)
routes.post('/createUsr', create.post)

routes.get('/updateUsr/:id', update.get)
routes.post('/updateUsr/:id', update.post)
routes.get('/deleteUsr/:id', update.del)

module.exports = routes;

