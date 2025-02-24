from aiogram.fsm.state import StatesGroup, State


class SectorState(StatesGroup):
    product_menu = State()
    movie_menu = State()
    language = State()