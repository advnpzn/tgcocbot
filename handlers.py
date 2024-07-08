from telegram.ext import CommandHandler, CallbackQueryHandler, ContextTypes
from telegram import Update, InlineKeyboardMarkup, constants

from strings import WELCOME, HELP
from keyboard import START_KEYBOARD, SEARCH_KEYBOARD, SETTINGS_KEYBOARD
import coc
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
    coc_client = await coc.Client(base_url=config.PROXY).login_with_tokens(config.API_KEY)
    reply_markup = InlineKeyboardMarkup(SEARCH_KEYBOARD)
    update.message.reply_text("Please select what you want to search", reply_markup=reply_markup)


async def search_clans(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) > 0:
        async with coc.Client(base_url=config.PROXY) as coc_client:
            await coc_client.login_with_tokens(config.API_KEY)
            clans = await coc_client.search_clans(name=" ".join(args))

            if len(clans) < 1:
                update.message.reply_text("Could not find any clans with that following name.")
            else:
                c = ""
                for clan in clans:
                    c = c + f"{clan.name}\n"

                await update.message.reply_text(text=c)
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