FROM postgres:latest

# Definir variáveis de ambiente para configurar o PostgreSQL
ENV POSTGRES_DB=tp_eng2
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=1234

# Diretório onde os scripts SQL de inicialização serão copiados
# Esses scripts serão executados automaticamente na inicialização do contêiner
COPY ./initdb /docker-entrypoint-initdb.d/

# Expor a porta padrão do PostgreSQL
EXPOSE 5432
