

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)
import logging
import requests


# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
PINCODE, AGAIN, LOCATION, BIO = range(4)

apiUrl = 'http://127.0.0.1:8000'
def start(update, _):
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Салам бро это бот для Barinsatu, чтобы пользоваться напиши секретный код\nКоманда /cancel, чтобы прекратить разговор'
        )
    return PINCODE


def again(update, _):
    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Ок давай пин код еще раз'
        )
    return PINCODE

# Обрабатываем пол пользователя
def pincode(update, _):
    text = update.message.text



    if text == '020128':
        update.message.reply_text(
        'Хорошо, вы ответили правильно теперь мы можем отправить данные, ждите вестей',
        reply_markup=ReplyKeyboardRemove(),
        )
        res = requests.post(apiUrl+'/api/v1/create-telegram-bot',data={
            "user_name": update.message.chat.username,
            "chat_id": update.message.chat.id
        })
        print(res.content)
    else:
        update.message.reply_text(
        'Оу кажется вы не знаете секретный код заново попробуйте',
        reply_markup=ReplyKeyboardRemove(),
    )




# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater("5478835430:AAEqT3Kw8QKDlTPRzIfSRVYAlBOW2uIxfPQ")
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями GENDER, PHOTO, LOCATION и BIO
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            PINCODE: [MessageHandler(Filters.text, pincode)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()

        # ')')

