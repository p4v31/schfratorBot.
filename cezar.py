def cezarik(update,context):
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    t=0
    while t==0:
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
        t+=1
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text='Результат:'+n)