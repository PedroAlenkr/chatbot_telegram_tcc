import telebot

# criação do bot com o token
bot = telebot.TeleBot('6035462268:AAGHAbn4sDsEC6cXbtj04ZWCKERo0EbuRdQ')

# função para lidar com o comando /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Olá, eu sou um bot!')

# início do bot
bot.polling()