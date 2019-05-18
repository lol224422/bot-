# -*- coding: utf-8 -*-
import telebot
token ="470893707:AAFIJVzwfDViy6RAmzshrcvOX0MJ2daJh8E"
bot = telebot.TeleBot(token)
import os
import random
from telebot import types
#  bot.send_message(453506802,"test")

#upd = bot.get_updates()
#print(upd)


#last_upd = upd[-1]
#messange_from_user = last_upd.message
#print(messange_from_user)

print(bot.get_me())

def log(message,answer):
    print('\n -----')
    from datetime import datetime
    print(datetime.now())
    print('Сообщение от {0} {1} (id = {2}) \n Текст - {3}'.format(message.from_user.first_name,
        message.from_user.last_name,
        str(message.from_user.id),
        message.text))
    

    print(answer)                                                             



@bot.message_handler(commands = ['start'])
def handle_start(message):
     user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
     user_markup.row('/start','/stop')
     user_markup.row('красивое фото')
     user_markup.row('милфы 😍','трапы 😍',"камшоты 😍",'домашнее 😍')
     bot.send_message(message.chat.id,'прывэтик))',reply_markup=user_markup)

@bot.message_handler(commands = ['stop'])
def handle_start(message):
     hide_markup = telebot.types.ReplyKeyboardRemove()
     bot.send_message(message.chat.id,'пока зайчик))',reply_markup=hide_markup)


@bot.message_handler(commands = ['help'])
def handle_text(message):
     bot.send_message(message.chat.id,'what do you need?')



@bot.message_handler(content_types = ['text'])
def handle_text(message):
    if message.text == 'a':
         answer = 'b'
         log(message,answer)
         bot.send_message(message.chat.id,"b")

    elif message.text == 'b':
         answer = 'v'
         bot.send_message(message.chat.id,"v")
         log(message,answer)

    elif message.text == 'красивое фото':
          directory = 'C:/Users/оператор/Pictures/fotos to bot'
          all_files_in_directory = os.listdir(directory)
          random_file = random.choice(all_files_in_directory)
          img = open(directory + '/' + random_file,'rb')
          bot.send_chat_action(message.from_user.id,'upload_photo')
          bot.send_photo(message.from_user.id, img)
          img.close()

    elif message.text == 'милфы 😍':
          directory = 'C:/Users/оператор/Documents/documents/1'
          all_files_in_directory = os.listdir(directory)
          random_file = random.choice(all_files_in_directory)
          document = open(directory + '/' + random_file,'rb')
          keyboard = types.InlineKeyboardMarkup()
          keyboard.add(*[types.InlineKeyboardButton(text = name,url = 'http://messagu.ru/telegram/telegram-bot-knopki-delaem-robota-v-telegram'
) for name in ['asfasf']])
          bot.send_chat_action(message.from_user.id,'upload_document')
          msg = bot.send_document(message.from_user.id, document,reply_markup=keyboard)
          parse_mod = 'http://messagu.ru/telegram/telegram-bot-knopki-delaem-robota-v-telegram'
          document.close()
          
          

    elif message.text == 'трапы 😍':
          directory = 'C:/Users/оператор/Documents/documents/2'
          all_files_in_directory = os.listdir(directory)
          random_file = random.choice(all_files_in_directory)
          document = open(directory + '/' + random_file,'rb')
          bot.send_chat_action(message.from_user.id,'upload_document')
          bot.send_document(message.from_user.id, document)
          document.close()
          bot.send_message(message.chat.id,'какая-то ссылка') 

    elif message.text == 'камшоты 😍':
          directory = 'C:/Users/оператор/Documents/documents/3'
          all_files_in_directory = os.listdir(directory)
          random_file = random.choice(all_files_in_directory)
          document = open(directory + '/' + random_file,'rb')
          bot.send_chat_action(message.from_user.id,'upload_document')
          bot.send_document(message.from_user.id, document)
          document.close()
          bot.send_message(message.chat.id,'какая-то ссылка')

    elif message.text == 'домашнее 😍':
          directory = 'C:/Users/оператор/Documents/documents/4'
          all_files_in_directory = os.listdir(directory)
          random_file = random.choice(all_files_in_directory)
          document = open(directory + '/' + random_file,'rb')
          bot.send_chat_action(message.from_user.id,'upload_document')
          bot.send_document(message.from_user.id, document)
          document.close()
          bot.send_message(message.chat.id,'какая-то ссылка')    
    else:
         bot.send_message(message.chat.id,"ebanutiy?")
         answer = 'ebanutiy?'
         log(message,answer)

bot.polling(none_stop = True, interval = 0)



