class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = "3330416"
    API_HASH = "551d747d492ad11a10054fbf672d16e3"

    CASH_API_KEY = ""  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://djvsjgqv:Ar16KXxOmEUiawIJANe2H6OMMbOyMteM@lallah.db.elephantsql.com/djvsjgqv"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001561812932)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://muhamadfaiz:muhamadfaiz@cluster0.mpwspud.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/04672cf73354dcaade860.jpg"

    SUPPORT_CHAT = "senzusupp"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "5262608425:AAEbUDcE2inIrSqmzdSTTJUDlVHeZF5pJw8"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = ""  # Get this value from https://timezonedb.com/api

    OWNER_ID = 1680004937  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = [1680004937]  # User id of dev users
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
