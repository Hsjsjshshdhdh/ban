from decouple import config
from heroku3 import from_key
from os import getenv

class Var:
    API_ID = config("API_ID", "16279517")
    API_HASH = config("API_HASH", "c5b2041092e01edf0d8374a99766e72e")
    BOT_TOKEN = config("BOT_TOKEN", "5617125263:AAExI0sH1TKjIGnbkF75ZTM-FudKfmxT9ZI")
    SUDO = list(map(int, getenv("SUDO", "1815057109 1491415522").split()))
