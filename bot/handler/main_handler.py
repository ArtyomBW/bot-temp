from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import build_reply_button
from bot.dispetcher import router
from bot.states import SectorState


@router.message(SectorState.language, F.text == __("⬅️ Orqaga"))
@router.message(SectorState.product_menu, F.text == __("⬅️ Orqaga"))
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    texts = [_("🍽 Restoran menyusi"),
             _("📞 Biz bilan aloqa"),
             _("🇺🇿🇬🇧 Til tanlash")]
    markup = build_reply_button(texts, (2, 1))
    await message.answer(_(f"🏠 Asosiy menyu"), reply_markup=markup)
# 🍽☎️🥗🍕🍜⬅️

@router.message(F.text == __("🇺🇿🇬🇧 Til tanlash"))
async def language_handler(message: Message, state: FSMContext):
    texts = [_("🇺🇿 Uzbek"), _("🇬🇧 English"),_("⬅️ Orqaga")]
    markup = build_reply_button(texts, (3, 1))
    await state.set_state(SectorState.language)
    await message.answer(_(f"🇺🇿🇬🇧 Tilni tanglang"), reply_markup=markup)


@router.message(SectorState.language)
async def language_handler(message: Message, state: FSMContext, i18n):
    map_lang = {
        "🇺🇿 Uzbek": "uz",
        "🇬🇧 English": "en",
    }
    code = map_lang.get(message.text)
    await state.update_data({"locale": code})
    i18n.current_locale = code
    texts = [_("🍽 Restoran menyusi"), _("📞 Biz bilan aloqa"), _("🇺🇿🇬🇧🇷🇺 Language")]
    markup = build_reply_button(texts, (2, 1))
    await message.answer(_("🏠 Asosiy menyu"), reply_markup=markup)
    await state.clear()

@router.message(SectorState.movie_menu, F.text == __("⬅️ Back"))
@router.message(F.text == __("🍽 Restoran menyusi"))
async def movies_handler(message: Message, state: FSMContext):
    texts = [_("🍽 Restoran menyusi"),
             _("🥗 Salatlar"),
             _("🍕 Fas-fud"),
             _("⬅️ Orqaga")]
    markup = build_reply_button(texts, (3, 1))
    await state.set_state(SectorState.product_menu)
    await message.answer(_(f"🍽 Restoran menyusi"), reply_markup=markup)