from lab_project.settings.base import *
import os
load_dotenv()

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = ['localhost', '127.0.0.1']
DEBUG = True


SECRET_KEY = str(os.getenv('SECRET_KEY'))

#Development database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'lab_project',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Testing database
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }