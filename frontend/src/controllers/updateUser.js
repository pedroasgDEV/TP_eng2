const get_one = require("../modules/users").get;
const update = require("../modules/users").put;
const del_doc = require("../modules/users").del;
const User = require("../class/user").User;
const getDif = require("../utils/objDiff").getObjectDifference

async function get (req, res) {
    const result = await get_one(req.params.id.slice(1));
    res.render('update_usr', { user: result });
}

async function post (req, res){
    regis_id = req.params.id.slice(1)
    const usr = await get_one(regis_id);

    const usr_update = new User(
        //regis
        regis_id,
        //name
        req.body.name,
        //email
        req.body.email,
        //passwrd
        req.body.passwrd,
        //course
        req.body.course
    );

    const diff = getDif(usr, usr_update)
    await update(diff, regis_id)

    res.render('update_usr', { people: usr_update });
}

async function del (req, res){
    await del_doc(req.params.id.slice(1));
    res.render('login');
}

module.exports = {
    get : get,
    post: post,
    del: del
}