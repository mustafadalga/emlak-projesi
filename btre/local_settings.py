
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x2h=+echhh7termal4*scq+_yq@(ix!1ogi*ra-gp(+h5g1_se'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['35.238.168.6']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'btre_prod',
        'USER':'dbadmin',
        'PASSWORD':'123456',
        'HOST':'localhost'
    }
}

#Email config
EMAIL_HOST="smtp.gmail.com"
EMAIL_PORT=587
EMAIL_HOST_USER=""
EMAIL_HOST_PASSWORD=""
EMAIL_USE_TLS=True
