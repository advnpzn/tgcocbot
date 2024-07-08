from telegram import InlineKeyboardButton
from strings import GITHUB, DEV_USERNAME

START_KEYBOARD = [
    [
        InlineKeyboardButton(text="GitHub", url=GITHUB),
        InlineKeyboardButton(text="Help", callback_data="help"),
        InlineKeyboardButton("Developer", url=DEV_USERNAME),
    ]
]

SETTINGS_KEYBOARD = [
    [
        InlineKeyboardButton("Alerts", callback_data="settings_alert"),
    ]
]

SEARCH_KEYBOARD = [
    [
        InlineKeyboardButton("Clans", callback_data="clans"),
        InlineKeyboardButton("Players", callback_data="players")
    ],
    [
        InlineKeyboardButton("Back", callback_data="back_search")
    ]
]