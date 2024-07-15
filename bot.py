import logging

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
import random

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

daywishing = ['Приятного дня!', 'Хорошей погоды!', 'Внезапных денег!']
dayweather = ['На улице рейн, на душе пейн', 'Тучки, тучки, тучки', 'Солнце на весь день']


async def startDialog(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None: #StartButton
    await update.message.reply_text('Привет! Введи команду:\n'
                                    'Пожелание на день - /wish\n'
                                    'Прогноз погоды - /weather\n'
                                    'Удачное число дня - /number\n')


async def dayWish(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(random.choice(daywishing))


async def dayWeather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(random.choice(dayweather))


async def dayNumber(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(random.randint(1,9))


async def errorDay(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Я не понимаю.\n'
                                    'Попробуй ввести одну из команд:\n'
                                    'Пожелание на день - /wish\n'
                                    'Прогноз погоды - /weather\n'
                                    'Удачное число дня - /number\n')


def main() -> None:
    application = Application.builder().token("7385961287:AAEss6WrzDJbx0UM_VKKpoNtbzsQnY0rGQ8").build()
    application.add_handler(CommandHandler('start', startDialog))
    application.add_handler(CommandHandler('wish', dayWish))
    application.add_handler(CommandHandler('weather', dayWeather))
    application.add_handler(CommandHandler('number', dayNumber))
    application.add_handler(MessageHandler(filters.TEXT or filters.COMMAND, errorDay))
    #application.add_handler(CommandHandler(exit))

    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()