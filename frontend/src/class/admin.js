const Usr = require("usr").Usr

class Admin extends Usr {
    constructor(id = -1, name = "NONAME", email = "NOEMAIL", passwrd = "NOPASSWRD", derp = "NODERP") {
      try {
        super(name, email, passwrd);
        this._derp = derp;
        this._id = id;
      } catch (e) {
        throw new Error(`ERROR: object cannot be created\n${e}`);
      }
      this._description = this.toString();
    }
  
    get derp() {
      return this._derp;
    }
  
    set derp(derp) {
      if (typeof derp !== "string") {
        throw new TypeError("TYPE_ERROR: derp is a string");
      }
      this._derp = derp;
    }
  
    get id() {
      return this._id;
    }
}

exports.Admin = Admin
  