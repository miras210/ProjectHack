# -*- coding: utf-8 -*-
import telebot
import time
import mysql.connector
import sys
reload(sys)
sys.setdefaultencoding("utf-8")


"""--------------------DATABASE--------------------"""
mydb = mysql.connector.connect(user='LucaN4ick',
password='123123YyY!',
host='LucaN4ick.mysql.pythonanywhere-services.com',
database='LucaN4ick$default'
)

mycursor = mydb.cursor()
"""--------------------DATABASE--------------------"""
from datetime import date
from telebot import types

TOKEN = '926752910:AAFGad8KGmXJGXkO2tX0re0MXLv4NPPLwTw'

knownUsers = []
userStep = {}
userNum = {}
userName = {}
userSurname = {}

appealType = {}
appealTheme = {}
appealText = {}
appealLocLong = {}
appealLocLat = {}
appealDate = {}
appealID = {}
gosUch = {}

commands = {
    'start'     : 'This is the beginning of ur journey',
    'help'      : 'Use this in order to see other commands'
}

hideBoard = types.ReplyKeyboardRemove()

"""--------------------FUNCTIONS SECTION------------------------"""
def send_contact(cid,phone):
    bot.SendContact(cid, phone, "Служба поддержки")

def wrong_command(cid):
    bot.send_message(cid, "Hey, bullsh*t you have typed wrong command")
    bot.send_message(cid, "Please try again")

def TelPhone(cid):
    PAns = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    Yes = types.KeyboardButton('Yes', request_contact=True)
    No = types.KeyboardButton('No', request_contact=False)
    PAns.row(Yes, No)
    bot.send_message(cid, "Do You trust us ur phone number ?", reply_markup=PAns)

def MainMenu(cid):
    Menu = types.ReplyKeyboardMarkup(row_width = 2)
    Appeal = types.KeyboardButton('Обратиться')
    AppealCheckout = types.KeyboardButton('Проверить обращение')
    AppealHistory = types.KeyboardButton('История обращений')
    ExtraCall = types.KeyboardButton('Звонок в 109')
    Menu.row(Appeal,AppealCheckout)
    Menu.row(AppealHistory,ExtraCall)
    bot.send_message(cid,"Now wait a sec until new command appears",reply_markup=Menu)

def Type(cid):
    Type = types.ReplyKeyboardMarkup(row_width=1)
    Type.add('Жалоба','Предложение','Запрос','Заявление','Отклик','Назад')
    bot.send_message(cid, "Choose your type please", reply_markup=Type)
    userStep[cid] = 20

def Theme(cid):
    Theme = types.ReplyKeyboardMarkup(row_width=1)
    Theme.add('Свет', 'Вода', 'Канализация', 'Логистика', 'Митинги','Назад')
    bot.send_message(cid, "Choose your theme please", reply_markup=Theme)
    userStep[cid] = 21

def GosUch(cid):
    Gos = types.ReplyKeyboardMarkup(row_width=1)
    Gos.add('МВД', 'КСК', 'ЦОН', 'Больницы', 'Акимат','Назад')
    bot.send_message(cid, 'Choose your гос орган', reply_markup=Gos)
    userStep[cid] = 22

def Doc(cid):
    Doc = types.ReplyKeyboardMarkup(row_width=2)
    Doc.add('Yes', 'No')
    bot.send_message(cid, 'Would you like to send some files ?', reply_markup=Doc)
    userStep[cid] = 24

