import logging
import os

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)


class ENV_VARS(object):
    API_ID = int(os.environ.get("API_ID",  "26383827"))
    API_HASH = os.environ.get("API_HASH", "968980466c5527a1b494c546542582e3")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8103620901:AAF0zEFHNRs5wXeA0gJPdN_0geAbKZQooO8")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Chooducid_bot")
    #AUTH_USER = int(os.environ.get("AUTH_USER", 5071059420))


Config = ENV_VARS

handler = Config.BOT_USERNAME


class CMD(object):
    START = ["start", f"start@{handler}"]
