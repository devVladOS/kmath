import telebot
from telebot import types
from telebot.types import InputMediaPhoto

bot = telebot.TeleBot('');

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Здарова, "  + message.from_user.first_name + "! Это бот проекта *kmath*.\nКонтрошы по матеше в одном месте!\n``` Тот, у кого есть контрольные по математике - есть Бог ``` _Владислав Тихомиров, голова проекта_", parse_mode="Markdown")
	choose(message)

@bot.message_handler(commands=['help'])
def send_help(message):
	bot.send_message(message.chat.id, "*Справка по командам*\n/choose - выбрать раздел\n/help - справка по командам", parse_mode="Markdown")

@bot.message_handler(commands=['choose'])
def choose(message):
	keyboard = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton('Алгебра', callback_data='alg')
	btn2 = types.InlineKeyboardButton('Геометрия', callback_data='geom')
	keyboard.add(btn1)
	keyboard.add(btn2)
	bot.send_message(message.chat.id, "Выбери раздел", reply_markup=keyboard, parse_mode="Markdown")

def razdel_alg(call):
	keyboard = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton('КР №1', callback_data='ak1')
	btn2 = types.InlineKeyboardButton('КР №2', callback_data='ak2')
	btn3 = types.InlineKeyboardButton('КР №3', callback_data='ak3')
	btn4 = types.InlineKeyboardButton('КР №4', callback_data='ak4')
	btn5 = types.InlineKeyboardButton('КР №5', callback_data='ak5')
	btn6 = types.InlineKeyboardButton('КР №6', callback_data='ak6')
	btn7 = types.InlineKeyboardButton('КР №7', callback_data='ak7')
	btn8 = types.InlineKeyboardButton('КР №8', callback_data='ak8')
	btn9 = types.InlineKeyboardButton('КР №9', callback_data='ak9')
	keyboard.add(btn1, btn2, btn3)
	keyboard.add(btn4, btn5, btn6)
	keyboard.add(btn7, btn8, btn9)
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Раздел *Алгебра*", reply_markup=keyboard, parse_mode="Markdown")

def razdel_geom(call):
	keyboard = types.InlineKeyboardMarkup()
	btn1 = types.InlineKeyboardButton('КР №1', callback_data='gk1')
	btn2 = types.InlineKeyboardButton('КР №2', callback_data='gk2')
	btn3 = types.InlineKeyboardButton('КР №3', callback_data='gk3')
	btn4 = types.InlineKeyboardButton('КР №4', callback_data='gk4')
	btn5 = types.InlineKeyboardButton('КР №5', callback_data='gk5')
	btn6 = types.InlineKeyboardButton('КР №6', callback_data='gk6')
	keyboard.add(btn1, btn2, btn3)
	keyboard.add(btn4, btn5, btn6)
	bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Раздел *Геометрия*", reply_markup=keyboard, parse_mode="Markdown")

def test(lesson, number, call):
    if number != '9':
        pic1 = open("/kmath/"+lesson+"/kr"+number+"/"+number+"krv1.jpg", "rb")
        pic2 = open("/kmath/"+lesson+"/kr"+number+"/"+number+"krv2.jpg", "rb")
        pic3 = open("/kmath/"+lesson+"/kr"+number+"/"+number+"krv3.jpg", "rb")
        pic4 = open("/kmath/"+lesson+"/kr"+number+"/"+number+"krv4.jpg", "rb")
        pic5 = open("/kmath/"+lesson+"/kr"+number+"/d"+number+"krv1.jpg", "rb")
        pic6 = open("/kmath/"+lesson+"/kr"+number+"/d"+number+"krv2.jpg", "rb")
        media1 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2), InputMediaPhoto(pic3), InputMediaPhoto(pic4), InputMediaPhoto(pic5), InputMediaPhoto(pic6)]
    else:
        pic1 = open("/kmath/"+lesson+"/kr"+number+"/d"+number+"krv1.jpg", "rb")
        pic2 = open("/kmath/"+lesson+"/kr"+number+"/d"+number+"krv2.jpg", "rb")
        media1 = [InputMediaPhoto(pic1), InputMediaPhoto(pic2)]
    bot.send_chat_action(chat_id=call.message.chat.id, action="upload_photo")
    bot.send_media_group(chat_id=call.message.chat.id, media=media1)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
	if call.data == 'alg':
		razdel_alg(call)

	if call.data == 'geom':
		razdel_geom(call)	

	if call.data[1] == 'k':
		test(call.data[0], call.data[2], call)
		if 

@bot.message_handler(content_types=['sticker'])
def reply_sticker(message):
	bot.send_message(message.chat.id, "Я не понимаю стикеров")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
		bot.send_message(message.chat.id, "Я не понимаю тебя\nСправка по командам: /help")

bot.polling(none_stop=True, interval=0)
