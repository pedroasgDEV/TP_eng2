//modulos
const login = require("../modules/login").login;

function get (req, res) {
    res.render('login');
}

async function post (req, res) {
    doc = {
        "email": req.body.email,
        "passwrd": req.body.passwrd
    }
    
    const result = await login(doc);
    if (!result) res.render('login');

    res.render('update_usr', { user: result });
}

module.exports = {
    get : get,
    post : post
}