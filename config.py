import os

from setup import basedir


class BaseConfig(object):
    MONGODB_SETTINGS = {
        'USERNAME': 'lohithn4mlab',
        'PASSWORD': 'lohithn4mlab',
        'HOST': 'ds157380.mlab.com',
        'PORT': 57380,
        'DB': 'demo_db'
    }
    SECRET_KEY = "SO_SECURE"
    DEBUG = True

class TestingConfig(object):
    """Development configuration."""
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
    DEBUG_TB_ENABLED = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False
