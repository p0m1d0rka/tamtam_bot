import logging.config
from config.base import Config


def create_logger(name):
    logger_config = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'std_format': {
                'format': '{asctime} | {levelname} | {name} | {module}:{funcName}:{lineno} | {message}',
                'style': '{'
            }
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'level': Config.log_level,
                'formatter': 'std_format'
            }
        },
        'loggers': {
            name: {
                'level': 'DEBUG',
                'handlers': ['console']
                # 'propagate': False
            }
        }
    }
    logging.config.dictConfig(logger_config)
    logger = logging.getLogger(name)

    return logger


