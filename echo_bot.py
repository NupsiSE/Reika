from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command

BOT_TOKEN = "5452706659:AAH_hZchULI0cLGd4tZXS5S-P8_Bln2ji0k"

# создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# хэндлер, который срабатывает на команду "старт"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer("Hello!")


# хэндлер,который срабатывает на команду "help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer("i'm echo-bot!")


# хэндлер, который срабатывает на любые сообщения,
# кроме старт и help
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)


if __name__ == "__main__":
    dp.run_polling(bot)
