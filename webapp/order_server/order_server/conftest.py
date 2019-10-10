import os
import django
from django.conf import settings

# We manually designate which settings we will be using in an environment variable
# This is similar to what occurs in the `manage.py`
profile = os.environ.get('PROFILE', 'develop')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'order_server.settings.%s' % profile)


# `pytest` automatically calls this function once when tests are run.
def pytest_configure():
    settings.DEBUG = False
    # If you have any test specific settings, you can declare them here,
    # e.g.
    # settings.PASSWORD_HASHERS = (
    #     'django.contrib.auth.hashers.MD5PasswordHasher',
    # )
    settings.DATABASES['default'] = {
        'NAME': os.path.join(settings.BASE_DIR, 'test_db.sqlite3'),
        # 'NAME': 'test_db.sqlite3',
        'ENGINE': 'django.db.backends.sqlite3',
    }


    # settings.REST_FRAMEWORK = {
    #     'DEFAULT_PERMISSION_CLASSES': [
    #         'rest_framework.permissions.AllowAny', 
    #     ]
    # }

    django.setup()
    # Note: In Django =< 1.6 you'll need to run this instead
    # settings.configure()