def history(cid):
    markup = InlineKeyboardMarkup()
    sql = "SELECT appeal_id, date FROM appeal_info WHERE user_id = %s"
    val = (cid, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for row in myresult:
        for val in range(2):
            if val == 0:
                msg1 = val
            else:
                msg2 = val
        markup.add(InlineKeyboardButton("Appeal num [" + msg1 + "] written on " + msg2, callback_data=msg1))
    return markup

def get_user_data(uid):
    print("[" + str(uid) + "] " + userName[uid] + " " + userSurname[uid] + " " + userNum[uid])
    return 0

def get_user_step(uid):
    if uid in userStep:
        return userStep[uid]
    else:
        knownUsers.append(uid)
        userStep[uid] = 0
        print("New user detected and added \n")
        return 0

def listener(messages):
    for m in messages:
        print(str(m.chat.first_name) + " [" + str(m.chat.id) + "]: " + str(m.text))

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(listener)

def alertBut(m):
    cid = m.chat.id
    time.sleep(1)
    Ans = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    Ans.add('Yes', 'No')
    userStep[cid] = 1
    bot.send_message(cid, "Is ur phone number in Telegram real one ?", reply_markup = Ans)

def PhoneCheck(num):
    if not (len(num) == 11 or len(num) == 12):
        return False
    else:
        if len(num) == 12 and (num[0] != '+' or num[1] != '7'):
            return False
        elif len(num) == 11 and num[0] != '7':
            return False
        else:
            if len(num) == 12:
                num = num[2:]
            elif len(num) == 11:
                num = num[1:]
            for ch in num:
                if not (ch >= '0' and ch <= '9'):
                    return False
            return True


"""--------------------FUNCTIONS SECTION------------------------"""

"""----------------------- HANDLERS ----------------------------"""
@bot.message_handler(commands=['start'])
def command_help(m):
    cid = m.chat.id
    if cid not in knownUsers:
        knownUsers.append(cid)
        bot.send_photo(cid, open('logo.jpg', 'rb'))
        bot.send_message(cid, "Здравствуйте! Вы обратились в информационно-справочную службу 109")
        alertBut(m)
    elif userStep[cid] >= 10:
        bot.send_message(cid, "I already know you, so what is ur choice ?")
        #action buttons
    else:
        bot.send_photo(cid, open('logo.jpg', 'rb'))
        bot.send_message(cid, "Здравствуйте! Вы обратились в информационно-справочную службу 109")
        alertBut(m)


@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 1)
def msg_choice(m):
    cid = m.chat.id
    text = m.text
    if text == 'Yes':
        userStep[cid] = 2
        TelPhone(cid)
    elif text == 'No':
        userStep[cid] = 5
        bot.send_message(cid, "Please enter ur phone number\nRight Format: +7**********")
    else:
        wrong_command(cid)

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 5)
def inp_tel(m):
    cid = m.chat.id
    text = m.text
    #func check num
    if PhoneCheck(text):
        if len(text) == 11:
            userNum[cid] = text[1:]
        elif len(text) == 12:
            userNum[cid] = text[2:]
        time.sleep(1)
        bot.send_message(cid, "Enter your name, please")
        userStep[cid] = 3
    else:
        bot.send_message(cid, "You have entered your phone number in a wrong format\nPlease try to do it again")

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 2)
def phone_num(m):
    cid = m.chat.id
    text = m.text
    if text == 'No':
        bot.send_message(cid, "Fuck*ng bastard send ur motherfuck*ng Telegram number")
        TelPhone(cid)
    else:
        wrong_command(cid)

@bot.message_handler(content_types=['contact'])
def phone(m):
    cid = m.chat.id
    num = m.contact.phone_number
    #func check num
    if PhoneCheck(num):
        if len(num) == 11:
            userNum[cid] = num[1:]
        elif len(num) == 12:
            userNum[cid] = num[2:]
        bot.send_message(cid, "Processing ur data ...", reply_markup=hideBoard)
        time.sleep(1)
        bot.send_message(cid, "Enter your name, please")
        userStep[cid] = 3
    else:
        userStep[cid] = 5
        bot.send_message(cid, "You have entered your phone number in a wrong format\nPlease try to do it again")

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 3)
def name(m):
    cid = m.chat.id
    text = m.text
    userName[cid] = text
    bot.send_message(cid, "Processing your data ...")
    time.sleep(1)
    bot.send_message(cid, "Enter your surname, please")
    userStep[cid] = 4

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 4)
def surname(m):
    cid = m.chat.id
    text = m.text
    userSurname[cid] = text
    get_user_data(cid)
    """--------------------DATABASE STUFF--------------------"""
    sql = "INSERT INTO users (user_id, fname, lname, phone_num ) VALUES (%s, %s, %s, %s)"
    val = (cid, userName[cid], userSurname[cid],userNum[cid])
    bot.send_message(cid, "Thank you for your answers")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "Succesfull!")
    """--------------------DATABASE STUFF--------------------"""
    userStep[cid] = 10
    time.sleep(1)
    MainMenu(cid)
"""--------------------Main Menu--------------------"""
@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 10)
def choice(m):
    cid = m.chat.id
    text = m.text
    if text == 'Обратиться':
        Type(cid)
    elif text == 'Проверить обращение':
        time.sleep(1)
        bot.send_message(cid, "Введите номер вашего обращения", reply_markup=hideBoard)
        userStep[cid] = 30
    elif text == 'История обращений':
        time.sleep(1)
        bot.send_message(cid,"Choose any appeal id to see info",reply_markup=history(cid))
        userStep[cid] = 40
    elif text == 'Звонок в 109':
        userStep[cid] = 50
    else:
        wrong_command(cid)
"""--------------------Main Menu--------------------"""

"""--------------------Обратиться--------------------"""
@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 20)
def ap_type(m):
    cid = m.chat.id
    text = m.text
    if text == 'Жалоба' or text == 'Предложение' or text == 'Запрос' or text == 'Заявление' or text == 'Отклик':
        appealType[cid] = text
        Theme(cid)
    else:
        wrong_command(cid)

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 21)
def theme(m):
    cid = m.chat.id
    text = m.text
    if text == 'Свет' or text == 'Вода' or text == 'Канализация' or text == 'Логистика':
        appealTheme[cid] = text
        GosUch(cid)
    elif text == 'Митинги':
        bot.send_message(cid, 'Ах ты Жукуш Улан')
        appealTheme[cid] = text
        GosUch(cid)
    else:
        wrong_command(cid)

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 22)
def gos(m):
    cid = m.chat.id
    text = m.text
    if text == 'МВД' or text == 'КСК' or text == 'ЦОН' or text == 'Больницы' or text == 'Акимат':
        gosUch[cid] = text
        bot.send_message(cid, 'Now you can enter your appeal', reply_markup=hideBoard)
        userStep[cid] = 23
    else:
        wrong_command(cid)

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 23)
def appeal(m):
    cid = m.chat.id
    text = m.text
    if len(text) <= 800:
        appealText[cid] = text
        Doc(cid)
    else:
        bot.send_message(cid, 'You have written very long text, please write a bit shorter (max 800 characters)')

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 24)
def doc(m):
    cid = m.chat.id
    text = m.text
    if text == 'Yes':
        bot.send_message(cid, "Send your files here", reply_markup=hideBoard)
    elif text == 'No':
        #next
        bot.send_message(cid, 'Moving to the next step. Type "Next"', reply_markup=hideBoard)
        userStep[cid] = 25
    else:
        wrong_command(cid)

