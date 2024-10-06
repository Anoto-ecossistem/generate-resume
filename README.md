# Website in Danjgo for generate resume and other things.

![Captura de tela 2024-10-05 121921](https://github.com/user-attachments/assets/96f98925-0161-4a9c-bb5e-ffdd161a6f84)


## 
    This project is a Django-based application that allows users to generate resume
    

### Heroku

```bash
$ heroku create
$ heroku addons:add heroku-postgresql:hobby-dev
$ heroku pg:promote DATABASE_URL
$ heroku config:set ENVIRONMENT=PRODUCTION
$ heroku config:set DJANGO_SECRET_KEY=`./manage.py generate_secret_key`
```

## REsources

- [Django Builder](http://mmcardle.github.io/django_builder/#!/models)
- [Django and Postgres](https://wsvincent.com/django-docker-postgresql)
