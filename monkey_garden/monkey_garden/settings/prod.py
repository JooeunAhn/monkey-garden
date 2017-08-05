from .common import *

DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'realmonkey.mysql.database.azure.com',
        "PORT": 3306,
        "USER": "monkeyadmin@realmonkey",
        "PASSWORD": load_credential('DB_PASSWORD'),
        "NAME": "monkeydb",
    }
}
