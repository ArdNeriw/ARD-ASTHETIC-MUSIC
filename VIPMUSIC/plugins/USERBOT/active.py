from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from VIPMUSIC.utils.database import get_active_chats, get_active_video_chats


@Client.on_message(filters.command(["ac", "activevc", "activevoice"], prefixes=["."]))
async def start(client: Client, message: Message):
    ac_audio = str(len(await get_active_chats()))
    ac_video = str(len(await get_active_video_chats()))
    await message.reply_text(
        f"✫ <b><u>ᴀᴄᴛɪᴠᴇ ᴄʜᴀᴛs ɪɴғᴏ</u></b> :\n\nᴠᴏɪᴄᴇ : {ac_audio}\nᴠɪᴅᴇᴏ  : {ac_video}",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("𓏲𝄢 ᴄʟᴏsᴇ 𓏲𝄢", callback_data=f"close")]]
        ),
    )
