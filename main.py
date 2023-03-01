import codecs
import config
import telebot
from telebot import types

bot = telebot.TeleBot(config.TOKEN)  # вставить токен из BotFather

with open("dolgi.txt", "r+", encoding="utf-8") as file:
    dolgi_list = [line.strip() for line in file]

def numering(lst):  # функция, которая присваивает номера элементам списка
    for _ in range(len(lst)):
        if f"{_ + 1}." in lst[_]:
            pass
        else:
            lst[_] = f"{_ + 1}. *{lst[_]}*"
    return lst

def back(message):  # функция, которая возвращает пользователя в главное меню
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton("Долги")
    markup.add(button_1)
    bot.send_message(message.chat.id, "Выбери то, с чем у тебя самые большие проблемы, xDD", reply_markup=markup)

def listing(message, lst):  # функция, которая выводит на экран список задолжнстей с окончанием функцией back()
    temp_str = '\n\n'.join(numering(lst))
    bot.send_message(message.chat.id, f"{temp_str}", parse_mode="Markdown")

def list_adding(message, lst):  # функция, которая добавляет в список задолжность, после чего обновляет файл задолжностей
    if message.text == "Назад":
        back(message)
        return 0
    lst.append(message.text)
    lst = numering(lst)
    bot.send_message(message.chat.id, "Задолжность добавлена.")
    with open("dolgi.txt", "w", encoding="utf-8") as file:
        for line in lst:
            file.write(line + "\n")
    back(message)

def list_removing(message, lst):  # функция, которая удаляет из списока задолжность, после чего обновляет файл задолжностей
    try:
        if (int(message.text) <= 0) or (int(message.text) > len(lst)):
            bot.send_message(message.chat.id, "Задолжности с таким номером нет.")
            back(message)
        else:
            lst.pop(int(message.text)-1)
            bot.send_message(message.chat.id, "Задолжность удалена.")
            with open("dolgi.txt", "w", encoding="utf-8") as file:
                for line in lst:
                    file.write(line + "\n")
            back(message)
    except ValueError:
        if message.text == "Назад":
            back(message)
        else:
            bot.send_message(message.chat.id, "Номер введи, а не число, гений.")

def main():  # главная функция, содержит основной функционал бота

    @bot.message_handler(commands=["help", "test", "start"])  # главное меню бота
    def menu(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1 = types.KeyboardButton("Долги")
        markup.add(button_1)
        bot.send_message(message.chat.id, "Выбери то, с чем у тебя самые большие проблемы, xDD", reply_markup=markup)

    @bot.message_handler(content_types=["text"])  # основной функционал бота
    def Dolgi(message):
        if message.text == "Долги":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button_1 = types.KeyboardButton("Просмотреть задолжности")
            button_2 = types.KeyboardButton("Добавить задолжность")
            button_3 = types.KeyboardButton("Удалить задолжность")
            button_4 = types.KeyboardButton("Назад")
            markup.add(button_1, button_2, button_3, button_4)
            bot.send_message(message.chat.id, f"Выбери действие", reply_markup=markup)

        elif message.text == "Просмотреть задолжности":
            if len(dolgi_list) == 0:
                bot.send_message(message.chat.id, "Задолжностей нет, красава)")
                back(message)
            else:
                listing(message, dolgi_list)
                back(message)

        elif message.text == "Добавить задолжность":
            msg = bot.send_message(message.chat.id, "Введи задолжность и день пересдачи.")
            bot.register_next_step_handler(msg, list_adding, dolgi_list)

        elif message.text == "Удалить задолжность":
            listing(message, dolgi_list)
            msg = bot.send_message(message.chat.id, "Введи номер задолжности, которую надо удалить.")
            bot.register_next_step_handler(msg, list_removing, dolgi_list)

        elif message.text == "Назад":
            back(message)

    bot.infinity_polling()  # обязательная строка для работы бота

if __name__ == "__main__":  # входная точка кода
    main()
