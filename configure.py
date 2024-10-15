import os

class Config:
    OWNER_ID = 5227327021
    API_ID = int(os.environ.get("API_ID", "9590156"))
    API_HASH = os.environ.get("API_HASH", "368a346bb1b206b650f2b3b37f91e237")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6032731588:AAGenBIMIq94EDeYVaqjNLg-QOiV1TMGoQU")
    DATABASE_URI = os.getenv("mongodb://javamindful:javamindful@cluster0-shard-00-00.zeupx.mongodb.net:27017,cluster0-shard-00-01.zeupx.mongodb.net:27017,cluster0-shard-00-02.zeupx.mongodb.net:27017/myDatabase?ssl=true&replicaSet=atlas-zeupx-shard-0&authSource=admin&retryWrites=true")
    DATABASE_NAME = os.environ.get('DATABASE_NAME', "telebot")
