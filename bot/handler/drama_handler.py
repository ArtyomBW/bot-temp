from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.buttons.reply import build_reply_button
from bot.dispetcher import router
from bot.handler.main_handler import SectorState
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

@router.message(SectorState.product_menu, F.text == __("🎭 Drama"))
async def drama_handler(message: Message, state : FSMContext):
    texts = [_("🎬 Forrest Gump"), _("🎬 Titanic"), _("⬅️ Back")]
    markup = build_reply_button(texts, (2,1))
    await state.set_state(SectorState.movie_menu)
    await message.answer(f"🎭 Drama : \nBW", reply_markup=markup)
