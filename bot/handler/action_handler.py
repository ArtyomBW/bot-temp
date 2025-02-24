from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InputMediaPhoto, InputMediaVideo
from aiogram.utils.i18n import gettext as _
from aiogram.utils.i18n import lazy_gettext as __

from bot.buttons.reply import build_reply_button
from bot.dispetcher import router
from bot.handler.main_handler import SectorState
from db.model import Genre, Movie

actions_films = Genre(id=1, name="Action")

batman_movie = Movie(
    id=1,
    name="The Batman",
    genre_id=1,
    description="A dark kinght crime in Gotham City.",
    image="AgACAgIAAxkBAAJ0fGex-Qk95FNCM8a1tH9CEJxXVLaBAAK78jEbRLeRScxXD5UkkEibAQADAgADeQADNgQ",
    file_id="BAACAgIAAxkBAAJ1Umex_5spK3ARkkGzFwgai53atcKEAAKyaAACRLeRSesSKTVE-GAENgQ"
)

movies = [batman_movie]

pinguin_movie = Movie(
    id=2,
    name="The Penguin",
    genre_id=1,
    description="A gritty crime thriller following the Penguin's rise in Gotham's underworld.",
    image="AgACAgIAAxkBAAJ9dWe3jLiYSXhsWH1fuRa8k7-p23ZCAAIs8DEbVkS4ScnRb1JNqUBnAQADAgADeAADNgQ",
    file_id="BAACAgIAAxkBAAJ9eWe3jkX_dFjokDc6z9qI3hlJYrBrAAJ7bgACVkS4SfYOJHKrl1zSNgQ"
)

@router.message(SectorState.product_menu, F.text == __("🎬 Action"))
async def action_handler(message: Message, state: FSMContext):
    texts = [_("🎬 Batman"), _("🎬 Penguin"), _("⬅️ Back")]
    markup = build_reply_button(texts, (2, 1))
    await state.set_state(SectorState.movie_menu)
    await message.answer(_("🎬 Action: \nBW"), reply_markup=markup)



@router.message(F.text == __("🎬 Batman"))
async def batman_action_handler(message: Message):
    media = [
        InputMediaPhoto(media=batman_movie.image, caption=f"🎬 {batman_movie.name}\n\n{batman_movie.description}"),
        InputMediaVideo(media=batman_movie.file_id)
    ]
    await message.answer_media_group(media)



@router.message(F.text == __("🎬 Penguin"))
async def penguin_action_handler(message: Message):
    media = [
        InputMediaPhoto(media=pinguin_movie.image, caption=f"🎬 {pinguin_movie.name}\n\n{pinguin_movie.description}"),
        InputMediaVideo(media=pinguin_movie.file_id)
    ]
    await message.answer_media_group(media)



