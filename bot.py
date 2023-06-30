import telebot
bot = telebot.TeleBot('YOUR TOKEN')
from telebot import types

@bot.message_handler(content_types=['text'])

@bot.message_handler(commands=['start'])
def msg(message):
    if message.text == 'эмодзи | Кто-то в что-то':
        markup = types.InlineKeyboardMarkup()
        site = types.InlineKeyboardButton(text='Клик!', url='ссылка на одну соцсеть')
        markup.add(site)
        bot.send_message(message.from_user.id, 'По кнопке можно перейти на соцсеть!', reply_markup=markup)
    elif message.text == 'эмодзи | Кто-то в что-то':
        markup = types.InlineKeyboardMarkup()
        site = types.InlineKeyboardButton(text='Клик!', url='ссылка на одну соцсеть')
        markup.add(site)
        bot.send_message(message.from_user.id, 'По кнопке можно перейти на соцсеть!', reply_markup=markup)
    elif message.text == 'эмодзи | Кто-то в что-то':
        markup = types.InlineKeyboardMarkup()
        site = types.InlineKeyboardButton(text='Клик!', url='ссылка на одну соцсеть')
        markup.add(site)
        bot.send_message(message.from_user.id, 'По кнопке можно перейти на соцсеть!', reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('эмодзи | Кто-то в что-то')
        btn2 = types.KeyboardButton('эмодзи | Кто-то в что-то')
        btn3 = types.KeyboardButton('эмодзи | Кто-то в что-то')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, 'Привет! Я Путеводитель кое-кого! Нажми на кнопку, чтобы перейти к чему-то!', reply_markup=markup)

bot.polling(none_stop=True, interval=0)