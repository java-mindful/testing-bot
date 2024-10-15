import os

API_ID = int(os.environ.get("API_ID", "9590156"))
API_HASH = os.environ.get("API_HASH", "368a346bb1b206b650f2b3b37f91e237")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6032731588:AAGenBIMIq94EDeYVaqjNLg-QOiV1TMGoQU")
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002265568616"))
AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())
DB_URL = os.environ.get("DB_URL", "mongodb://javamindful:javamindful@cluster0-shard-00-00.zeupx.mongodb.net:27017/myDatabase?ssl=true&replicaSet=atlas-zeupx-shard-0&authSource=admin&retryWrites=true")
DB_NAME = os.environ.get("DB_NAME", "BroadcastBot")
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
