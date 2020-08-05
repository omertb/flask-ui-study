class BaseConfig(object):
    DEBUG = False
    SECRET_KEY = 'YOUR_SECRET_KEY'
    # SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "postgresql://USER:PASS@localhost/DATABASE_NAME"
    SECURITY_PASSWORD_SALT = 'YOUR_SALT'

    # mail settings
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    # gmail authentication
    MAIL_USERNAME = "GMAIL_USERNAME"  # os.environ['APP_MAIL_USERNAME']
    MAIL_PASSWORD = "GMAIL_PASS"  # os.environ['APP_MAIL_PASSWORD']

    # mail accounts
    MAIL_DEFAULT_SENDER = 'SENDER_NAME'


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False