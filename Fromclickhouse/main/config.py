import os


# uncomment the line below for postgres database url from environment variable
# postgres_local_base = os.environ['DATABASE_URL']

# basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious_secret_key")
    DEBUG = False
    PORT = os.getenv("PORT", 30037)
    DEVICE_DATA_URL = os.getenv("DEVICE_DATA_URL", "192.168.3.228")
    RESTX_MASK_SWAGGER = False

    MQ_CONFIG = os.getenv("MQ_CONFIG", {
        "IP_PORT": "192.168.3.235:9876",
        "ACCEPT_TOPIC": "chelion_algorithms_py_topic",
        "SEND_TOPIC": "chelion_algorithms_py_to_java_topic",
        "ACCEPT_GROUP_NAME": "chelion_group_tariff",
        "SEND_GROUP_NAME": "chelion_group_algorithms"
    })

    REDIS_CONFIG = os.getenv("REDIS_CONFIG", {
        "host": "192.168.3.248",
        "port": 6379,
        "db": 3,
        "password": "Chelion999",
        "ex": 60 * 10
    })


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    # TESTING = True
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    # PRESERVE_CONTEXT_ON_EXCEPTION = False
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(dev=DevelopmentConfig, test=TestingConfig, prod=ProductionConfig)

key = Config.SECRET_KEY
