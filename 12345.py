from this import s

import telebot
import wikipedia
import re
from telebot import types
import requests
import datetime
from config import bottoken, weather_token

bot = telebot.TeleBot(bottoken)
open_weather_token = weather_token
wikipedia.set_lang("ru")


def keyboard_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('/start')
    markup.add(item1)
    bot.send_message(message.chat.id, 'с начала?', reply_markup=markup)


@bot.message_handler(commands=['start'])
def welcome(message, txt=None):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("погода")
    item2 = types.KeyboardButton("перевертыш")
    item3 = types.KeyboardButton("википедия")
    kb.add(item1, item2, item3)
    if txt is None:
        bot.send_message(message.chat.id, f'Hello, {message.from_user.first_name}\n"Выберите что-нибудь ⬇"',
                         reply_markup=kb)
    else:
        bot.send_message(message.chat.id, txt, reply_markup=kb)


@bot.message_handler(content_types=['text'])
def some_text(message):
    text = message.text.lower()
    if text == 'погода':
        kb = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.chat.id, 'В каком населённом пункте хотим узнать погоду?', reply_markup=kb)
        bot.register_next_step_handler(msg, weather)

    elif text == 'перевертыш':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.chat.id, 'Поиграем?\nНапиши слово:', reply_markup=markup)
        bot.register_next_step_handler(msg, change_message)

    elif text == 'википедия':
        markup = telebot.types.ReplyKeyboardRemove()
        msg = bot.send_message(message.chat.id,
                               "Отправь мне любое слово, и я найду его значение на Wikipedia\nНапишите слово на русском:",
                               reply_markup=markup)
        bot.register_next_step_handler(msg, word)


def wiki(sd):
    try:
        ny = wikipedia.page(sd)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        wikitext2 = ''
        for x in wikimas:
            if not ('==' in x):
                if len((x.strip())) > 3:
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except:
        return 'В энциклопедии нет информации об этом'


def word(message):
    bot.send_message(message.chat.id, wiki(message))
    end_func(message)


def change_message(message):
    text = message.text.lower()
    bot.send_message(message.chat.id, 'Вот как будет наоборот: ')
    bot.send_message(message.chat.id, text[::-1])
    end_func(message)


def weather(message):
    emodji = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Ясно \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F23B'
    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        city = data['name']
        cur_temp = data['main']['temp']
        cur_humidity = data['main']['humidity']
        cur_pressure = data['main']['pressure']
        temp_max = data['main']['temp_max']
        temp_min = data['main']['temp_min']
        wind_speed = data['wind']['speed']
        sunrise_time = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_time = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        weather_emodzi = data['weather'][0]['main']
        if weather_emodzi in emodji:
            weather_em = emodji[weather_emodzi]
        else:
            weather_em = 'У природы нет плохой погоды'
        bot.send_message(message.chat.id, f'Сегодня ***{now}***\n'
                                          f'Погода в городе {city.capitalize()}:\n'
                                          f'Температура: {cur_temp} °С\n'
                                          f'{weather_em}\n'
                                          f'Влажность: {cur_humidity} %\n'
                                          f'Давление: {cur_pressure} мм.рт.ст\n'
                                          f'Максимальная температура: {temp_max} °С\n'
                                          f'Минимальная температура: {temp_min} °С\n'
                                          f'Скорость ветра: {wind_speed} м.с\n'
                                          f'Время рассвета: {sunrise_time}\n'
                                          f'Время заката: {sunset_time}\n'
                                          f'Хорошего настроения!!\n\n'
                         )
    except:
        bot.send_message(message.chat.id, 'Проверьте название города')
    end_func(message)


def end_func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    back = types.KeyboardButton('Основное меню')
    markup.add(back)
    msg = bot.send_message(message.chat.id, 'До свидания!', reply_markup=markup)
    txt = 'Продолжим?'
    bot.register_next_step_handler(msg, welcome, txt)


bot.polling(none_stop=True)
