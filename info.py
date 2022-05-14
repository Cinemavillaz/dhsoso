import re
import json
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = "SESSION", "Media_search"
API_ID = "7575401"
API_HASH = "39f129688377a544d3088fbff80c05b8"
BOT_TOKEN = "5039178288:AAGXJdASd-4LGzISJoapwne4ejxILFwnoDE"

# Bot settings
CACHE_TIME = "300"
USE_CAPTION_FILTER = "USE_CAPTION_FILTER", "False"
PICS = (environ.get('PICS', 'https://telegra.ph/file/7e56d907542396289fee4.jpg https://telegra.ph/file/9aa8dd372f4739fe02d85.jpg https://telegra.ph/file/adffc5ce502f5578e2806.jpg https://telegra.ph/file/6937b60bc2617597b92fd.jpg https://telegra.ph/file/09a7abaab340143f9c7e7.jpg https://telegra.ph/file/5a82c4a59bd04d415af1c.jpg https://telegra.ph/file/323986d3bd9c4c1b3cb26.jpg https://telegra.ph/file/b8a82dcb89fb296f92ca0.jpg https://telegra.ph/file/31adab039a85ed88e22b0.jpg https://telegra.ph/file/c0e0f4c3ed53ac8438f34.jpg https://telegra.ph/file/eede835fb3c37e07c9cee.jpg https://telegra.ph/file/e17d2d068f71a9867d554.jpg https://telegra.ph/file/8fb1ae7d995e8735a7c25.jpg https://telegra.ph/file/8fed19586b4aa019ec215.jpg https://telegra.ph/file/8e6c923abd6139083e1de.jpg https://telegra.ph/file/0049d801d29e83d68b001.jpg')).split()

# Admins, Channels & Users
ADMINS = "1745047302"
CHANNELS = "-1001569496598", "-1001512245325", "-1001753962462"
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = "-1001744938590"
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = "-1001744938590"
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None

# MongoDB information
DATABASE_URI = "mongodb+srv://Zerina:zerinaxbot@cluster0.gbfew.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
DATABASE_NAME = "Zerina"
COLLECTION_NAME = "Telegram_files"

# Command
COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "/")
WARN_DATA_ID = int(environ.get("WARN_DATA_ID", "0"))
WARN_SETTINGS_ID = int(environ.get("WARN_SETTINGS_ID", "0"))

# the maximum number of 'selectable' messages in Telegram
TG_MAX_SELECT_LEN = 100

# Others
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', -1001790957739))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'TeamEvamaria')
P_TTTI_SHOW_OFF = bool((environ.get('P_TTTI_SHOW_OFF', False)))
IMDB = bool((environ.get('IMDB', True)))
SINGLE_BUTTON = bool((environ.get('SINGLE_BUTTON', False)))
CUSTOM_FILE_CAPTION = "🗃 **File Name** <code>[@Cv_Group1].{file_name}</code>\n📂 **File Size** <code>{file_size}</code>"
LONG_IMDB_DESCRIPTION = bool(environ.get("LONG_IMDB_DESCRIPTION", True))
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", 4)
