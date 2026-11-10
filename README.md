# Lista de tarefas — Django

Projeto de estudos com Django e SQLite.

## Executar localmente

Use Python 3.12 ou superior. A partir da raiz do repositório:

```bash
cd listar_tarefas
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse <http://127.0.0.1:8000/>. Para criar um usuário administrador,
execute `python manage.py createsuperuser`.

## Verificações

Com o ambiente ativado, dentro de `listar_tarefas`:

```bash
python manage.py check
python manage.py test
```

## Controle de versão

O ambiente virtual, os caches Python, arquivos `.env` e o banco SQLite local
são ignorados pelo Git. O banco é criado pelo comando `migrate`; as migrations
permanecem versionadas, assim como o código e os templates.

As configurações atuais são destinadas ao desenvolvimento local.
