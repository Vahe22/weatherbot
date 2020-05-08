import pyowm
import telebot

owm = pyowm.OWM('39e36f9b1f21d3ba74cd21c5c65c8527', language="eng")
bot = telebot.TeleBot("1250094784:AAGiQVMenJlrotPQg8gkOMNzwVE_Gw7KsNg")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place(message.text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')['temp']


    answer = 'In ' + message.text + ' is ' +  w.get_detailed_status() + "\n"
    answer += 'Temperature in ' + message.text + ' is ' + str(temp) + "\n\n"

    if temp < 10:
        answer +='Now so cold wear hot clothes'
    elif temp < 20:
        answer +='Now weather is normal'
    elif temp >= 20:
        answer +='Now weather is hot'



    bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )