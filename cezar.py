def cezarik(update, context):
    """

    Шифр Цезаря, также известный как шифр сдвига, код Цезаря или сдвиг Цезаря — один из самых простых и наиболее широко известных методов шифрования.

    Шифр Цезаря — это вид шифра подстановки, в котором каждый символ в открытом тексте заменяется символом, находящимся на некотором постоянном числе позиций левее или правее него в алфавите. Например, в шифре со сдвигом вправо на 3, А была бы заменена на Г, Б станет Д, и так далее.

    """
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    t = 0
    while t == 0:
        main = context.user_data['menu_cezar'].lower()
        if main == 'в':
            break
        elif not (main == 'ш' or main == 'р'):
            continue
        n = ''
        message = context.user_data['text_cezar'].lower()
        key = int(context.user_data['key_cezar'])
        if main == 'р':
            key *= -1
        for letter in message:
            if letter in alphabet:
                t = alphabet.find(letter)
                new_key = (t + key) % len(alphabet)
                n += alphabet[new_key]
            else:
                n += letter
        t += 1
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Результат:' + n)
