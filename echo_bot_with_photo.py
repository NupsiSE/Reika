from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, ContentType
from aiogram import F

BOT_TOKEN = "5452706659:AAH_hZchULI0cLGd4tZXS5S-P8_Bln2ji0k"

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


async def process_start_command(message: Message):
    await message.answer("Hello!!!")


async def process_help_command(message: Message):
    await message.answer("it's echo-bot 3.0")


async def send_echo(message: Message):
    await message.reply(text=message.text)


async def send_photo_echo(message: Message):
    await message.reply_photo(message.photo[0].file_id)


dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=["help"]))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)
