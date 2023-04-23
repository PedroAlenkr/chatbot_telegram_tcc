import telebot

# criação do bot com o token
bot = telebot.TeleBot('token do bot n vai pro github')

# função para lidar com o comando /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Olá, eu sou um bot!')

# início do bot
bot.polling()