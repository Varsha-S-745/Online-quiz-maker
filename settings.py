import os
from pathlib import Path
from .config import *

base_dir = Path(__file__).resolve(strict=True).parent.parent

secret_key = os.getenv('DJANGO_SECRET_KEY', 'i_x-#xe=e6xo64m&(=p6nis^9b13xhr)*n1332g6+e16*ddwam')
debug = os.getenv('DJANGO_DEBUG', 'True') == 'True'
allowed_hosts = ['*']

static_url = '/static/'
static_root = os.path.join(base_dir, 'static')

media_url = '/media/'
media_root = os.path.join(base_dir, 'media')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Accounts.apps.AccountsConfig',
    'ExamManagement.apps.ExammanagementConfig',
    'ResultManagement.apps.ResultmanagementConfig',
    'AnswerManagement.apps.AnswermanagementConfig',
    'crispy_forms',
    'matplotlib',
]

crispy_template_pack = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'OnlineQuizPlatform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(base_dir, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'Accounts.processor_context.check',
            ],
        },
    },
]

WSGI_APPLICATION = 'OnlineQuizPlatform.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': base_dir / 'db.sqlite3',
    }
}

login_url = '/login'
logout_url = '/logout'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = email_acc
EMAIL_HOST_PASSWORD = password
