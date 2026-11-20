# Módulo 3 – Django

Diferente dos módulos anteriores, as aulas 19 a 29 constroem **um único projeto, de forma cumulativa**:
[`djangobasico/`](djangobasico). Cada aula acrescenta uma camada (rotas, templates, models, admin…), então o
repositório mostra o **resultado final** e esta página indica **o que pertence a cada aula**.

## Executando o projeto

Requer **Python 3.12+**. A partir de `modulo-3-django/djangobasico`:

```bash
python -m venv .venv
.venv\Scripts\activate            # macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata clientes   # 5 clientes de exemplo (opcional)
python manage.py createsuperuser     # usuário para a área administrativa
python manage.py runserver
```

Abra <http://127.0.0.1:8000/>. Para outra porta: `python manage.py runserver 8888`.

Testes automatizados: `python manage.py test`.

## Mapa das aulas

| Aula | Assunto | Onde ver no projeto |
| --- | --- | --- |
| **19** Introdução | O que é o Django; `pip install django`, `django-admin startproject djangobasico .`, `runserver` | `manage.py`, pacote `djangobasico/` (`settings.py`, `urls.py`, `asgi.py`, `wsgi.py`) |
| **20** Padrão MTV | *Model – View – Template*; projeto × aplicação | Uma pasta por app: `inicio`, `produtos`, `clientes` |
| **21** Configurações e apps | `DEBUG`, `ALLOWED_HOSTS`, `LANGUAGE_CODE='pt-br'`, `startapp`, `INSTALLED_APPS`, `urls.py` com `include()` | `djangobasico/settings.py`, `djangobasico/urls.py`, `produtos/` |
| **22** Renderizando HTML | `startapp clientes`, `templates/clientes/index.html`, `render()` | `clientes/templates/`, `clientes/views.py` |
| **23** Rotas e app inicial | Rota raiz `''`, app `inicio` | `inicio/` |
| **24** Templates | Django Template Language: `{{ }}`, `{% for %}`, filtro `\|length` | `produtos/views.py`, `produtos/templates/produtos/index.html` |
| **25** Models e persistência | `models.Model`, `makemigrations`, `migrate`, SQLite | `clientes/models.py`, `clientes/migrations/` |
| **26** Área administrativa | `createsuperuser`, `admin.py`, `__str__`, `ModelAdmin` | `clientes/admin.py` → <http://127.0.0.1:8000/admin/> |
| **27** Shell | `python manage.py shell`, `save()`, `objects.all()`, `filter()` | veja a seção abaixo |
| **28** Lista de dados do BD | View lê o Model e envia ao Template; página de cada cliente | `clientes/views.py`, `urls.py`, `item_cliente.html` |
| **29** Arquivos estáticos | `static/css`, `static/js`, `static/images`, `STATIC_ROOT`, `{% static %}` | `clientes/static/`, `djangobasico/settings.py` |

## Comandos da aula 27 (shell)

```bash
python manage.py shell
```

```python
from clientes.models import Cliente

cliente = Cliente(nome="Rafaela de Alencar", email="rafaela@email.com", nascimento="2001-11-27")
cliente.save()

cliente.id, cliente.pk
print(cliente)

cliente.nascimento = "2000-01-01"
cliente.save()

dir(cliente)  # o que um objeto Cliente sabe fazer
dir(Cliente.objects)  # o que o "gerenciador" de consultas sabe fazer

Cliente.objects.all()
Cliente.objects.count()
Cliente.objects.filter(id=1)
```

No slide aparecem `Clientes.objects.filter(...)` e `Cliente.objetcs`; o correto é `Cliente.objects`.

## Modernizações e correções em relação aos slides

- **Segredos fora do código**: `SECRET_KEY`, `DEBUG` e `ALLOWED_HOSTS` vêm de variáveis de ambiente
  (`DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`). Sem elas, o projeto roda em modo de desenvolvimento.
  O slide sugere `ALLOWED_HOSTS = ['*']`; aqui isso só vale com `DEBUG=True`.
- `STATIC_ROOT = BASE_DIR / 'staticfiles'` com `pathlib` (o slide usa `os.path.join`).
- **Namespaces de rotas** (`app_name`) e `{% url 'clientes:cliente_id' cliente.id %}`: evitam conflito de nomes entre apps.
- Rota com conversor de tipo `<int:id>/` e `get_object_or_404`: um id inexistente devolve **404** em vez de erro 500.
- `{% for %}...{% empty %}` mostra uma mensagem quando não há clientes; datas formatadas com `|date:"d/m/Y"`.
- Preços como `Decimal` (nunca `float` para dinheiro) com `|floatformat:"2g"` → `5.250,00`.
- `@admin.register(Cliente)`, `Meta.ordering`, `search_fields` e `list_filter` no admin.
- JavaScript com `addEventListener` em vez de `onclick=""` no HTML.
- CSS: `text_decoration` (inválido) corrigido para `text-decoration`.
- Imagem `pessoas.png` substituída por `pessoas.svg` (leve e sem direitos autorais).
- Corrigidas as aspas "curvas" (`'4550.00’`) que quebrariam o dicionário do slide 24.
- `fixtures/clientes.json` e testes (`tests.py` de cada app) para validar o que as aulas constroem.

## Para ir para produção (fora do escopo do curso)

`python manage.py check --deploy` lista o que falta (HTTPS, cookies seguros, HSTS, `SECRET_KEY` forte,
`ALLOWED_HOSTS`, backend de e-mail real). O banco SQLite (`db.sqlite3`) **não é versionado**: está no `.gitignore`.
