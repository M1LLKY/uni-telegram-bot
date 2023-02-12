#Telegram bot, that take info from university site and send it to user.
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)  # put token from config.py into our code

def main():  # main function, that contain most of commands

    @bot.message_handler(commands=["start"])  # start message
    def start_message(message):
        bot.send_message(message.chat.id,"Привет, я универскальный бот помощник! Располагайся поудобнее.")


    @bot.message_handler(commands=["help"])  # main bot menu
    def menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard= True)

        button_1 = types.KeyboardButton("Расписание")
        button_2 = types.KeyboardButton("Домашка")
        button_3 = types.KeyboardButton("Долги")

        markup.add(button_1, button_2, button_3)

        bot.send_message(message.chat.id, "Выбери то, с чем у тебя самые большие проблемы, xDD", reply_markup= markup)

    @bot.message_handler(content_types=["text"])
    def checker(message):
        if message.chat.type == "private":
            if message.text == "Расписание":
                bot.send_message(message.chat.id, "Расписание вообще тупа класс")
            elif message.text == "Домашка":
                bot.send_message(message.chat.id, "ДЗ... Что это такое?")
            elif message.text == "Долги":
                bot.send_message(message.chat.id, "Я - Наруто удзумаки")


    bot.infinity_polling()  # bot running

if __name__ == "__main__":
    main()