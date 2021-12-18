def atbashh(update,context):
    """

    Шифр Атбаш – простой шифр подстановки для алфавитного письма, в котором каждая n-я буква алфавита заменяется буквой m - n +1, где m - общее число букв в алфавите. Другими словами первая буква заменяется на последнюю, вторая – на предпоследнюю и так далее. Сервис позволяет выполнить шифрование и расшифровку для кириллицы и латиницы.

    """
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']
    s= context.user_data['atbash']
    u = ''
    s = s.lower()
    s = list(str(s))
    for i in range(len(s)):
        if s[i] not in abc:
            u += s[i]
        else:
            e = abc.index(s[i])
            e = 26 - e - 1
            u += abc[e]
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Результат:'+u)