from os  import environ

class Config:
    """
    app config
    """
    # tamtam access_token
    access_token = environ["access_token"]

    # base url for tamtamapi
    base_url = 'https://botapi.tamtam.chat'

    # log level:
    # 10 - DEBUG
    # 20 - INFO
    # 30 - WARNING
    # 40 - ERROR
    # 50 - CRITICAL
    log_level = 10


