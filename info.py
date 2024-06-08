# (c) @biisal
from os import getenv
import re

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


ADMIN = int(getenv("ADMIN", "6987799874"))
API_ID = int(getenv("API_ID", "23171051"))
API_HASH = str(getenv("API_HASH", "10331d5d712364f57ffdd23417f4513c"))
BOT_TOKEN = str(getenv("BOT_TOKEN", "7343805166:AAHtmz0TxF0mq5YmJGnEEFYSDc2GPH9vgyA"))
MONGO_DB = str(
    getenv(
        "MONGO_DB",
        "mongodb+srv://tmr624062:2fS3ifhHtKRaLWQZ@cluster0.3gpzrlg.mongodb.net/?retryWrites=true&w=majority",
    )
)
DEF_CAP = str(
    getenv(
        "DEF_CAP",
        "<b><a href='telegram.me/bisal_files'>{file_name} Telegram : @Bisal_Files\n\nForward the file before Downloading.</a></b>",
    )
)
