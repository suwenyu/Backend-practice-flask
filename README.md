# Backend-practice-flask

---

Technique:

Flask + PostgreSQL

## Set up
---

#### PostgreSQL Database:

For Dev Env
```bash
$ export DATABASE_URL="postgresql://[username]@[host]:[port]/[database]"
```

For Test Env
```bash
$ export DATABASE_URL_TEST="postgresql://[username]@[host]:[port]/[database]"
```

### Install Python Packages
```bash
$ python3 -m venv venv

$ source venv/bin/activate

$ pip install -r requirements.txt
```

---
## Start Application


1. Database Initialization

```bash
# step 1: initializing
$ python manage.py db init


# step 2: migrate new model setting
$ python manage.py db migrate --message 'initial database'

# step 3: exec new model
$ python manage.py db upgrade
```
Once modifying the models, run the step 2 and 3.

2. Run the Application
```bash
$ python manage.py run
```

3. Run the Unit Test
```bash
$ python manage.py test
```

