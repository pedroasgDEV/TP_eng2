const axios = require("axios");
const User = require("../class/user").User;

const link = "http://localhost:3030/api/users/";

async function post(doc) {
    try{
        result = (await axios.post(link, doc)).data;
    }
    catch{
        return false
    } 
    if (result.message == "User created") return true;
    else return false;
}

async function get(regis_id){
    result = (await axios.get(link + `${regis_id}`)).data;
    if (result.message == "User not found") return false;
    result = convert(result);
    return result;
}

async function put(doc, regis_id) {
    result = (await axios.put(link + `${regis_id}`, doc)).data;
    if (result.message = "User updated") return true;
    else return false;
}

async function del(regis_id) {
    result = (await axios.delete(link + `${regis_id}`)).data;
    if (result.message = "User deleted") return true;
    else return false;
}

function convert(doc){
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

module.exports = {
    "post" : post,
    "get" : get,
    "put" : put,
    "del" : del
};