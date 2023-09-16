import logging.config
import os
from os import path

LOGGING = {
    "version": 1,
    "formatters": {
        "verbose": {
            "format": "[%(asctime)s] %(levelname)s [%(pathname)s:%(lineno)s] %(message)s",# NOQA
            "datefmt": "%m/%d/%Y %H:%M:%S",
        },
        "simple": {"format": "%(levelname)s %(message)s"},
    },
    "handlers": {
        "log_file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": path.join(os.getcwd(), "project.log"),
            "formatter": "verbose",
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "project": {
            "handlers": ["log_file", "console"],
            "propagate": False,
            "level": "DEBUG",
        },
    }
}

logging.config.dictConfig(LOGGING)
