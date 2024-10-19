from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, Message
import config
import asyncio
from BABYMUSIC import app
from config import BOT_USERNAME


# Start panel for inline buttons
def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{BOT_USERNAME}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


# Private panel for inline buttons
def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["S_B_5"], user_id=config.CHAT),
            InlineKeyboardButton(text=_["S_B_7"], user_id=config.SOURCE),
        ],
    ]
    return buttons
