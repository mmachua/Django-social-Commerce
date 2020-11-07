from martinn.settings.base import *

#override base settings here
DEBUG = False
ALLOWED_HOSTS = ['django-env.mpaxbrtxcu.us-west-2.elasticbeanstalk.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


try:
    from martinn.settings.local import *
except:
    pass
    