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
MENU_CEZAR=7
TEXT_CEZAR=8
KEY_CEZAR=9
ATBASH=10

TOKEN = '2140744898:AAE3VxNEAq1EUuacpQR4Wn13kSCx1bKguzs'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher


# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Привет!Я бот, который поможет тебе зашифровать/расшифровать послания с помощью различных шифров.Напиши /")


def cezarius(update, context):
    global STATE
    STATE = MENU_CEZAR
    update.message.reply_text(
        "Выбран шифр Цезаря.")
    update.message.reply_text(
        "Язык ввода - русский")
    update.message.reply_text(
        "Функции: шифрование, расшифрование")
    update.message.reply_text(
        "Введите Ш чтобы зашифровать сообщение, Р чтобы расшифровать и В чтобы выйти(только русский язык)")


def atbatsha(update,context):
    global STATE
    STATE = ATBASH
    update.message.reply_text(
        "Выбран шифр Атбатша.")
    update.message.reply_text(
        "Язык ввода - английский")
    update.message.reply_text(
        "Функции: шифрование")
    update.message.reply_text(
        "Введите текст:")

def visioner(update, context):
    global STATE
    STATE = LANG
    update.message.reply_text(
        "Выбран шифр Виженера.")
    update.message.reply_text(
        "Язык ввода - английский, русский. Бот предоставит возможность выбора")
    update.message.reply_text(
        "Функции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру")
    update.message.reply_text("Выберите язык.Для сообщения на русском языке команда - русс, а для английского - англ.")


# функция обработки текстовых сообщений
def echo(update, context):
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
    global STATE
    context.user_data['lang'] = update.message.text
    update.message.reply_text("Шифрование или же расшифрование?Команды шифр/расшифр соответственно.")
    STATE = INF


def recieved_inf(update, context):
    global STATE
    inf = update.message.text
    context.user_data['inf'] = inf
    update.message.reply_text("Введите текст:")
    STATE = TXT


def recieved_txt(update, context):
    global STATE
    txt = update.message.text
    context.user_data['txt'] = txt
    update.message.reply_text("Введите ключ шифрования:")
    STATE = KEY


def recieved_key(update, context):
    global STATE
    key = update.message.text
    context.user_data['key'] = key
    update.message.reply_text("По какой гамме шифровать/расшифровать?Команды: повтор(повтор ключа), само (повтор ключа и текста),самш(сложная совокупность ключа и текста):")
    STATE = GAMMA


def recieved_gamma(update, context):
    global STATE
    gamma = update.message.text
    context.user_data['gamma'] = gamma
    update.message.reply_text("Сделать строчными?")
    STATE = STR


def recieved_str(update, context):
    global STATE
    str = update.message.text
    context.user_data['str'] = str
    STATE = None
    vizik(context,update)
    print(context.user_data)

def recieved_menu_cezar(update, context):
    global STATE
    menu_cezar = update.message.text
    context.user_data['menu_cezar'] = menu_cezar
    update.message.reply_text("Введите текст:")
    STATE = TEXT_CEZAR

def recieved_text_cezar(update, context):
    global STATE
    text_cezar = update.message.text
    context.user_data['text_cezar'] = text_cezar
    update.message.reply_text("Введите ключ:")
    STATE=KEY_CEZAR
def recieved_key_cezar(update, context):
    global STATE
    key_cezar = update.message.text
    context.user_data['key_cezar'] = key_cezar
    STATE = None
    cezarik(update,context)

def recieved_atbash(update, context):
    global STATE
    atbash = update.message.text
    context.user_data['atbash'] = atbash
    STATE = None
    atbashh(update,context)
# функция обработки команды '/caps'
def caps(update, context):
    if context.args:
        text_caps = ' '.join(context.args).upper()
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=text_caps)
    else:
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='No command argument')
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='send: /caps argument')


# функция обработки встроенного запроса
def inline_caps(update, context):
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


# функция обработки не распознных команд
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Я не понимаю, что Вы написали.Ознакомьтесь с возможностями бота или повторите попытку.")


# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

visioner_handler = CommandHandler('visioner', visioner)
dispatcher.add_handler(visioner_handler)

cezarius_handler = CommandHandler('cezarius', cezarius)
dispatcher.add_handler(cezarius_handler)

atbatsha_handler = CommandHandler('atbatsha', atbatsha)
dispatcher.add_handler(atbatsha_handler)

# обработчик текстовых сообщений
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
dispatcher.add_handler(echo_handler)

# обработчик команды '/caps'
caps_handler = CommandHandler('caps', caps)
dispatcher.add_handler(caps_handler)

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
