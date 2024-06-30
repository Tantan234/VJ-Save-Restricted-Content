import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7499750406:AAFX5jY6lhxGjbxJO2P9FkZBYmUWebBVMpU")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "21844093"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "fe7d41dd4f381b836abdabf1fd87af3a")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://alexandernox701:nrcekYdUWlUStkbp@cluster0.aemadzc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
