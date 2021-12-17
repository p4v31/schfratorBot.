from atbatsha import atbashh
from telethon import TelegramClient, sync, events
from telethon.tl.functions.channels import GetMessagesRequest
import unittest
import time

# Your API ID, hash and session string here
api_id = int('')
api_hash = ""
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
    def testVisionerSCHrusPOVstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'абоба')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мак')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'повтор')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:мбщна'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHrusPOVstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мбщна')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мак')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'повтор')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:абоба'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHengPOVstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'aboba')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mac')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'повтор')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:mbqna'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHengPOVstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mbqna')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mac')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'повтор')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:aboba'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHrusSAMOstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'абоба')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мак')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:мбщбб'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHrusSAMOstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мбщбб')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'макаб')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:абоба'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHengSAMOstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'aboba')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mac')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:mbqbb'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHengSAMOstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mbqbb')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'macab')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:aboba'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHrusSAMOstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'абоба')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мак')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'самш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:мнёшш'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHrusSAMSHstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мнёшш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'ммччш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'самш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:абоба'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHengSAMSHstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'aboba')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mac')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'самш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:mncpp'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHengSAMOstr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mncpp')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mmoop')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:aboba'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHrusPOVnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'абоБа')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мак')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'повтор')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:мбщНа'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHrusPOVnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мбщНа')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мак')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'повтор')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:абоБа'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHengPOVnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'aboBa')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mac')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'повтор')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:mbqNa'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHengPOVnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mbqNa')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mac')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'повтор')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'да')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:aboBa'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHrusSAMOnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'абоБа')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мак')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:мбщБб'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHrusSAMOnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мбщБб')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'макаб')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:абоБа'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHengSAMOnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'aboBa')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mac')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:mbqBb'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHengSAMOnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mbqBb')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'macab')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'само')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:aboBa'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHrusSAMOnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'абоБа')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мак')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'самш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:мнёШш'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerRASHrusSAMSHnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'русс')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'расшифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'мнёШш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'ммччш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'самш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:абоБа'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
    def testVisionerSCHengSAMSHnostr(self):
        try:
            client.send_message('@schfratorBot', '/visioner')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Выбран шифр Виженера\n\nЯзык ввода - английский, русский\n\nБот предоставит возможность выбора\n\nФункции: шифрование, расшифрование, выбор гаммы, приведение к одному регистру\n\nВыберите язык.Для сообщения на русском языке команда - русс, а для английского - англ'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'англ')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Шифрование или расшифрование.Команды шифр или расшифр соответственно?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'шифр')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите текст:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'aboBa')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Введите ключ шифрования:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'mac')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'По какой гамме производить операции: повтор,само,самш:'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'самш')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Сделать строчными?'
            self.assertRegex(m, text)
            client.send_message('@schfratorBot', 'нет')
            time.sleep(2)
            messages = client.get_messages('@schfratorBot')
            for message in client.get_messages('@schfratorBot', limit=1):
                m = message.message
            self.assertEqual(len(messages), 1)
            text = 'Результат:mncPp'
            self.assertRegex(m, text)
        except:
            self.assertFalse(True)
