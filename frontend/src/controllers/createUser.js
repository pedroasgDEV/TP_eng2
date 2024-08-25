const post_usr = require("../modules/users").post;

function get (req, res) {
    res.render('create_usr');
}

async function post(req, res){
    const usr = {
        //regis_id
        "regis_id": req.body.regis_id,
        //name
        "name": req.body.name,
        //email
        "email": req.body.email,
        //passwrd
        "passwrd": req.body.passwrd,
        //course
        "course": req.body.course
    };

    result = await post_usr(usr);

    if (!result) res.render('create_usr');
    else res.render('login');
} 

module.exports = {
    get : get,
    post: post
}