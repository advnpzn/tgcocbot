from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes
from telegram import Update, InlineKeyboardMarkup, constants

from strings import WELCOME, HELP
from keyboard import START_KEYBOARD, SEARCH_KEYBOARD, SETTINGS_KEYBOARD
from coc import Clan, Client
from config import config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    reply_markup = InlineKeyboardMarkup(inline_keyboard=START_KEYBOARD)

    await update.message.reply_text(
        text=WELCOME.format(update.effective_chat.first_name), 
        parse_mode=constants.ParseMode.HTML,
        reply_markup=reply_markup
    )


async def help(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    if not update.callback_query:
        await update.message.reply_text(text=HELP)
    else:
        await update.callback_query.edit_message_text(text=HELP)


async def search(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    coc_client: Client = await Client(base_url=config.PROXY).login_with_tokens(config.API_KEY)
    reply_markup = InlineKeyboardMarkup(SEARCH_KEYBOARD)
    update.message.reply_text("Please select what you do you want to search", reply_markup=reply_markup)


async def search_clans(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) > 0:
        coc_client: Client = await Client(base_url=config.PROXY).login_with_tokens(config.API_KEY)
        clans = await coc_client.search_clans("".join(args))
        for clan in clans:
            await update.message.reply_text(text=clan.name)
        
    else:
        await update.message.reply_text(text="Please enter a clan name!")

commands = {
    "start": start,
    "help": help,
    "search": search_clans
}

callbacks = {
    "help": help
}



handlers = []
for cmd, callback in commands.items():
    handlers.append(CommandHandler(command=cmd, callback=callback))
for pattern, callback in callbacks.items():
    handlers.append(CallbackQueryHandler(callback, pattern=pattern))