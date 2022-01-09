import telebot #импорт pyTelegramBotAPI - подключаем библиотеку для работы в телеграм
import random #рандом - библиотека для получения случайых чисел
bot = telebot.TeleBot("5072458067:AAGNfscfb3fkFqvSiJxDEYhBDIDHuga3HEE") #ключ бота который нам выдал BotFather
#Переменные случайного числа которое загадывает бот и хода игрока 
rnd = 0
step = 0
usrdict = dict() #Создадим словарь пользователей 
stepdict = dict() #Создадим словарь ходов пользователей

@bot.message_handler() #commands=['start']
def send_welcome(message): #Основная процедура которая обрабатывает сообщения с клавиатуры. Параметр message - это текст отправленного сообщения  
    usrdig = message.text #Присвоим переменной текст, который пользователь ввёл нам в чате
    #step = 0
    if message.text.startswith("/start"):#Проверяем начинается сообщение на /start или нет.
        #Если да то выводим приветственное сообщение и загадываем число.
        bot.reply_to(message, "Здравствуй, {0.first_name}\nЯ загадал число от 0 до 100. Попробуй отгадать его!".format(message.from_user),parse_mode='html') #Вывод приветствия от бота в чат
        #global rnd #Объявим переменную rmd, как глобальную, то есть загадонное значение будет сохраняться и не сбрасываться.       
        #rnd = random.randrange(0, 101, 1) #Загадываем целое число от 0 до 100, которое будем угадывать
        #if not message.from_user.id in usrdict:
        usrdict[message.from_user.id] = random.randrange(0, 101, 1) #Загадываем целое число от 0 до 100, которое будем угадывать
        stepdict[message.from_user.id] = 1 #Счётчик ходов
        #global step #Счётчик ходов
        #step = 1
    elif message.text.startswith("/h"):#Проверяем начинается сообщение на /h или нет.
        bot.reply_to(message, "{0.first_name}\nЯ загадал число: ".format(message.from_user) + str(usrdict[message.from_user.id]).format(message.from_user),parse_mode='html') #Вывод загаданного числа в чат
    else:    
        try:# Попробуем перевести текст ответа в число 
            usr_val = int(eval(usrdig))#Переводим в целое число 
            if usr_val < int(usrdict[message.from_user.id]): #Если введённое число меньше загаданного 
                bot.reply_to(message, "Твоё число меньше чем я загадал".format(message.from_user),parse_mode='html')
            if usr_val > int(usrdict[message.from_user.id]):#Если введённое число больше загаданного 
                bot.reply_to(message, "Твоё число больше чем я загадал".format(message.from_user),parse_mode='html')
            if usr_val == int(usrdict[message.from_user.id]):#Если введённое число равно загаданного 
                msg = bot.reply_to(message, "Ура, я загадал имменно это число! Ты угадал его за ".format(message.from_user) + str(stepdict[message.from_user.id]).format(message.from_user)+" шагов!".format(message.from_user),parse_mode='html')
                bot.reply_to(msg, "{0.first_name}, сыграем ещё раз? Нажми /start".format(message.from_user),parse_mode='html') #Вывод приветствия от бота в чат
            stepdict[message.from_user.id] = stepdict[message.from_user.id] + 1 #Увеличем счётчик шагов на 1   
        except Exception as e:#Если не получилось перевести текст в число то сообщаем об ошибке
		        bot.reply_to(message, "Введи число!".format(message.from_user),parse_mode='html')
bot.polling()#Запускаем бота. Он будет работать, пока мы его не остановим в  VS Code. Чтобы он работал всегда нам надо разместить его на сервере