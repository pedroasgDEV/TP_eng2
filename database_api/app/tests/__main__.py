from app.tests.users import UsersTest
from app.tests.admins import AdminsTest

usr = UsersTest()

doc = {
    "regis_id": "21.1.4015",
    "name": "Pedro Augusto",
    "email": "pedro.asg@aluno.ufop.edu.br",
    "passwrd": "1234",
    "course": "Ciencia da Computação"
}

if usr.insertTest(doc): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

doc = {
    "email": "pedro.asg@aluno.ufop.edu.br",
    "passwrd": "1234"
}

if usr.loginTest(doc): print(" * Login operation works :)")
else: print(" * Login operation not works :(")

if usr.selectTest("21.1.4015"): print(" * Select operation works :)")
else: print(" * Select operation not works :(")

doc = {
    "name": "Fake",
    "email": "fake@email.com",
}

if usr.updateTest("21.1.4015", doc): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if usr.deleteTest("21.1.4015"): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

usr.endTestes()

adm = AdminsTest()

doc = {
    "name": "Pedro Augusto",
    "email": "jalnsldasd",
    "passwrd": "1234",
    "derp": "DECOM"
}

if adm.insertTest(doc): print(" * Insert operation works :)")
else: print(" * Insert operation not works :(")

doc = {
    "email": doc["email"],
    "passwrd": doc["passwrd"]
}

if adm.loginTest(doc): print(" * Login operation works :)")
else: print(" * Login operation not works :(")

if adm.selectTest(): print(" * Select operation works :)")
else: print(" * Select operation not works :(")

if adm.selectAllTest(): print(" * Select All operation works :)")
else: print(" * Select operation not works :(")

doc = {
    "name": "Fake",
    "email": "fake@email.com",
}

if adm.updateTest(doc): print(" * Update operation works :)")
else: print(" * Update operation not works :(")

if adm.deleteTest(): print(" * Delete operation works :)")
else: print(" * Delete operation not works :(")

adm.endTestes()

#6