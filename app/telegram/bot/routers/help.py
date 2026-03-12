from aiogram import F, Router
from aiogram.filters import Command, StateFilter
from aiogram.types import Message

from app.telegram.bot.keyboards import HELP_BUTTON_TEXT
from app.telegram.bot.states import BotStates
from app.telegram.bot.views import build_help_text

router = Router()


@router.message(
    StateFilter(BotStates.main_menu, BotStates.processing_resume, None),
    F.text == HELP_BUTTON_TEXT,
)
@router.message(
    StateFilter(BotStates.main_menu, BotStates.processing_resume, None),
    Command("help"),
)
async def cmd_help(message: Message) -> None:
    await message.answer(build_help_text())
