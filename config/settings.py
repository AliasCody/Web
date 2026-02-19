from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# 載入 .env 檔案
load_dotenv(BASE_DIR / ".env")

# 🔑 不要直接寫在程式裡，改用環境變數
# 注意：在生產環境（Render）中，如果沒有設定 DJANGO_SECRET_KEY，程式應該報錯
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")
if not SECRET_KEY and not DEBUG:
    raise ValueError("DJANGO_SECRET_KEY environment variable is not set!")
elif not SECRET_KEY:
    SECRET_KEY = "django-insecure-fallback-key-for-local-dev"

# 記得把 DEBUG 設為根據環境變數決定（Render 上通常是 False）
DEBUG = os.environ.get("DEBUG", "True").lower() == "true"

# 允許本機測試 + Render 部署的域名 (從環境變數讀取，預設為本機)
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# 資料庫設定：優先使用 DATABASE_URL (Render)，若無則使用 SQLite (本機)
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        conn_max_age=600
    )
}


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        'OPTIONS': {'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ]},
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases



# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'zh-hant'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise 設定：幫助在生產環境處理靜態檔案
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
'''
    Telling Django how to store and manage files
    "whitenoise.storage.CompressedManifestStaticFilesStorage" will help you compressed and manifest(快取管理，幫忙上一串亂碼，這樣你更新內容的時候使用者瀏覽器會直接發現並讀取新的檔案)
'''
# STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
# 生產環境安全設定
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT", "False").lower() == "true"
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
