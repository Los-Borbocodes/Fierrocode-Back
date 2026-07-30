# Fierrocode Backend

Backend del proyecto web e-commerce "Fierrocode"

# Installation setup

1. Setup virtual enviroment and enter virtual enviroment

```bash
python -m venv .venv
source ./venv/bin/activate
```

2. Install dependencies

`pip install requirements.txt`

3. Migrate tables to database

```bash
python manage.py makemigrations
python manage.py migrate
```

4. Run project

`python manage.py runserver`

5. Profit

---
pdt: Docker deployment comming soon...
