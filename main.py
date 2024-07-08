from telegram.ext import ApplicationBuilder
from config import config
from handlers import handlers
import logging
        

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handlers(handlers=handlers)

    app.run_polling()