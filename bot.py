# sample-bot.py
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler
from telegram.ext import MessageHandler, Filters, InlineQueryHandler

STATE= None
LANG= 1
INF= 2
GAMMA= 3
KEY= 4
TXT= 5
STR= 6

TOKEN = '2140744898:AAE3VxNEAq1EUuacpQR4Wn13kSCx1bKguzs'
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

# функция обработки команды '/start'
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")

def visioner(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=visioner)
def visioner(update,context):
    global STATE
    STATE=LANG
    update.message.reply_text("Выберите язык")
    # alphabet=dict = {chr(ord('а') + i) : chr(ord('А') + i) for i in range(33)}
    alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
                'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
    Alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
                'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
    alphabet1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
    Alphabet1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z']
    symbol = ["'", '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '?', ',', '.', '@', '"', '*', '&', '$', '%',
              '§', '±', '<', '>', ';', ':', '[', ']', '{', '}', '^', '(', ')', '#', '№', '~', '`', ' ', '-']
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Какой язык будем использовать?(команды русс и англ соответственно)')
    y = update.message.text
    if y == 'русс':
        print('Что будем делать?Шифровать или расшифровывать?(команды шифр и расшифр соответсвенно)')
        a = input()
        if a == 'шифр':
            c = 0
            k = 0
            p, b, v, n, m, e = [], [], [], [], [], []
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Введите открытый текст:')
            l = list(update.message.text)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Введите секретный ключ:')
            d = list(update.message.text)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=
                'Какой формат ключа:повторение ключа,самоключ по открытому тексту или самоключ по шифртексту?(соответсвенно команды повтор,само,самш)')
            j = update.message.text
            # короткий лозунг
            if j == 'повтор':
                if len(l) > len(d):
                    while len(l) > len(d):
                        for i in range(len(d)): d.append(d[i])
            # самоключ по открытому тексту:
            if j == 'само':
                l = ''.join(l)
                d = ''.join(d)
                if len(l) > len(d):
                    d = d + l
                d = list(d)
                l = list(l)
            # самоключ по шифртексту:
            if j == 'самш':
                d = d + l
                d = ''.join(d)
                d = [x for x in d if x not in symbol]
                d = d[:len(l)]
                d = ''.join(d)
                d.lower()
                d = list(d)
                for i in range(1, len(d)):
                    if d[i - 1] in alphabet:
                        s = alphabet.index(d[i - 1])
                    else:
                        s = Alphabet.index(d[i - 1])
                    if d[i] in alphabet:
                        x = alphabet.index(d[i])
                    else:
                        x = Alphabet.index(d[i])
                    u = s + x
                    u = u % 33
                    d[i] = alphabet[u]
            for i in range(len(l)):
                if l[i] not in symbol:
                    b.append(l[i])
                else:
                    v.append(i)
                    m.append(l[i])
            d = [x for x in d if x not in symbol]
            d = d[:len(l)]
            for i in range(len(b)):
                if b[i] in alphabet:
                    k = alphabet.index(b[i])
                else:
                    k = Alphabet.index(b[i])
                if d[i] in alphabet:
                    z = alphabet.index(d[i])
                else:
                    z = Alphabet.index(d[i])
                if b[i] in alphabet:
                    p.append(alphabet[(k + z) % 33])
                else:
                    p.append(Alphabet[(k + z) % 33])
            if len(v) != 0:
                for i in range(len(v)): p.insert(v[i], m[i])
            p = ''.join(p)
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Строчными сделать?:(команды да или нет соответсвенно)')
            t = update.message.text
            if t == 'да':
                p = p.lower()
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Результат:')
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Результат:')
                context.bot.send_message(chat_id=update.effective_chat.id,
                                        text=p)
            d = ''.join(d)
            d = d.lower()
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вот гамма(ключ) для расшифроки полученного сообщения-')
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=d)
        if a == 'расшифр':
            c = 0
            p, b, v, n, m = [], [], [], [], []
            print('Введите шифртекст:')
            l = list(input())
            print('Введите секретный ключ:')
            d = list(input())
            print(
                'Какой формат ключа:повторение ключа,самоключ по открытому тексту или самоключ по шифртексту?(соответсвенно команды повтор,само,самш)')
            j = input()
            # короткий лозунг
            if j == 'повтор':
                if len(l) > len(d):
                    while len(l) > len(d):
                        for i in range(len(d)): d.append(d[i])
            # самоключ по открытому тексту:
            if j == 'само': d = d[:len(l)]
            # самоключ по шифртексту:
            if j == 'самш': d = d[:len(l)]
            d = d[:len(l)]
            for i in range(len(l)):
                if l[i] not in symbol:
                    b.append(l[i])
                else:
                    v.append(i)
                    m.append(l[i])
            for i in range(len(b)):
                if b[i] == ' ':
                    p.append(' ')
                else:
                    if b[i] in alphabet:
                        k = alphabet.index(b[i])
                    else:
                        k = Alphabet.index(b[i])
                    if d[i] in alphabet:
                        z = alphabet.index(d[i])
                    else:
                        z = Alphabet.index(d[i])
                    if b[i] in alphabet:
                        p.append(alphabet[(k - z) % 33])
                    else:
                        p.append(Alphabet[(k - z) % 33])
            if len(v) != 0:
                for i in range(len(v)): p.insert(v[i], m[i])
            p = ''.join(p)
            print('Результат:')
            print(p)
    else:
        print('Что будем делать?Шифровать или расшифровывать?(команды шифр и расшифр соответсвенно)')
        a = input()
        if a == 'шифр':
            c = 0
            k = 0
            p, b, v, n, m, e = [], [], [], [], [], []
            print('Введите открытый текст:')
            l = list(input())
            print('Введите секретный ключ:')
            d = list(input())
            print(
                'Какой формат ключа:повторение ключа,самоключ по открытому тексту или самоключ по шифртексту?(соответсвенно команды повтор,само,самш)')
            j = input()
            # короткий лозунг
            if j == 'повтор':
                if len(l) > len(d):
                    while len(l) > len(d):
                        for i in range(len(d)): d.append(d[i])
            # самоключ по открытому тексту:
            if j == 'само':
                l = ''.join(l)
                d = ''.join(d)
                if len(l) > len(d):
                    d = d + l
                d = list(d)
                l = list(l)
            # самоключ по шифртексту:
            if j == 'самш':
                d = d + l
                d = ''.join(d)
                d = [x for x in d if x not in symbol]
                d = d[:len(l)]
                d = ''.join(d)
                d.lower()
                d = list(d)
                for i in range(1, len(d)):
                    if d[i - 1] in alphabet1:
                        s = alphabet1.index(d[i - 1])
                    else:
                        s = Alphabet1.index(d[i - 1])
                    if d[i] in alphabet1:
                        x = alphabet1.index(d[i])
                    else:
                        x = Alphabet1.index(d[i])
                    u = s + x
                    u = u % 26
                    d[i] = alphabet1[u]
            for i in range(len(l)):
                if l[i] not in symbol:
                    b.append(l[i])
                else:
                    v.append(i)
                    m.append(l[i])
            d = [x for x in d if x not in symbol]
            d = d[:len(l)]
            for i in range(len(b)):
                if b[i] in alphabet1:
                    k = alphabet1.index(b[i])
                else:
                    k = Alphabet1.index(b[i])
                if d[i] in alphabet1:
                    z = alphabet1.index(d[i])
                else:
                    z = Alphabet1.index(d[i])
                if b[i] in alphabet1:
                    p.append(alphabet1[(k + z) % 26])
                else:
                    p.append(Alphabet1[(k + z) % 26])
            if len(v) != 0:
                for i in range(len(v)): p.insert(v[i], m[i])
            p = ''.join(p)
            print('Строчными сделать?:(команды да или нет соответсвенно)')
            t = input()
            if t == 'да':
                p = p.lower()
                print('Результат:')
            else:
                print('Результат:')
            print(p)
            d = ''.join(d)
            d = d.lower()
            print('Вот гамма(ключ) для расшифроки полученного сообщения-', d)
        if a == 'расшифр':
            c = 0
            p, b, v, n, m = [], [], [], [], []
            print('Введите шифртекст:')
            l = list(input())
            print('Введите секретный ключ:')
            d = list(input())
            print(
                'Какой формат ключа:повторение ключа,самоключ по открытому тексту или самоключ по шифртексту?(соответсвенно комнады повтор,само,самш)')
            j = input()
            # короткий лозунг
            if j == 'повтор':
                if len(l) > len(d):
                    while len(l) > len(d):
                        for i in range(len(d)): d.append(d[i])
            # самоключ по открытому тексту:
            if j == 'само':
                d = d[:len(l)]
            # самоключ по шифртексту:
            if j == 'самш': d = d[:len(l)]
            d = d[:len(l)]
            for i in range(len(l)):
                if l[i] not in symbol:
                    b.append(l[i])
                else:
                    v.append(i)
                    m.append(l[i])
            for i in range(len(b)):
                if b[i] == ' ':
                    p.append(' ')
                else:
                    if b[i] in alphabet1:
                        k = alphabet1.index(b[i])
                    else:
                        k = Alphabet1.index(b[i])
                    if d[i] in alphabet1:
                        z = alphabet1.index(d[i])
                    else:
                        z = Alphabet1.index(d[i])
                    if b[i] in alphabet1:
                        p.append(alphabet1[(k - z) % 26])
                    else:
                        p.append(Alphabet1[(k - z) % 26])
            if len(v) != 0:
                for i in range(len(v)): p.insert(v[i], m[i])
            p = ''.join(p)
            print('Результат:')
            print(p)
