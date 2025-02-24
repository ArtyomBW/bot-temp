from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import build_reply_button
from bot.dispetcher import router
from bot.states import SectorState


@router.message(SectorState.language, F.text == __("⬅️  Back"))
@router.message(SectorState.product_menu, F.text == __("⬅️ Back"))
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    texts = [_("🎥 Movies Section"),
             _("📞 Contact center"),
             _("🇺🇿🇬🇧🇷🇺 Language")]
    markup = build_reply_button(texts, (2, 1))
    await message.answer(_(f"🏠 Main menu: \nBW"), reply_markup=markup)


@router.message(F.text == __("🇺🇿🇬🇧🇷🇺 Language"))
async def language_handler(message: Message, state: FSMContext):
    texts = [_("🇺🇿 Uzbek"), _("🇬🇧 English"), _("🇷🇺 Russia"), _("⬅️  Back")]
    markup = build_reply_button(texts, (3, 1))
    await state.set_state(SectorState.language)
    await message.answer(_(f"Choose language: \nBW"), reply_markup=markup)


@router.message(SectorState.language)
async def language_handler(message: Message, state: FSMContext, i18n):
    map_lang = {
        "🇺🇿 Uzbek": "uz",
        "🇬🇧 English": "en",
        "🇷🇺 Russia": "ru",
    }

    code = map_lang.get(message.text)
    await state.update_data({"locale": code})
    i18n.current_locale = code
    # await state.update_data({"locale": code})
    texts = [_("🎥 Movies Section"), _("📞 Contact center"), _("🇺🇿🇬🇧🇷🇺 Language")]
    markup = build_reply_button(texts, (2, 1))
    await message.answer(_("🏠 Main menu : \nBW"), reply_markup=markup)
    await state.clear()


@router.message(SectorState.movie_menu, F.text == __("⬅️ Back"))
@router.message(F.text == __("🎥 Movies Section"))
async def movies_handler(message: Message, state: FSMContext):
    texts = [_("🎭 Drama"),
             _("😂 Comedy"),
             _("🎬 Action"),
             _("⬅️ Back")]
    markup = build_reply_button(texts, (3, 1))
    await state.set_state(SectorState.product_menu)
    await message.answer(_(f"🎥 Movies section: \nBW"), reply_markup=markup)