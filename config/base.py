from os import environ
from app.errors import NoTokenError


def get_config_val(name, default):
    return environ.get(name) if environ.get(name) else default


class Config:
    """
    app config
    """
    # tamtam access_token
    access_token = environ.get("access_token")
    if access_token is None:
        raise NoTokenError("No token provided. set token as env[access_token]")

    # base url for tamtamapi
    base_url = get_config_val("base_url", 'https://botapi.tamtam.chat')

    # log level:
    #  0 - NOTSET
    # 10 - DEBUG
    # 20 - INFO
    # 30 - WARNING
    # 40 - ERROR
    # 50 - CRITICAL
    log_level = get_config_val("log_level", "DEBUG")

    # host
    host = get_config_val("host", "0.0.0.0")

    # port
    port = get_config_val("port", "8080")
