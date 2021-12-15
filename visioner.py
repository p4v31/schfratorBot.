def vizik(context,update):
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
    y = context.user_data['lang']
    if y == 'русс':
        a = context.user_data['inf']
        if a == 'шифр':
            c = 0
            k = 0
            p, b, v, n, m, e = [], [], [], [], [], []
            l = list(context.user_data['txt'])
            d = list(context.user_data['key'])
            j = context.user_data['gamma']
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

            t = context.user_data['str']
            if t == 'да':
                p = p.lower()
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Результат:')
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=p)
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
            l = list(context.user_data['txt'])
            d = list(context.user_data['key'])
            j = context.user_data['gamma']
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
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Результат:')
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=p)

    else:
        a = context.user_data['inf']
        if a == 'шифр':
            c = 0
            k = 0
            p, b, v, n, m, e = [], [], [], [], [], []
            l = list(context.user_data['txt'])
            d = list(context.user_data['key'])
            j = context.user_data['gamma']
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
            t = context.user_data['str']
            if t == 'да':
                p = p.lower()
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Результат:')
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=p)
            else:
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text='Результат:')
                context.bot.send_message(chat_id=update.effective_chat.id,
                                         text=p)
            d = ''.join(d)
            d = d.lower()
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Вот гамма(ключ) для расшифроки полученного сообщения:')
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=d)
        if a == 'расшифр':
            c = 0
            p, b, v, n, m = [], [], [], [], []
            l = list(context.user_data['txt'])
            d = list(context.user_data['key'])
            j = context.user_data['gamma']
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
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text='Результат:')
            context.bot.send_message(chat_id=update.effective_chat.id,
                                     text=p)
