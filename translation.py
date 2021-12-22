class Translation(object):
    START_TEXT = """Hello!..... 

This is a simple my.telegram.org bot. Enter your Telegram Phone Number, to get the APP-ID & API-HASH from my.telegram.org.

To Restart the Progress for IDs Press /start

Made With ❤ By [@TeleRoidGroup](https://t.me/TeleRoidGroup)"""
    AFTER_RECVD_CODE_TEXT = """Ohh Great !
Now please send the Telegram code that you received from Telegram!

This code is only used for the purpose of getting the APP ID from my.telegram.org.

And There Will Be No Issue With Your Account

/start to re-enter your details"""
    BEFORE_SUCC_LOGIN = "recieved code. Scarpping the web page ..."
    ERRED_PAGE = "something Went Wrong . Failed to get app id & hash. \n\n@TheTeleRoid"
    CANCELLED_MESG = "Khatam ! Please re /start the bot conversation & Re-fill the Data"
    IN_VALID_CODE_PVDED = "Sorry, but the Input does not seem to be a valid Telegram Web-Login code"
    IN_VALID_PHNO_PVDED = "Sorry, but the Input does not seem to be a valid phone number"
