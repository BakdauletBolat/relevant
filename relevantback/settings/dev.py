from pathlib import Path

BASE_DIR_DEV = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR_DEV / 'db.sqlite3',
    }
}

DEBUG = True
