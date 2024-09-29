class Usr {
    constructor(name = "NONAME", email = "NOEMAIL", passwrd = "NOPASSWRD") {
      try {
        this._name = name;
        this._email = email;
        this._passwrd = passwrd;
      } catch (e) {
        throw new Error(`ERROR: object cannot be created\n${e}`);
      }
      this._description = this.toString();
    }
  
    get name() {
      return this._name;
    }
  
    set name(name) {
      if (typeof name !== "string") {
        throw new TypeError("TYPE_ERROR: name is a string");
      }
      this._name = name;
    }
  
    get email() {
      return this._email;
    }
  
    set email(email) {
      if (typeof email !== "string") {
        throw new TypeError("TYPE_ERROR: email is a string");
      }
      this._email = email;
    }
  
    get passwrd() {
      return this._passwrd;
    }
  
    set passwrd(passwrd) {
      if (typeof passwrd !== "string") {
        throw new TypeError("TYPE_ERROR: passwrd is a string");
      }
      this._passwrd = passwrd;
    }
  
    toString() {
      return `Name: ${this._name}, Email: ${this._email}`;
    }
}

exports.Usr = Usr;