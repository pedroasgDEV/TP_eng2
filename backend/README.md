**ROTAS**

***USER**** -> arquivo: app/routes/users.py

POST: localhost:3030/api/users/ 
    SEND: (JSON com os dados do novo usuario)
    RECV: (JSON com 'message' se funcionou ou não) 

GET: localhost:3030/api/users/<regis_id>
    SEND: (nada)
    RECV: (JSON com 'message' se não funcionou ou JSON com os dados do usuario encontrado)

PUT: localhost:3030/api/users/<regis_id>
    SEND: (JSON com os campos atualizados, não precisa enviar todos os dados do usario)
    RECV: (JSON com 'message' se funcionou ou não)

DELETE: localhost:3030/api/users/<regis_id>
    SEND: (nada)
    RECV: (JSON com 'message' se funcionou ou não)

***ADMIN**** -> arquivo: app/routes/admins.py

POST: localhost:3030/api/admins/ 
    SEND: (JSON com os dados do novo admin)
    RECV: (JSON com 'message' se funcionou ou não) 

GET ONE: localhost:3030/api/admins/<id>
    SEND: (nada)
    RECV: (JSON com 'message' se não funcionou ou JSON com os dados do admin encontrado)

GET ALL: localhost:3030/api/admins/all
    SEND: (nada)
    RECV: (JSON com 'message' se não funcionou ou JSON com uma lista com os dados de todos os admins)

PUT: localhost:3030/api/admins/<id>
    SEND: (JSON com os campos atualizados, não precisa enviar todos os dados do admin)
    RECV: (JSON com 'message' se funcionou ou não)

DELETE: localhost:3030/api/admins/<id>
    SEND: (nada)
    RECV: (JSON com 'message' se funcionou ou não)

***LOGIN**** -> arquivo: app/routes/login.py

GET: localhost:3030/api/login/
    SEND: (JSON com 'email' e 'passwrd')
    RECV: (JSON com 'message' se não funcionou ou JSON com os dados do usr ou adm encontrado em 'obj' e com 'type' com o tipo de cadastro encontrado, se é user ou admin)

