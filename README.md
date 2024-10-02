# Website in Danjgo for generate resume and other things.

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