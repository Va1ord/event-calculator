import telebot
from datetime import datetime


API_TOKEN = 'YOUR_TOKEN'

bot = telebot.Telebot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi, I'm an event calculator."
                     "Write me the event and its date (format: YYYY-MM-DD")

@bot.message_handler(func = lambda message: True)
def calculate_time(message):
    try:
        event_day = message.text.split(',')
        event_day = event_day[0].strip()
        event_day = datetime.strptime(event_day[1].strip(), "%Y-%m-%d")

        now = datetime.now()
        time = event_day - now

        if time.days < 0:
            days_pass = abs(time.days)
            bot.send_message(message.chat.id, f'The event "{event_day}" has already passed {days_pass}')
        else:
            bot.send_message(message.chat.id, f'Before the event "{event_day}" {time.days} days left')

    except Exception as e:
        bot.send_message(message.chat.id, 'An error has occurred. Make sure that you have entered everything correctly')


bot.polling()
