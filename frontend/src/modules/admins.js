const axios = require("axios");
const Admin = require("../class/admin").Admin;

const link = "http://localhost:3030/api/admins/";

async function post(doc) {
    result = (await axios.post(link, doc)).data;

    if (result.message == "Admin created") return result.id;
    else return false;
}

async function get(id){
    result = (await axios.get(link + `${id}`)).data;

    if (result.message == "Admin not found") return false;

    return convert(result);
}

async function get_all(){
    result = (await axios.get(link + "all")).data;

    if (result.message == "Admin not found") return false;

    result.forEach( (val, i, array) => {
        array[i] = convert(val)
    });

    return result;
}

async function put(doc, id) {
    result = (await axios.put(link + `${id}`, doc)).data;
    
    if (result.message == "Admin updated") return true;
    else return false;
}

async function del(id) {
    result = (await axios.delete(link + `${id}`)).data;
    
    if (result.message == "Admin deleted") return true;
    else return false;
}

function convert(doc){
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
    "post" : post,
    "get" : get,
    "get_all": get_all,
    "put" : put,
    "del" : del
};