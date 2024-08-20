from app.models.usr import Usr

class User(Usr):
    def __init__(self, name = "NONAME", email = "NOEMAIL", passwrd = "NOPASSWRD",
                 inst = "NOINST", course = "NOCOURSE", regis_id = "NO_regis_id"):
        try:
            super().__init__(name, email, passwrd)
            self.__inst = inst
            self.__course = course
            self.__regis_id = regis_id 
        except Exception as e:
            raise Exception(f"ERRO: object cannot be created\n{e}")
        self._description = self.__str__()

    @property
    def inst(self):
        return self.__inst

    @inst.setter
    def inst(self, inst):
        if not isinstance(inst, str):
            raise TypeError("TYPE_ERRO: inst is a string")
        self.__inst = inst

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        if not isinstance(course, str):
            raise TypeError("TYPE_ERRO: course is a string")
        self.__course = course

    @property
    def regis_id(self):
        return self.__regis_id