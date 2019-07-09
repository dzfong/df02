"""
Django settings for test1 project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# 
# 项目目录的绝对路径
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'idjwk+q$o83bw-t@j6l!jjp^74!^*46#rm6%lb(b7=4i((qsa0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True                        # 调试窗口， 正常网站运行，这里改成 False
# DEBUG = False

# ALLOWED_HOSTS = []                  # 如果 debug设置为False 那么这里也需要设置， 允许哪些地址访问网站 ； 允许所有那么 ALLOWED_HOSTS = ['*'] 
ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'booktest',                      # 添加应用名称
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',          # 默认开启了csrf防护，只针对post提交
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'booktest.middleware.BlockedIPSMiddleware',            # 注册自定义的中间件类
]

ROOT_URLCONF = 'test1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',       # 引擎
        'DIRS': [os.path.join(BASE_DIR, 'templates')],       # 模板目录文件夹路径, 把项目路径和模板文件夹拼接起来
        'APP_DIRS': True,                                    # 如果上面的 dirs 没有定义，这里显示 True 的是会去应用目录找
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins': [                                   # 添加此属性，导入static文件，就不需要在html首行导入 static了
                'django.templatetags.static'
            ],
        },
    },
]

WSGI_APPLICATION = 'test1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',                 #  可以更改数据库为 MySQL
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'                        # 语言设置成中文

# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'                       # 地区设置成上海

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'                                         # 设置访问静态文件对应的url地址
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]           # 设置静态文件的保存目录


MEDIA_ROOT = os.path.join(BASE_DIR, 'static/media')             # 设置上传文件的保存目录