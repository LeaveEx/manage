class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "29651673"
    API_HASH = "51bde64a6630fb11d459b1cb41781fd2"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://wsphktgr:MejtrepyRRzVMeHiOyfTpgm8ks0f2yAb@lallah.db.elephantsql.com/wsphktgr"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001928120860)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://anjfaiz2:anjfaiz2@cluster0.k2rtvad.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/6fbdb2f77c4ec8898994e.jpg"

    SUPPORT_CHAT = "senzusupp"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5907159775:AAHCaXpstMbJPxCLuu75gIBoXqX5_cF7nR0"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1221971774  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = [1221971774]  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
