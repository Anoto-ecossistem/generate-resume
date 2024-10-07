# Website in Django for generate resume and other things.

![header](https://github.com/user-attachments/assets/0e5161cb-229f-4403-817a-afb248314fe9)
![resumegenerator](https://github.com/user-attachments/assets/39567f62-7e98-45c7-88c0-98bc0fbe9a5f)
![jobs](https://github.com/user-attachments/assets/f4570bf5-3a26-499a-af20-788743fe3847)
![footer](https://github.com/user-attachments/assets/ccddd470-c241-4aa6-b3ba-74823567b0ff)

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
