"""
Django settings for guerradevotos project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
PROJECT_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)))

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT,'static')

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, 'static'),
)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'templates'),
)

ADMINS = {
    ('Ramon Zuniga', 'ramonzuniga9@gmail.com'),
}

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_hatw*0kj+2ut1%6bgbuuaavvizhlg_x7w==jhs$u=fxa#f2&)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',
    'social_auth',
    'appengine_toolkit',
)


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'social_auth.context_processors.social_auth_by_type_backends',
    'guerradevotos.context_processor.user_picture',
)

FACEBOOK_APP_ID='269238803250226'
FACEBOOK_API_SECRET='d0e17ed2e711e8437f0ccc27c2d0fa4b'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/main/'
LOGIN_ERROR_URL = '/login-error/'
MAIN = '/'

SOCIAL_AUTH_ENABLED_BACKENDS = ('facebook',)
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

FACEBOOK_EXTENDED_PERMISSIONS = ['email']

# SOCIAL_AUTH_PIPELINE = (
#     'social_auth.backends.pipeline.social.social_auth_user',
#     'social_auth.backends.pipeline.associate.associate_by_email',
#     'social_auth.backends.pipeline.user.get_username',
#     'social_auth.backends.pipeline.user.create_user',
#     'social_auth.backends.pipeline.social.associate_user',
#     'social_auth.backends.pipeline.user.update_user_details',
#     'guerradevotos.pipeline.update_avatar',
# )
 
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'guerradevotos.urls'

WSGI_APPLICATION = 'guerradevotos.wsgi.application'

SESSION_SERIALIZER='django.contrib.sessions.serializers.PickleSerializer'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
import appengine_toolkit
DATABASES = {
    'default': appengine_toolkit.config(),
}

APPENGINE_TOOLKIT = {
    'APP_YAML': os.path.join(BASE_DIR, 'app.yaml'),
    'BUCKET_NAME': 'gdv-bucket',
}

# DEFAULT_FILE_STORAGE = 'appengine_toolkit.storage.GoogleCloudStorage'
# STATICFILE_STORAGE = 'appengine_toolkit.storage.GoogleCloudStorage'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Media files (file uploads)

MEDIA_URL = '/media/'
