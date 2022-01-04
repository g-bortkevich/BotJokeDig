import telebot #импорт pyTelegramBotAPI - подключаем библиотеку для работы в телеграм
import random #рандом - библиотека для получения случайых чисел
bot = telebot.TeleBot("5072458067:AAGNfscfb3fkFqvSiJxDEYhBDIDHuga3HEE")#ключ бота который нам выдал BotFather
rnd = 0

step = 0
@bot.message_handler()
def send_welcome(message): #Основная процедура которая обрабатывает сообщения с клавиатуры. Параметр message - это текст отправленного сообщения  
    usrdig = message.text #Присвоим переменной текст, который пользователь ввёл нам в чате
    #step = 0
    if message.text.startswith("/start"):#Проверяем начинается сообщение на /start или нет.
        #Если да то выводим приветственное сообщение и загадываем число.
        bot.reply_to(message, "Здравствуй, {0.first_name}\nЯ загадал число от 0 до 100. Попробуй отгадать его!".format(message.from_user),parse_mode='html') #Вывод приветствия от бота в чат
        global rnd #Объявим переменную rmd, как глобальную, то есть загадонное значение будет сохраняться и не сбрасываться.
        rnd = random.randrange(0, 101, 1) #Загадываем целое число от 0 до 100, которое будем угадывать
        global step #Счётчик ходов
        step = 1
    else:
        #Иначе, если сообщение не начинается на старт, то считаем что пользователь вводит свой ответ
        try:# Попробуем перевести текст ответа в число 
            usr_val = int(eval(usrdig))#Переводим в целое число 
            if usr_val < rnd: #Если введённое число меньше загаданного 
                bot.reply_to(message, "Твоё число меньше чем я загадал".format(message.from_user),parse_mode='html')
            if usr_val > rnd:#Если введённое число больше загаданного 
                bot.reply_to(message, "Твоё число больше чем я загадал".format(message.from_user),parse_mode='html')
            if usr_val == rnd:#Если введённое число равно загаданного 
                msg = bot.reply_to(message, "Ура, я загадал имменно это число! Ты угадал его за ".format(message.from_user) + str(step).format(message.from_user)+" шагов!".format(message.from_user),parse_mode='html')
                bot.reply_to(msg, "{0.first_name}, сыграем ещё раз? Нажми /start".format(message.from_user),parse_mode='html') #Вывод приветствия от бота в чат
            step = step + 1 #Увеличем счётчик шагов на 1   
        except Exception as e:#Если не получилось перевести текст в число то сообщаем об ошибке
		        bot.reply_to(message, "Введи число!".format(message.from_user),parse_mode='html')
bot.polling()#Запускаем бота. Он будет работать, пока мы его не остановим в  VS Code. Чтобы он работал всегда нам надо разместить его на сервере