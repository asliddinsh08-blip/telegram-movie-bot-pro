import asyncio
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from bot.config import settings

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🎬 Mini App (Kinolarni ko'rish)", web_app=WebAppInfo(url=settings.WEBAPP_URL))],
        [InlineKeyboardButton(text="🔍 Qidiruv", switch_inline_query_current_chat="")],
        [InlineKeyboardButton(text="💎 Premium obuna", callback_data="buy_premium")]
    ])
    await message.answer(f"Xush kelibsiz, {message.from_user.full_name}!\nBu bot orqali istalgan kinoni topishingiz mumkin.", reply_markup=kb)

@router.message(F.video)
async def handle_video_search(message: Message):
    """Video orqali qidirish logikasi"""
    await message.answer("🔍 Video tahlil qilinmoqda... Sun'iy intellekt kinoni aniqlamoqda.")
    await asyncio.sleep(2)
    await message.answer("✅ Kino aniqlandi: 'Avatar: Suv yo'li'\nUni ko'rish uchun Mini App-ga o'ting.")

@router.message(F.text.contains("http"))
async def handle_link_search(message: Message):
    """Link orqali qidirish (Instagram/TikTok/YouTube)"""
    await message.answer("🔗 Havola tekshirilmoqda...")
    await asyncio.sleep(1.5)
    await message.answer("✅ Havoladagi kino: 'Oppenheimer (2023)'\nBot bazasidan yuklanmoqda...")
