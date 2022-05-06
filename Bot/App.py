import telebot
from Config import TOKEN, keys
from Utils import ConvertionExeption, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: telebot.types.Message):
    text = 'Чтобы начать введите команду в формате: ' \
           '\n<Название валюты> \n<В какую валюту перевести> \n<Количество переводимой валюты>' \
           '\nПосмотреть список доступных валют ----> /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        value = message.text.split(' ')

        if len(value) != 3:
            raise ConvertionExeption('Слишком много параметров.')

        quote, base, amount = value
        total_base = CryptoConverter.convert(quote, base, amount)

    except ConvertionExeption as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')

    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')

    else:
        text = f'За {amount} - {quote} вы получите \n{total_base * int(amount)} - {base} \nпо курсу cryptocompare.com'
        bot.send_message(message.chat.id, text)


bot.polling()
