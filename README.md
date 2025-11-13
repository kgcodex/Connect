# Connect
Connect is a social media platform


# Steps to Setup 

## Backend

1. Clone this repo

2. Create a secret key

```py
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

3. Create .env file in backend/
  add

  ```
  DEBUG = True 
  DJANGO_ENV = dev | prod

  SECRET_KEY 

  DEV_DB_NAME
  PROD_DB_NAME 

  DB_USERNAME
  DB_PASSWORD 

  DB_HOST 
  DB_PORT
  ```