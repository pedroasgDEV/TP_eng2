const Usr = require("./usr").Usr;

class User extends Usr {
    constructor(regis_id = "NO_regis_id", name = "NONAME", email = "NOEMAIL", passwrd = "NOPASSWRD", course = "NOCOURSE") {
      try {
        super(name, email, passwrd);
        this._course = course;
        this._regis_id = regis_id;
      } catch (e) {
        throw new Error(`ERROR: object cannot be created\n${e}`);
      }
      this._description = this.toString();
    }
  
    get course() {
      return this._course;
    }
  
    set course(course) {
      if (typeof course !== "string") {
        throw new TypeError("TYPE_ERROR: course is a string");
      }
      this._course = course;
    }
  
    get regis_id() {
      return this._regis_id;
    }
  
    toString() {
      return `Name: ${this._name}, Email: ${this._email}, Course: ${this._course}, Registration ID: ${this._regis_id}`;
    }
}

exports.User = User;

