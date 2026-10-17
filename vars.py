

from os import environ

API_ID = int(environ.get("API_ID", "39992456"))
API_HASH = environ.get("API_HASH", "029cfb9784f4b9f25b55f30db06a271a")
BOT_TOKEN = environ.get("BOT_TOKEN", "8998143459:AAHLs5LaM2QHGgvxWjSjjp2l_wVDnh3tgTs")

# Force Subscribe Configuration
FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "bot_subscription")  # Channel username without @, 
FORCE_SUB_CHANNEL_LINK = environ.get("FORCE_SUB_CHANNEL_LINK", "https://t.me/bot_subscription")  # Channel link

# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", ""))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "")





