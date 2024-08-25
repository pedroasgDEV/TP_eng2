const axios = require("axios");
const User = require("../class/user").User;
const Admin = require("../class/admin").Admin;

const link = "http://localhost:3030/api/login/";

async function login(doc){
    try{
        result = (await axios.get(link, doc)).data;
    }
    catch { return false }

    if (result.message == "Not found") return false;

    if(result.type == "user") return convert_usr(result.obj)
    else return convert_adm(result.obj)
}

function convert_usr(doc){
    return new User (
        //regis
        doc.regis_id,
        //name
        doc.name,
        //email
        doc.email,
        //passwrd
        doc.passwrd,
        //course
        doc.course
    )
}

function convert_adm(doc){
    return new Admin (
        //id
        doc.id,
        //name
        doc.name,
        //email
        doc.email,
        //passwrd
        doc.passwrd,
        //derp
        doc.derp
    )
}

module.exports = {
    "login" : login
};