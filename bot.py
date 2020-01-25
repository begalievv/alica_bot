from telebot import types
import telebot
import time
# from apscheduler.scheduler import BlockingScheduler
from datetime import datetime





def main():
    bot = telebot.TeleBot("1002018915:AAGULsOoo8ks-6AiW3dphFN8OjcUftMcCm0")

    didyoudo = ''
    willyoudo = ''
    problems = ""
    

    
    @bot.message_handler(content_types=['text'])
    def start(message):
        if message.text == '/start':
            bot.send_message(message.from_user.id, "Что вы сделали?")
            bot.register_next_step_handler(message, get_didyoudo); 
        else:
            bot.send_message(message.from_user.id, 'Напиши /start')
            
    def get_didyoudo(message):
        didyoudo = message.text
        bot.send_message(message.from_user.id, 'Что вы будете делать?')
        bot.register_next_step_handler(message, get_willyoudo)
        chatId = "-320639196"
        if message.from_user.username != None:
            otchet = f"{message.from_user.username} сделал {didyoudo}"
        elif message.from_user.first_name != None:
            otchet = f"{message.from_user.first_name} сделал {didyoudo}"
        elif message.from_user.last_name != None:
            otchet = f"{message.from_user.last_name} сделал {didyoudo}"
        bot.send_message(chatId, otchet)
        


    def get_willyoudo(message):
        global willyoudo
        willyoudo = message.text
        bot.send_message(message.from_user.id, 'Какие сложности?')
        bot.register_next_step_handler(message, get_problems)
        chatId = "-320639196"
        if message.from_user.username != None:
            otchet = f"{message.from_user.username} сделает {willyoudo}"
        elif message.from_user.first_name != None:
            otchet = f"{message.from_user.first_name} сделает {willyoudo}"
        elif message.from_user.last_name != None:
            otchet = f"{message.from_user.last_name} сделает {willyoudo}"
        bot.send_message(chatId, otchet)
        


    def get_problems(message):
        global problems

        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text="Повторить", callback_data="yes")
        keyboard.add(key_yes)
        # keyboard = types.InlineKeyboardMarkup()
        key_no = types.InlineKeyboardButton(text="Выйти", callback_data="no")
        keyboard.add(key_no)
        problems = message.text
        bot.send_message(message.from_user.id, 'Спасибо что написали отчет ', reply_markup=keyboard)

        chatId = "-320639196"
        if message.from_user.username != None:
            otchet = f"У {message.from_user.username} сложности с {problems}"
        elif message.from_user.first_name != None:
            otchet = f"У {message.from_user.first_name} сложности с {problems}"
        elif message.from_user.last_name != None:
            otchet = f"У {message.from_user.last_name} сложности с {problems}"
        bot.send_message(chatId, otchet)

        

        @bot.callback_query_handler(func=lambda call: True)
        def callback_worker(call):
            if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
                 #код сохранения данных, или их обработки
                bot.send_message(call.message.chat.id, 'напишите /start')
            elif call.data == "no":
                bot.send_message(call.message.chat.id, 'пока : )')

        



    bot.polling()



if __name__ == "__main__":
    main()
