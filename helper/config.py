from . import *

try:
    APP_ID = "2592026"
    API_HASH = "3c9ac728ca56eb0ab9b3b9bc55c48527"
    BOT_TOKEN = "5336358877:AAGdqr4HThCwK6O9mY7_F3AIZkrgQtC7WYo"
    OWNER = config("OWNER_ID", default=1264599494, cast=int)
    LOG = "1683924615"
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
