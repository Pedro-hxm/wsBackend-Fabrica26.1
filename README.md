# wsBackend-Fabrica26.1

🍲 RecipeApp








Seu gerenciador digital de receitas.

Sistema web completo para gerenciamento de receitas culinárias. O RecipeApp permite que usuários criem suas contas, cadastrem receitas com ingredientes detalhados, salvem receitas favoritas e importem receitas de uma API externa.

🎯 Escopo e Requisitos

Este projeto foi desenvolvido atendendo aos requisitos técnicos propostos, demonstrando competências em desenvolvimento Full Stack com foco em Backend:

✅ CRUD Completo: Criação, leitura, atualização e exclusão de receitas.
✅ Relacionamento de Entidades: Receita, Ingrediente e relação com quantidade/unidade.
✅ Autenticação: Sistema de login, cadastro e rotas protegidas (@login_required).
✅ Integração com API: Consumo da API externa TheMealDB.
✅ Persistência de Dados: Uso de banco relacional (SQLite).
✅ Docker: Projeto containerizado com Docker e Docker Compose.
🚀 Funcionalidades
🔐 Autenticação Completa
Cadastro de usuários
Login e logout
Rotas protegidas
🍲 CRUD de Receitas
Criar receitas com ingredientes
Visualizar receitas
Editar receitas
Excluir receitas
🧂 Ingredientes Integrados
Ingredientes cadastrados junto com a receita
Controle de quantidade e unidade
Reutilização automática de ingredientes
❤️ Sistema de Favoritos
Usuário pode favoritar receitas
Listagem de receitas favoritas
🔍 Busca via API (TheMealDB)
Buscar receitas externas
Visualizar resultados
Importar receitas para o sistema
🌎 Tratamento de Dados da API
Conversão de ingredientes da API
Organização automática no banco
🐳 Docker Ready
Projeto rodando em container
Ambiente padronizado
🛠 Tecnologias Utilizadas
Back-end
Python 3.12+
Django 6.0
SQLite (desenvolvimento)
Requests (consumo de API)
Docker & Docker Compose
Front-end
HTML5 / CSS3
Templates Django
Integrações
TheMealDB API
https://www.themealdb.com/api.php
🔗 Rotas Principais
Receitas
Método	Rota	Descrição
GET	/	Página inicial com receitas
GET/POST	/receitas/criar/	Criar nova receita
GET	/receitas/gerenciar/	Listar receitas
GET/POST	/receitas/<id>/editar/	Editar receita
GET/POST	/receitas/<id>/excluir/	Excluir receita
POST	/recipes/<id>/	Favoritar receita
API
Método	Rota	Descrição
GET	/?busca=nome	Buscar receitas na API
POST	/salvar-api/<id>/	Salvar receita da API
Autenticação
Método	Rota	Descrição
GET/POST	/cadastro/	Criar conta
GET/POST	/login/	Login
GET	/logout/	Logout
📁 Estrutura do Projeto
├── config/
├── recipes/
│   ├── migrations/
│   ├── templates/recipes/
│   │   ├── cadastro.html
│   │   ├── login.html
│   │   ├── recipes.html
│   │   ├── criar_receita.html
│   │   ├── editar_receita.html
│   │   ├── excluir_receita.html
│   │   └── gerenciar_receitas.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
├── .dockerignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements.txt
⚙️ Instalação e Execução
Pré-requisitos
Python 3.10+
Git
Docker (opcional)
🔹 1. Clonar o projeto
git clone https://github.com/seu-usuario/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1
🔹 2. Criar ambiente virtual
python -m venv venv
venv\Scripts\activate
🔹 3. Instalar dependências
pip install -r requirements.txt
🔹 4. Rodar migrations
python manage.py migrate
🔹 5. Criar superusuário
python manage.py createsuperuser
🔹 6. Rodar o projeto
python manage.py runserver
🐳 Docker

Rodar com Docker:

docker compose up --build

Acesse:

http://localhost:8000
🗄 Banco de Dados
SQLite (padrão)
Tabelas criadas com:
python manage.py migrate
🔐 Autenticação

Sistema padrão do Django:

/login/
/logout/
/cadastro/
🧠 Decisões de Projeto
Ingredientes são cadastrados junto com receitas (mais natural para o usuário)
Uso de tabela intermediária (ReceitaIngrediente) para armazenar quantidade e unidade
API externa integrada para enriquecer dados
Docker utilizado para padronização do ambiente
👨‍💻 Autor

Desenvolvido por Pedro Henrique