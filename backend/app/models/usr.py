class Usr:
    def __init__(self, name = "NONAME", email = "NOEMAIL", passwrd = "NOPASSWRD"):
        try:
            self.__name = name
            self.__email = email
            self.__passwrd = passwrd
        except Exception as e:
            raise Exception(f"ERRO: object cannot be created\n{e}")
        self._description = self.__str__()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError("TYPE_ERRO: name is a string")
        self.__name = name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        if not isinstance(email, str):
            raise TypeError("TYPE_ERRO: email is a string")
        self.__email = email

    @property
    def passwrd(self):
        return self.__passwrd

    @passwrd.setter
    def passwrd(self, passwrd):
        if not isinstance(passwrd, str):
            raise TypeError("TYPE_ERRO: passwrd is a string")
        self.__passwrd = passwrd