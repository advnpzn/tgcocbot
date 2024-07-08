from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import Config
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

cfg = Config()

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    logging.info("Sending hello message.")
    await context.bo
    logging.info("Done :)")

if __name__ == '__main__':
    
    app = ApplicationBuilder().token(cfg.BOT_TOKEN).build()
    app.add_handler(CommandHandler('hello', hello))

    app.run_polling()