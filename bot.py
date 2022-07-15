
import telebot
import config 
from telebot import types
import random
import  maket
import money
import users
import sqlite3 as sq

bot=telebot.TeleBot("5255982616:AAFrdnpqLK2tUXyWXv4AROj_C4ZAKboc0E4")
priv=["Привет","Как дела?","Что делаешь","Как здоровье?","Что сегодня кушал?","хахаха","Нууу...","Ты отличный собеседник)"]
id_box=[]
with sq.connect("users.db") as con:
        cur=con.cursor()
        
        for i in cur.execute("SELECT * FROM users"):
            id_box.append((i[0]))
  
  
@bot.message_handler(commands=["start"])
def start(message):
    global id_box
    id=message.chat.id
    print(id)
    
    markup=maket.markup
    bot.send_message(message.chat.id,"Добро пожаловать,{0.first_name}!Я-{1.first_name},буду с тобой дружить".format(message.from_user,bot.get_me()),reply_markup=markup)
    if int(message.chat.id) in id_box:
           
            bot.send_message(message.chat.id,"Вы успешно авторизовались.")
    else:
            users.id(int(message.chat.id))
            bot.send_message(message.chat.id,"Успешная регистрация .")
            
 
   
 
    
    
    
@bot.message_handler(content_types=["text"])

def lalala(message):
    global id_box
    
    if message.chat.type=="private":
        if message.text=="Рандомное число🎲":
            bot.send_message(message.chat.id,str(random.randint(0,100)))
        elif message.text=="Курс доллара💲":
               bot.send_message(message.chat.id,str(money.dolar()))
        elif message.text=="Просто поболтаем😉":
            for i in priv:
                bot.send_message(message.chat.id,i)
        elif  message.text=="Давайте знакомиться💃🕺":
            if len(id_box) <=10:
                for i in id_box:
                    bot.send_message(message.chat.id,str("tg://user?id="+str(i)))
            else:
                for i in range(10):
                    u=random(0,len(id_box)-1)
                    t=id_box[u]
                    bot.send_message(message.chat.id,str("tg://user?id="+str(t)))
                    
            
                    
        elif message.text=="Анекдоты😂":
            an=money.anecdot()
            th=0
            for i in range(5):
                bot.send_message(message.chat.id,str(an[th]))
                th+=1
        elif message.text=="Ну как там новости?":
            f=money.nowos()
            s=f[:20]
            f=s
          
            for i in f:
     
                bot.send_message(message.chat.id,i)
        
            
bot.polling(none_stop=True)







































