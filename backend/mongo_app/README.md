Aqui está o `README.md` gerado com base nas rotas e informações que você forneceu:

```markdown
# API de Fóruns com Flask e MongoDB

Esta API fornece um sistema de fóruns onde cada fórum corresponde a uma coleção no MongoDB. Os usuários podem criar, editar, listar e deletar fóruns e posts, com suporte a operações ordenadas por timestamp.

## Requisitos

- Python 3.x
- Flask
- PyMongo
- MongoDB (pode ser executado em um container Docker)

## Configuração do Ambiente

1. **Clone o repositório:**
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o MongoDB via Docker:**
   Certifique-se de que o MongoDB está rodando em um container Docker com a porta `27017` exposta.
   ```bash
   docker run -d -p 27017:27017 --name mongo mongo
   ```

4. **Configure as variáveis de ambiente do MongoDB:**
   Verifique o arquivo `app/config.py` para garantir que as configurações de conexão com o MongoDB estão corretas.

5. **Execute a aplicação Flask:**
   ```bash
   flask run
   ```

## Rotas da API

### **Fóruns**

#### Criar um Fórum
**POST:** `/api/<subject_code>`  
**Envio:**
```json
{
  "User": "00.0.0000",
  "Type": "POST",
  "text": "FORUM <subject_code> CREATED",
  "time": 1234567890
}
```
**Recebimento:**
```json
{
  "status": "success",
  "message": "Forum Created"
}
```

#### Deletar um Fórum
**DELETE:** `/api/<subject_code>`  
**Envio:** N/A  
**Recebimento:**
```json
{
  "status": "success",
  "message": "Collection dropped successfully."
}
```

### **Posts**

#### Criar um Post
**POST:** `/api/<subject_code>/`  
**Envio:**
```json
{
  "User": "00.0.0000",
  "Type": "POST",
  "text": "Texto do post",
  "time": 1234567890
}
```
**Recebimento:**
```json
{
  "status": "success",
  "inserted_id": "60b1234567890abcdef12345",
  "doc": {
    "_id": "60b1234567890abcdef12345",
    "User": "00.0.0000",
    "Type": "POST",
    "text": "Texto do post",
    "time": 1234567890
  }
}
```

#### Listar Posts
**GET:** `/api/<subject_code>/`  
**Envio:** (Filtros opcionais no corpo da requisição)  
**Recebimento:**
```json
{
  "status": "success",
  "result": [
    {
      "_id": "60b1234567890abcdef12345",
      "User": "00.0.0000",
      "Type": "POST",
      "text": "Texto do post",
      "time": 1234567890
    }
  ]
}
```

#### Atualizar um Post
**PUT:** `/api/<subject_code>/?id=<post_id>`  
**Envio:**
```json
{
  "text": "Texto atualizado do post",
  "time": 1234567891
}
```
**Recebimento:**
```json
{
  "status": "success",
  "modified_count": 1
}
```

#### Deletar Posts
**DELETE:** `/api/<subject_code>/`  
**Envio:**
```json
{
  "User": "00.0.0000"
}
```
**Recebimento:**
```json
{
  "status": "success",
  "deleted_count": 1
}
```

### Exemplo de JSON de Post

```json
{
  "_id": "60b1234567890abcdef12345",
  "User": "00.0.0000",
  "Type": "POST",
  "text": "Texto do post",
  "time": 1234567890
}
```

## Contato

Para mais informações ou ajuda, entre em contato com [email@example.com].
```

Esse `README.md` contém todas as rotas relevantes para o sistema de fóruns, junto com exemplos de uso e instruções para rodar o projeto.