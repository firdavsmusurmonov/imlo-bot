import logging
import telebot
import dp
from aiogram import Bot, Dispatcher, executor, types
from checkWords import checkWord
from pytube import YouTube
API_TOKEN = '5386614808:AAHCnIelST9-SUQY95mUO2Tn50U-U_stNHU'

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Imlo botga Hush kelibsiz\n Siz bu bot orqali so'zlarni xatosiz yozasiz")


@dp.message_handler(commands=['help'])
async def help_user(message: types.Message):
    await message.reply("Botdan foydalanish uchun so'z kiriting")

# @dp.message_handler()
# def echo(message):
#     # bot.send_document(message.chat.id , open('main.py' , 'rb'))
#     try:
#         youtube = YouTube(message.text)
#         youtube.streams.first().download(filename="1.mp4")


#         videores = open(message.text+'.mp4')

#         bot.send_video(message.chat.id , videores )
#     except:
#         bot.reply_to(message ,'Xatolik kuzatildi !')
        

@dp.message_handler()
async def checkImlo(message: types.Message):
    # data = [line.strip() for line in open("C:\corpus\TermList.txt", 'r')]
    # # words = [[word for word in data.lower().split()] for word in data]
    # data = [line.strip() for line in open('corpus.txt', 'r')]
    # words = [[word.lower() for word in line.split()] for line in data]
    word = message.text
    result = checkWord(word)
    if result['available']:
        response = f"✅{word.capitalize()}"
    else:
        response = f"❌{word.capitalize()}\n"
        for text in result['matches']:
            response += f"✅{text.capitalize()}\n"
    await message.answer(response)

    # await message.reply("Botdan foydalanish uchun so'z kiriting")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
