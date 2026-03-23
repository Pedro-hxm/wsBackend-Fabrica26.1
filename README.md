# wsBackend-Fabrica26.1

🍲 **RecipeApp**

**Seu gerenciador digital de receitas.**

Sistema web completo para gerenciamento de receitas culinárias. O RecipeApp permite que usuários criem suas contas, cadastrem receitas com ingredientes detalhados, salvem receitas favoritas e importem receitas de uma API externa.

---

## 🎯 Objetivo do projeto

Construir um backend profissional em Django com recursos de:
- CRUD completo de receitas
- Relacionamento de entidades (receita, ingrediente, quantidade/unidade)
- Autenticação de usuário e rotas protegidas
- Integração com API externa (TheMealDB)
- Persistência em banco relacional (SQLite)
- Deploy via Docker/Docker Compose

---

## ✅ Funcionalidades principais

### 🔐 Autenticação
- Cadastro de usuário (`/cadastro/`)
- Login (`/login/`)
- Logout (`/logout/`)
- Proteção de rotas via `@login_required`

### 🍲 CRUD de receitas
- Criar, listar, editar e excluir receitas
- Receita com imagens, categoria e instruções
- Gerenciar receitas em painel próprio (`/receitas/gerenciar/`)

### 🧂 Ingredientes
- Ingredientes vinculados à receita via tabela associativa (`ReceitaIngrediente`)
- Armazenamento de quantidade e unidade
- Reutilização automática de ingredientes ao criar novas receitas

### ❤️ Favoritos
- Usuário pode favoritar receitas
- Visualização de favoritos em página principal

### 🔍 Integração com TheMealDB
- Busca (`/?busca=nome`) em API externa
- Importação de receita (`/salvar-api/<id>/`)
- Conversão do modelo API para o modelo local (ingredientes, medidas, instruções)

### 🐳 Docker
- Containerização do projeto com `Dockerfile` e `docker-compose.yml`
- Execução simplificada em `http://localhost:8000`

---

## 🛠 Tecnologias utilizadas

- Python 3.12+
- Django 6.0
- SQLite
- Requests
- Docker & Docker Compose
- HTML5/CSS3 (templates Django)
- API externa: TheMealDB

---

## 📁 Estrutura do projeto
```
├── 📁 config
│   ├── 🐍 __init__.py
│   ├── 🐍 asgi.py
│   ├── 🐍 settings.py
│   ├── 🐍 urls.py
│   └── 🐍 wsgi.py
├── 📁 recipes
│   ├── 📁 migrations
│   │   ├── 🐍 0001_initial.py
│   │   ├── 🐍 0002_rename_ingradiente_ingrediente_rename_recipe_receita_and_more.py
│   │   └── 🐍 __init__.py
│   ├── 📁 templates
│   │   └── 📁 recipes
│   │       ├── 🌐 cadastro.html
│   │       ├── 🌐 criar_receita.html
│   │       ├── 🌐 editar_receita.html
│   │       ├── 🌐 excluir_receita.html
│   │       ├── 🌐 gerenciar_receitas.html
│   │       ├── 🌐 login.html
│   │       └── 🌐 recipes.html
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 urls.py
│   └── 🐍 views.py
├── ⚙️ .dockerignore
├── ⚙️ .gitignore
├── 🐳 Dockerfile
├── 📝 README.md
├── ⚙️ docker-compose.yml
├── 🐍 manage.py
└── 📄 requirements.txt
```

---

## 🔗 Rotas principais

### Receitas
| Método | Rota | Descrição |
| ------ | ---- | --------- |
| GET | `/` | Página inicial com receitas + busca API + favoritos |
| GET/POST | `/receitas/criar/` | Criar nova receita |
| GET | `/receitas/gerenciar/` | Listar receitas |
| GET/POST | `/receitas/<id>/editar/` | Editar receita |
| GET/POST | `/receitas/<id>/excluir/` | Excluir receita |
| POST | `/recipes/<id>/` | Favoritar receita |

### API externa interna
| Método | Rota | Descrição |
| ------ | ---- | --------- |
| GET | `/?busca=nome` | Buscar receitas na API TheMealDB |
| POST | `/salvar-api/<id>/` | Salvar receita da API no sistema |

### Autenticação
| Método | Rota | Descrição |
| ------ | ---- | --------- |
| GET/POST | `/cadastro/` | Criar conta |
| GET/POST | `/login/` | Login |
| GET | `/logout/` | Logout |

---

## 📋 Modelos Django

### `Ingrediente`
- `nome` (CharField)

### `Receita`
- `nome`, `categoria`, `imagens`, `instrucoes`
- `ingradientes` (ManyToMany com `Ingrediente`, through `ReceitaIngrediente`)

### `ReceitaIngrediente`
- `receita` (FK)
- `ingrediente` (FK)
- `quantidade` + `unidade`

### `Favoritos`
- `usuario` (FK `User`)
- `receita` (FK `Receita`)

---

## ⚙️ Instalação e execução

### Pré-requisitos
- Python 3.10+
- Git
- Docker (opcional)

### Passos
1. Clonar o projeto
   ```bash
git clone https://github.com/seu-usuario/wsBackend-Fabrica26.1.git
cd wsBackend-Fabrica26.1
```
2. Criar e ativar ambiente virtual
   ```bash
python -m venv venv
venv\Scripts\activate
```
3. Instalar dependências
   ```bash
pip install -r requirements.txt
```
4. Rodar migrações
   ```bash
python manage.py migrate
```
5. Criar superusuário
   ```bash
python manage.py createsuperuser
```
6. Iniciar servidor
   ```bash
python manage.py runserver
```

Visitar: `http://localhost:8000`

### Usando Docker
```bash
docker compose up --build
```

---

## 🧠 Decisões de projeto

- Ingredientes são cadastrados com receitas para simplificar UX.
- Tabela intermediária (`ReceitaIngrediente`) armazena quantidade/unidade.
- API externa (TheMealDB) enriquece o catálogo.
- Docker padroniza ambiente de desenvolvimento/produção.

---

## 👨‍💻 Autor

Desenvolvido por Pedro Henrique
