import telebot
from telebot import types
#Макет к команде старт
textstart="Привет,Я твой помощник,Можешь покамись поболтать со мной,пока друзья тебе пишут.😎"
markup=types.ReplyKeyboardMarkup(resize_keyboard=False)
iten1=types.KeyboardButton("Курс доллара💲")
iten2=types.KeyboardButton("Рандомное число🎲")
iten3=types.KeyboardButton("Ну как там новости?")
iten4=types.KeyboardButton("Давайте знакомиться💃🕺")
iten5=types.KeyboardButton("Просто поболтаем😉")
iten6=types.KeyboardButton("Анекдоты😂")


markup.add(iten1,iten2,iten3,iten4,iten5,iten6)

#Макет к команде ''как дела"


markup2=types.InlineKeyboardMarkup(row_width=1)
inten1=types.InlineKeyboardButton("Редактировать свой профиль.😺",callback_data="prov")
inten2=types.InlineKeyboardButton("Знакомится💃🕺",callback_data="zoom")
markup2.add(inten1,inten2)