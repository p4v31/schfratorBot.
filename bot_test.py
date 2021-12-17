from atbatsha import atbashh
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time

# Your API ID, hash and session string here
api_id = int('9792884')
api_hash = "2b8ec72ad74cf0e3298180809246539c"
client = TelegramClient('session_name', api_id, api_hash)

client.start()

class TG_test(unittest.TestCase):
    def testStart(self):
        try:
            client.send_message('@schfratorBot', '/start')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Привет!Я бот, который поможет тебе зашифровать/расшифровать послания с помощью различных шифров.Напиши /'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testAtbasha(self):
        try:
            client.send_message('@schfratorBot', '/atbatsha')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Атбатша\n\nЯзык ввода - английский\n\nФункции: шифрование\n\nВведите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'abc')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:zyx'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testCezarSchifrator(self):
        try:
            client.send_message('@schfratorBot', '/cezarius')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Цезаря\n\nЯзык ввода - русский\n\nФункции: шифрование, расшифрование\n\nВведите Ш чтобы зашифровать сообщение, Р чтобы расшифровать'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'Ш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'абоба34')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', '5')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:еёуёе34'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testCezarRashifrator(self):
        try:
            client.send_message('@schfratorBot', '/cezarius')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Цезаря\n\nЯзык ввода - русский\n\nФункции: шифрование, расшифрование\n\nВведите Ш чтобы зашифровать сообщение, Р чтобы расшифровать'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'Р')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'еёуёе34')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', '5')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:абоба34'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
'''    def testrVisioner(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(1)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)

            client.send_message('@schfratorBot', 'англ')
            time.sleep(1)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = "Шифрование или же расшифрование?Команды шифр или расшифр соответственно"
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)'''