A playlist de Django mostrou como instalar a ferramenta e como fazer uma API simples, especificamente uma API de "To Do".

Se eu fosse propor um fluxo de pensamento para um projeto novo, eu faria o seguinte:

1. Antes de tudo, pensar no banco de dados. Vamos começar definindo as tabelas.
2. Pensar nas relações entre as tabelas, se uma depende da outra, se a relação é de 1:1, 1:N ou N:N, etc.
3. Replicar essas tabelas e relações dentro do Django usando models.py
4. Implementar o serializer para cada model para que o Django possa converter os dados em JSON/interpretar os dados JSON para salvar no banco de dados.
5. Implementar o CRUD, regras de negócio e rotas usando views.py
6. Expor as rotas criadas no views.py usando urls.py
7. Expor os modelos no dashboard do Djando usando admin.py
