def atbashh(update,context):
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