@bot.message_handler(content_types=['document', 'photo'])
def send(m):
    cid = m.chat.id
    #passing docs
    pass
    bot.send_message(cid, 'Any other file ?\nIf yes, send it. Otherwise type "No"')
    userStep[cid] = 25

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 25)
def geo(m):
    cid = m.chat.id
    geoL = types.ReplyKeyboardMarkup(row_width=2)
    yes = types.KeyboardButton("Yes", request_location=True)
    no = types.KeyboardButton("No")
    geoL.add(yes, no)
    bot.send_message(cid, "Would you like to send us ur current location ?", reply_markup=geoL)
    userStep[cid] = 26

@bot.message_handler(content_types=['location'])
def loc(m):
    cid = m.chat.id
    long = m.location.longitude
    lat = m.location.latitude
    appealLocLong[cid] = long
    appealLocLat[cid] = lat
    bot.send_message(cid, 'Your data is processing ...', reply_markup=hideBoard)
    time.sleep(1)
    bot.send_message(cid, 'I am ready, type next')
    userStep[cid] = 26

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 26)
def ready(m):
    cid = m.chat.id
    conf = types.ReplyKeyboardMarkup(row_width=2)
    conf.add('Yes', 'No')
    bot.send_message(cid, 'Are you ready to send the appeal ?', reply_markup=conf)
    userStep[cid] = 27

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 27)
def confirm(m):
    cid = m.chat.id
    text = m.text
    if text == 'Yes':
        appealDate[cid] = date.today()
        #send data, get appeal id
        sql = "INSERT INTO appeal_info (appeal_type, appeal_theme, appeal_text, date, user_id, status) VALUES (%s, %s, %s, %s, %s, 'зарегистрировано')"
        val = (appealType[cid], appealTheme[cid], appealText[cid], appealDate[cid], cid)
        bot.send_message(cid,"Thank you for your info")
        mycursor.execute(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "Appeal_Info Updated")
        time.sleep(1)
        sql = "SELECT appeal_id FROM appeal_info WHERE user_id = %s"
        val = (cid, )
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            for k in x:
                appealID[cid] = k
        msg = "Your num is #" + str(appealID[cid])
        bot.send_message(cid, msg, reply_markup=hideBoard)
        MainMenu(cid)
        userStep[cid] = 10
    elif text == 'No':
        Type(cid)
        userStep[cid] = 10
    else:
        wrong_command(cid)

@bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 30)
def appealCheck(m):
    cid = m.chat.id
    text = m.text
    sql = "SELECT date, status FROM appeal_info WHERE appeal_id = %s"
    val = (text, )
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()
    for x in myresult:
        for i in range(2):
            if i == 0:
                date = x[i]
            else:
                status = x[i]
    msg = "Ваше обращение написанное " + str(date) + " числа под номером #" + str(text) + ": " + str(status)
    bot.send_message(cid, msg)
    time.sleep(1)
    MainMenu(cid)
    userStep[cid] = 10

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    sql = "SELECT appeal_id, status FROM appeal_info WHERE appeal_id = %s"
    val = (call.data, )
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    for x in myresult:
        for i in range(2):
            if i == 0:
                id = x[i]
            else:
                status = x[i]
    msg = "Ваше обращение под номером #" + str(id) + " имеет статус " + str(status)
    bot.send_message(call.id, msg)
    time.sleep(1)
    MainMenu(cid)
    userStep[cid] = 10

# @bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 30)
# def history(m):
#     cid = m.chat.id
#     sql = ("SELECT appeal_id FROM appeal_info WHERE user_id = %s")
#     val = (cid, )
#     mycursor.execute(sql, val)
#     myresult = mycursor.fetchall()
#     markup = types.InlineKeyboardMarkup()
#     for x in myresult:
#         for k in x:
#             markup.add(types.InlineKeyboardButton(text=k,callback_data="['Номер обращения', '" + k + "']")
#             bot.send_message(chat_id=message.chat.id,
#                      text="Here are the values of stringList",
#                      reply_markup=makeKeyboard(),
#                      parse_mode='HTML')
# @bot.message_handler(func=lambda m: get_user_step(m.chat.id) == 50)
# def ExtraCall(m):
#     cid = m.chat.id
#     send_contact(cid, 109)
"""--------------------Обратиться--------------------"""



bot.polling()
