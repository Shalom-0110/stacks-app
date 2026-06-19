"""
Django settings for Stacks.
Personal / dev configuration — no paid external services required.
"""

import os
import sys
from pathlib import Path

import dj_database_url
from django.urls import reverse_lazy

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("EXP_DJANGO_SECRET_KEY", "dev-secret-key-change-in-production")  # nosec

DEBUG = os.environ.get("EXP_DEBUG", "True") == "True"

ALLOWED_HOSTS = os.environ.get("EXP_ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_filters",
    "rest_framework",
    "rest_framework.authtoken",
    "expense.apps.ExpenseConfig",
    "corsheaders",
    "social_django",
    "import_export",
    "easy_thumbnails",
    "django.contrib.humanize",
    "finflow.apps.FinflowConfig",
    "industrial_iot.apps.IndustrialIotConfig",
    "js_clown.apps.JsClownConfig",
    "integrations.apps.IntegrationsConfig",
    "ecommerce.apps.EcommerceConfig",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "finflow.middleware.PatchRequestMiddleware",
    "finflow.timezone_middleware.TimezoneMiddleware",
]

IS_DOKKU = os.environ.get("DATABASE_URL") is not None
if IS_DOKKU:
    MIDDLEWARE.insert(2, "whitenoise.middleware.WhiteNoiseMiddleware")

ROOT_URLCONF = "bridge_expense.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = "bridge_expense.wsgi.application"


# Database — defaults to SQLite so the app runs with zero setup.
# Set EXP_POSTGRES_HOST (or DATABASE_URL) to switch to Postgres.

if os.environ.get("EXP_POSTGRES_HOST"):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "HOST": os.getenv("EXP_POSTGRES_HOST"),
            "NAME": os.getenv("EXP_POSTGRES_DATABASE"),
            "USER": os.getenv("EXP_POSTGRES_USER"),
            "PASSWORD": os.getenv("EXP_POSTGRES_PASSWORD"),
            "PORT": os.getenv("EXP_POSTGRES_PORT"),
            "ATOMIC_REQUESTS": True,
            "TEST": {
                "NAME": "EXP_test_db",
            },
        },
    }
elif os.environ.get("DATABASE_URL"):
    DATABASES = {"default": dj_database_url.config()}
    DATABASES["default"]["ATOMIC_REQUESTS"] = True
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
            "ATOMIC_REQUESTS": True,
        }
    }


if "test" in sys.argv:

    class DisableMigrations:
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation.NumericPasswordValidator"
        ),
    },
]


# Internationalisation

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True
TIME_FORMAT = "P"
ISO_8601 = "Y-m-d G:i:s"
STRFTIME_DATE_FORMAT = "%B %-d, %Y"
STRFTIME_TIME_FORMAT = "%-I:%M %p"
STRFTIME_DATETIME_FORMAT = f"{STRFTIME_DATE_FORMAT} {STRFTIME_TIME_FORMAT}"


# Static files

STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR / "static"
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Django Vite
DJANGO_VITE_ASSETS_PATH = BASE_DIR / "expense" / "static" / "expense"
DJANGO_VITE_DEV_MODE = False
DJANGO_VITE_MANIFEST_PATH = (
    BASE_DIR / "expense" / "static" / "expense" / ".vite" / "manifest.json"
)

STATICFILES_DIRS = [BASE_DIR / "global_static"]

LOGIN_URL = reverse_lazy("login")
LOGIN_REDIRECT_URL = reverse_lazy("home")
LOGOUT_URL = reverse_lazy("logout")


# DRF

REST_FRAMEWORK = {
    "DATETIME_FORMAT": STRFTIME_DATETIME_FORMAT,
    "TIME_FORMAT": STRFTIME_TIME_FORMAT,
    "DATE_FORMAT": "iso-8601",
    "DATE_INPUT_FORMATS": ["iso-8601", "%b %d, %Y"],
    "TIME_INPUT_FORMATS": ["%I:%M %p", "iso-8601"],
    "DATETIME_INPUT_FORMATS": ["%Y-%m-%d %I:%M %p", "iso-8601"],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend"
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PARSER_CLASSES": (
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
    ),
    "DEFAULT_PAGINATION_CLASS": (
        "finflow.pagination.FarbenPageNumberPagination"
    ),
    "PAGE_SIZE": 3,
}


# Media / file uploads — always local filesystem, no S3 needed

MEDIA_ROOT = BASE_DIR / "media"
MEDIA_URL = "/media/"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

THUMBNAIL_DEFAULT_STORAGE_ALIAS = "default"


# Celery — runs tasks synchronously in dev so Redis is not required.
# Set CELERY_TASK_ALWAYS_EAGER=False and provide EXP_CELERY_BROKER_URL
# if you want async background jobs.

CELERY_TASK_ALWAYS_EAGER = True
CELERY_BROKER_URL = os.getenv("EXP_CELERY_BROKER_URL", "memory://")
CELERY_RESULT_BACKEND = "cache+memory://"
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "UTC"


# Email — prints to the terminal in dev, no SMTP account needed.
# To send real emails set EMAIL_BACKEND to smtp and provide credentials.

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
DEFAULT_FROM_EMAIL = "stacks@localhost"
ENABLE_OUTGOING_EMAIL = False
FQDN = os.getenv("EXP_FQDN", "localhost")
BASE_URL = os.getenv("EXP_BASE_URL", "http://localhost:8000")


# CORS / CSRF — localhost only for personal dev

CORS_ALLOWED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:5173",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5173",
]

CORS_ALLOW_METHODS = (
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
)

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://localhost:5173",
    "http://127.0.0.1:8000",
    "http://127.0.0.1:5173",
]


# Google OAuth (optional — only needed if you want "Sign in with Google")
# Leave blank to use username/password login only.

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv("EXP_GOOGLE_OAUTH_CLIENT_ID", "")
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv("EXP_GOOGLE_OAUTH_CLIENT_SECRET", "")
SOCIAL_AUTH_JSONFIELD_ENABLED = True
SOCIAL_AUTH_REQUIRE_POST = False

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SOCIAL_AUTH_PIPELINE = (
    "social_core.pipeline.social_auth.social_details",
    "social_core.pipeline.social_auth.social_uid",
    "social_core.pipeline.social_auth.social_user",
    "finflow.social_pipeline.require_tenant_domain",
    "finflow.social_pipeline.handle_user_oauth_login",
    "social_core.pipeline.social_auth.associate_user",
    "social_core.pipeline.social_auth.load_extra_data",
    "social_core.pipeline.user.user_details",
)


# Logging

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{asctime}] {levelname}: {name}.{message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}


# js_clown (internal code-gen tool)

JS_CLOWN_TEMPLATES_PREFIX = "js_clown"
JS_CLOWN_ASSETS_ROOT = (
    BASE_DIR / "js_clown" / "templates" / "js_clown" / "assets"
)
JS_CLOWN_OUTPUT_DIRECTORY = (
    BASE_DIR / "expense" / "static_dev" / "expense" / "src" / "components.gen"
)
