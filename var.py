from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", "18810284")
    API_HASH = config("API_HASH", "4b137145eaab2e278fdaf91197c79040")
    BOT_TOKEN = config("BOT_TOKEN", "5575988245:AAGuSFl4yKl8k6UojMTH6lauD5APZafSIG8")
    SUDO = list(map(int, getenv("SUDO", "5340100457").split()))
