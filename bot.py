# sample-bot.py
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler
from visioner import vizik
from cezar import cezarik
from atbatsha import atbashh

STATE = None
LANG = 1
INF = 2
GAMMA = 3
KEY = 4
TXT = 5
STR = 6
MENU_CEZAR = 7
TEXT_CEZAR = 8
KEY_CEZAR = 9
ATBASH = 10

TOKEN = '2140744898:AAE3VxNEAq1EUuacpQR4Wn13kSCx1bKguzs'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


# функция обработки команды '/start'
def start(update, context):
    """

    Главная функция, которая запускается при старте бота

    """
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет!Я бот, который поможет тебе зашифровать/расшифровать послания с помощью различных шифров.Напиши /")


def cezarius(update, context):
    """

    Функция, отвечающая за шифр Цезаря

    """
    global STATE
    STATE = MENU_CEZAR
    update.message.reply_text(
        "Выбран шифр Цезаря\n\nЯзык ввода - русский\n\nФункции: шифрование, расшифрование\n\nВведите Ш чтобы зашифровать сообщение, Р чтобы расшифровать")


def atbatsha(update, context):
    """

    Функция, отвечающая за шифр Атбатша

    """
    global STATE
    STATE = ATBASH
    update.message.reply_text(
        "Выбран шифр Атбатша\n\nЯзык ввода - английский\n\nФункции: шифрование\n\nВведите текст:")


def visioner(update, context):
    """

    Функция, отвечающая за шифр Виженера

    """
    global STATE
    STATE = LANG
    update.message.reply_text(
        "Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ")


# функция обработки текстовых сообщений
def echo(update, context):
    """

    Функция, которая записывает сообщения в переменные

    """
    global STATE
    if STATE == LANG:
        return recieved_lang(update, context)
    if STATE == INF:
        return recieved_inf(update, context)
    if STATE == GAMMA:
        return recieved_gamma(update, context)
    if STATE == KEY:
        return recieved_key(update, context)
    if STATE == TXT:
        return recieved_txt(update, context)
    if STATE == STR:
        return recieved_str(update, context)
    if STATE == MENU_CEZAR:
        return recieved_menu_cezar(update, context)
    if STATE == TEXT_CEZAR:
        return recieved_text_cezar(update, context)
    if STATE == KEY_CEZAR:
        return recieved_key_cezar(update, context)
    if STATE == ATBASH:
        return recieved_atbash(update, context)


def recieved_lang(update, context):
    """

    Функция, принимающая язык на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    context.user_data['lang'] = update.message.text
    update.message.reply_text("Шифрование или расшифрование.Команды шифр или расшифр соответственно?")
    STATE = INF


def recieved_inf(update, context):
    """

    Функция, принимающая язык на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    inf = update.message.text
    context.user_data['inf'] = inf
    update.message.reply_text("Введите текст:")
    STATE = TXT


def recieved_txt(update, context):
    """

    Функция, принимающая ключ шифрования на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    txt = update.message.text
    context.user_data['txt'] = txt
    update.message.reply_text("Введите ключ шифрования:")
    STATE = KEY


def recieved_key(update, context):
    """

    Функция, принимающая гамму на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    key = update.message.text
    context.user_data['key'] = key
    update.message.reply_text("По какой гамме производить операции: повтор,само,самш:")
    STATE = GAMMA


def recieved_gamma(update, context):
    """

    Функция, принимающая да или нет на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    gamma = update.message.text
    context.user_data['gamma'] = gamma
    update.message.reply_text("Сделать строчными?")
    STATE = STR


def recieved_str(update, context):
    """

    Функция, принимающая текст на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    str = update.message.text
    context.user_data['str'] = str
    STATE = None
    vizik(context, update)
    print(context.user_data)


def recieved_menu_cezar(update, context):
    """

    Функция, принимающая Ш или Д на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    menu_cezar = update.message.text
    context.user_data['menu_cezar'] = menu_cezar
    update.message.reply_text("Введите текст:")
    STATE = TEXT_CEZAR


def recieved_text_cezar(update, context):
    """

    Функция, принимающая текст на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    text_cezar = update.message.text
    context.user_data['text_cezar'] = text_cezar
    update.message.reply_text("Введите ключ:")
    STATE = KEY_CEZAR


def recieved_key_cezar(update, context):
    """

    Функция, принимающая ключ на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    key_cezar = update.message.text
    context.user_data['key_cezar'] = key_cezar
    STATE = None
    cezarik(update, context)


def recieved_atbash(update, context):
    """

    Функция, принимающая текст на вход. Срабатывает когда global равен определенному состоянию.

    """
    global STATE
    atbash = update.message.text
    context.user_data['atbash'] = atbash
    STATE = None
    atbashh(update, context)


def inline_caps(update, context):
    """
    Функция обработки встроенного запроса

    """
    query = update.inline_query.query
    if not query:
        return
    results = list()
    results.append(
        InlineQueryResultArticle(
            id=query.upper(),
            title='Convert to UPPER TEXT',
            input_message_content=InputTextMessageContent(query.upper())
        )
    )
    context.bot.answer_inline_query(update.inline_query.id, results)


def unknown(update, context):
    """

    Функция обработки не распознных команд

    """
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Я не понимаю, что Вы написали.Ознакомьтесь с возможностями бота или повторите попытку.")


# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# обработчик команды '/visioner'
visioner_handler = CommandHandler('visioner', visioner)
dispatcher.add_handler(visioner_handler)

# обработчик команды '/cezarius'
cezarius_handler = CommandHandler('cezarius', cezarius)
dispatcher.add_handler(cezarius_handler)

# обработчик команды '/atbasha'
atbatsha_handler = CommandHandler('atbatsha', atbatsha)
dispatcher.add_handler(atbatsha_handler)

# обработчик текстовых сообщений
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# обработчик встроенных запросов
inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)

# обработчик не распознных команд
unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)

# запуск прослушивания сообщений
updater.start_polling()
# обработчик нажатия Ctrl+C
updater.idle()
