from app.models.usr import Usr

class Admin(Usr):
    def __init__(self, name = "NONAME", email = "NOEMAIL", passwrd = "NOPASSWRD",
                 derp = "NODERP", id = -1):
        try:
            super().__init__(name, email, passwrd)
            self.__derp = derp
            self.__id = id 
        except Exception as e:
            raise Exception(f"ERRO: object cannot be created\n{e}")
        self._description = self.__str__()

    @property
    def derp(self):
        return self.__derp

    @derp.setter
    def derp(self, derp):
        if not isderpance(derp, str):
            raise TypeError("TYPE_ERRO: derp is a string")
        self.__derp = derp

    @property
    def id(self):
        return self.__id