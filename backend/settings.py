from .settings_common import *
import os


DEBUG = False
ALLOWED_HOSTS = ["*"]

STATIC_ROOT = os.path.join(BASE_DIR,"static")
MEDIA_ROOT = os.path.join(BASE_DIR,"media")

# settings of logging
LOGGING = {
    "version": 1,
    "disable_exisiting_logger": False,

    # Logger 
    "loggers": {
        # Logger for django
        "django" : {
            "handlers":["file"],
            "level": "INFO",
        },
        # Logger for coupon application
        "coupon":{
            "handlers":["file"],
            "level": "INFO",
        }
    },

    # Settings of handlers
    "handlers" : {
       "file": {
            "level" : "INFO",
            "class" : "logging.handlers.TimedRotatingFileHandler",
            "filename" : os.path.join(BASE_DIR, "logs/django.log",),
            "formatter": "prod",
            "when": "D",
            "interval": 1,
            "backupCount":7,
        },
    },

    # Settings of formatter
    "formatters": {
        "prod" : {
            "format" : "\t".join([
                "%(asctime)s",
                "[%(levelname)s]",
                "%(pathname)s(Line:%(lineno)d",
                "%(message)s"
            ])
        },
    }
}