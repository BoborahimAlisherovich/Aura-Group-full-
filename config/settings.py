from pathlib import Path
import os
from dotenv import load_dotenv
from django.utils.translation import gettext_lazy as _

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9t*^^qi)nln5&uh@#ssxn70t_3zk3ob#0qq&4yhvc*3$owqa6w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',  # django-modeltranslation - MUHIM: admin'dan oldin
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'phonenumber_field',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auragroup',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Statik fayllarni tezlashtirish
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'



# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'uz'

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



LANGUAGES = [
    ('uz', 'Oʻzbekcha'),
    ('ru', 'Русский'),
    ('en', 'English'),
]

# Modeltranslation sozlamalari
MODELTRANSLATION_DEFAULT_LANGUAGE = 'uz'
MODELTRANSLATION_LANGUAGES = ('uz', 'ru', 'en')

LANGUAGE_SESSION_KEY = 'django_language'

LANGUAGE_COOKIE_NAME = 'django_language'
LANGUAGE_COOKIE_AGE = 365 * 24 * 60 * 60  # 1 yil

# JAZZMIN KONFIGURATSIYASI - ADMIN PANELNI O'ZBEKCHAGA O'TKAZISH
JAZZMIN_SETTINGS = {
    "site_title": "AURA Group Admin",
    "site_header": "AURA Group",
    "site_brand": "AURA Group",
    "login_logo": None,
    "login_logo_dark": None,
    "site_logo_classes": "img-circle",
    "welcome_sign": "AURA Group Admin Paneli'ga Xush Kelibsiz",
    "copyright": "AURA Group © 2024. Barcha huquqlar himoyalangan.",
    "search_model": ["auth.User", "auth.Group"],
    "user_avatar": None,
    "topmenu_links": [
        {"name": "Bosh sahifa", "url": "admin:index", "permissions": ["auth.add_user"]},
        {"name": "Saytga Qaytish", "url": "/", "new_window": True},
    ],
    "usermenu_links": [
        {"model": "auth.user"}
    ],
    "show_sidebar": True,
    "navigation_expanded": True,
    "hide_apps": [],
    "hide_models": [],
    "order_with_respect_to": ["auth", "auragroup"],
    "custom_css": None,
    "custom_js": None,
    "show_ui_builder": False,
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
    "language_chooser": True,
}
