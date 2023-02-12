#Telegram bot, that take info from university site and send it to user.
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)  # put token from config.py into our code

AI_list = ["abpba", "odwkoa", "ijadwi"]

def back(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("Расписание")
    button_2 = types.KeyboardButton("Домашка")
    button_3 = types.KeyboardButton("Долги")
    markup.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id, "Выбери то, с чем у тебя самые большие проблемы, xDD", reply_markup=markup)

def listing(message, lst):
    bot.send_message(message.chat.id, "————————————————————————")
    for _ in range(len(lst)):
        bot.send_message(message.chat.id, f"{_+1}. {lst[_]}")
    bot.send_message(message.chat.id, "————————————————————————")
    back(message)

def listing_sup(message, lst):
    bot.send_message(message.chat.id, "————————————————————————")
    for _ in range(len(lst)):
        bot.send_message(message.chat.id, f"{_+1}. {lst[_]}")
    bot.send_message(message.chat.id, "————————————————————————")

def list_adding(message, lst):
    lst.append(message.text)
    bot.send_message(message.chat.id, "Задолжность добавлена")
    back(message)

def list_removing(message, lst):
    lst.pop(int(message.text)-1)
    bot.send_message(message.chat.id, "Задолжность удалена")
    back(message)

prev = None

def main():  # main function, that contain most of commands

    @bot.message_handler(commands=["start"])  # start message
    def start_message(message):
        bot.send_message(message.chat.id, f"Привет, я универскальный бот помощник! Располагайся поудобнее.")

    @bot.message_handler(commands=["help", "test"])  # main bot menu
    def menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton("Расписание")
        button_2 = types.KeyboardButton("Домашка")
        button_3 = types.KeyboardButton("Долги")
        markup.add(button_1, button_2, button_3)
        bot.send_message(message.chat.id, "Выбери то, с чем у тебя самые большие проблемы, xDD", reply_markup=markup)

    @bot.message_handler(content_types=["text"])
    def Dolgi(message):
        global prev
        if message.text == "Долги":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_1 = types.KeyboardButton("Искусственный интелект")
            button_2 = types.KeyboardButton("Физическая культура и спорт")
            button_3 = types.KeyboardButton("Иностранный язык")
            button_4 = types.KeyboardButton("Математический анализ")
            button_5 = types.KeyboardButton("Объектно-ориентированное программирование")
            button_6 = types.KeyboardButton("Правоведение")
            button_7 = types.KeyboardButton("Русский язык и культура речи")
            button_8 = types.KeyboardButton("Структуры и алгоритмы обработки данных")
            button_9 = types.KeyboardButton("Физика")
            button_10 = types.KeyboardButton("Линейная алгебра и аналитическая геометрия")
            button_11 = types.KeyboardButton("Математическая логика и теория алгоритмов")
            markup.add(button_1, button_2, button_3, button_4, button_5,
                       button_6, button_7, button_8, button_9, button_10, button_11)
            bot.send_message(message.chat.id, "Выбери предмет", reply_markup=markup)

        elif message.text == "Искусственный интелект":
            prev = message.text
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_1 = types.KeyboardButton("Просмотреть задолжности")
            button_2 = types.KeyboardButton("Добавить задолжность")
            button_3 = types.KeyboardButton("Удалить задолжность")
            markup.add(button_1, button_2, button_3)
            bot.send_message(message.chat.id, f"Выбери действие", reply_markup=markup)

        elif (message.text == "Просмотреть задолжности") and (prev == "Искусственный интелект"):
            if len(AI_list) == 0:
                bot.send_message(message.chat.id, "Задолжностей нет, красава)")
                back(message)
            else:
                listing(message, AI_list)

        elif (message.text == "Добавить задолжность") and (prev == "Искусственный интелект"):
            msg = bot.send_message(message.chat.id, "Введи задолжность и день пересдачи")
            bot.register_next_step_handler(msg, list_adding, AI_list)

        elif (message.text == "Удалить задолжность") and (prev == "Искусственный интелект"):
            listing_sup(message, AI_list)
            msg = bot.send_message(message.chat.id, "Введи номер задолжности, которую надо удалить")
            bot.register_next_step_handler(msg, list_removing, AI_list)

        elif message.text == "Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_1 = types.KeyboardButton("Расписание")
            button_2 = types.KeyboardButton("Домашка")
            button_3 = types.KeyboardButton("Долги")
            markup.add(button_1, button_2, button_3)
            bot.send_message(message.chat.id, "Выбери то, с чем у тебя самые большие проблемы, xDD", reply_markup=markup)

    bot.infinity_polling()  # bot running

if __name__ == "__main__":
    main()