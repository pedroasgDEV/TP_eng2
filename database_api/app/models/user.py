from app.models.usr import Usr

class User(Usr):
    def __init__(self, regis_id = "NO_regis_id", name = "NONAME", email = "NOEMAIL",
                 passwrd = "NOPASSWRD", course = "NOCOURSE"):
        try:
            super().__init__(name, email, passwrd)
            self.__course = course
            self.__regis_id = regis_id 
        except Exception as e:
            raise Exception(f"ERRO: object cannot be created\n{e}")
        self._description = self.__str__()

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