# функция обработки текстовых сообщений
def echo(update, context):
    global STATE
    if STATE==LANG:
        return recieved_lang(update, context)
    if STATE==INF:
        return recieved_inf(update, context)
    if STATE==GAMMA:
        return recieved_gamma(update, context)
    if STATE==KEY:
        return recieved_key(update, context)
    if STATE==TXT:
        return recieved_txt(update, context)
    if STATE==STR:
        return recieved_str(update, context)

def recieved_lang(update, context):
    global STATE
    lang=update.message.text
    update.message.reply_text("шифр/расшифр?")
    STATE=INF
def recieved_inf(update, context):
    global STATE
    lang=update.message.text
    update.message.reply_text("открытый ключ")
    STATE=TXT
def recieved_txt(update, context):
    global STATE
    lang=update.message.text
    update.message.reply_text("сикрет кей")
    STATE=KEY
def recieved_key(update, context):
    global STATE
    lang=update.message.text
    update.message.reply_text("гамма")
    STATE=GAMMA
def recieved_gamma(update, context):
    global STATE
    lang=update.message.text
    update.message.reply_text("строчными")
    STATE=STR
def recieved_str(update, context):
    global STATE
    lang=update.message.text
    STATE=None
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
                             text="Sorry, I didn't understand that command.")

# обработчик команды '/start'
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

visioner_handler = CommandHandler('visioner', visioner)
dispatcher.add_handler(visioner_handler)

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