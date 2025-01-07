from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "5452706659:AAH_hZchULI0cLGd4tZXS5S-P8_Bln2ji0k"

# создаем объекты бота и диспетчера
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


# хэндлер, который срабатывает на команду "старт"
async def process_start_command(message: Message):
    await message.answer("Hello!")


# хэндлер,который срабатывает на команду "help"
async def process_help_command(message: Message):
    await message.answer("i'm echo-bot 2.0!")


# хэндлер, который срабатывает на любые сообщения,
# кроме старт и help
async def send_echo(message: Message):
    await message.reply(text=message.text)


# регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=["help"]))
dp.message.register(send_echo)

if __name__ == "__main__":
    dp.run_polling(bot)
