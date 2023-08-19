import telebot
import json

bot = telebot.TeleBot("your token")

@bot.message_handler(commands=['start'])
def start(message):
    btn_zone = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn_I = telebot.types.KeyboardButton("Каталог")
    btn_II = telebot.types.KeyboardButton("Информация")

    btn_zone.add(btn_I, btn_II)
    bot.send_message(message.chat.id, "Здравствуйте, я телеграм-бот магазин товаров. Для более подробной информации обо мне нажмите на кнопку 'Информация'", reply_markup=btn_zone)


@bot.message_handler(commands=['history'])
def info(message):
    with open("../payment_info.json", "r") as file:
        a = json.load(file)
        if message.from_user.username in a:
            i = 1
            for item in a[f"{message.from_user.username}"]["items"]:
                bot.send_message(message.chat.id, f"{i}. Вы заказывали: {item}")
                i += 1
        else:
            bot.send_message(message.chat.id, "Ничего не куплено")

@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Информация":
        bot.send_message(message.chat.id, "По нажатию кнопки 'Каталог' - Откроется каталог товаров. \nПо вводу команды '/history' вы можете посмотреть свою историю заказов. ")
    if message.text == "Каталог":
        btn_zone = telebot.types.InlineKeyboardMarkup(row_width=3)

        btn_I = telebot.types.InlineKeyboardButton("Клавиатура", callback_data="Klava")
        btn_II = telebot.types.InlineKeyboardButton("Мышь", callback_data="Mouse")
        btn_d = telebot.types.InlineKeyboardButton("Коврик", callback_data="Kovrik")
        btn_arrow = telebot.types.InlineKeyboardButton(">>>", callback_data="Arrow")
        btn_zone.add(btn_I, btn_II, btn_d, btn_arrow)
        with open("img/Catalog.jpg", "rb") as img:
            caption_photo = "Каталог"
            bot.send_photo(message.chat.id, img, reply_markup=btn_zone, caption=caption_photo)


@bot.callback_query_handler(func=lambda call: True)
def inline_decor(call):
    if call.data == "Arrow":
        with open("img/Catalog.jpg", "rb") as img:
            btn_zone = telebot.types.InlineKeyboardMarkup(row_width=3)
            btn_I = telebot.types.InlineKeyboardButton("Монитор", callback_data="Monitor")
            btn_II = telebot.types.InlineKeyboardButton("Камера", callback_data="Cam")
            btn_d = telebot.types.InlineKeyboardButton("Компьютер", callback_data="pc")
            btn_arrow = telebot.types.InlineKeyboardButton("<<<", callback_data="Arrow_back")
            btn_zone.add(btn_I, btn_II, btn_d, btn_arrow)
            bot.edit_message_media(media=telebot.types.InputMediaPhoto(img, caption="Каталог"), chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=btn_zone)
    if call.data == "Arrow_back":
        with open("img/Catalog.jpg", "rb") as img:
            btn_zone = telebot.types.InlineKeyboardMarkup(row_width=3)
            btn_I = telebot.types.InlineKeyboardButton("Клавиатура", callback_data="Klava")
            btn_II = telebot.types.InlineKeyboardButton("Мышь", callback_data="Mouse")
            btn_d = telebot.types.InlineKeyboardButton("Коврик", callback_data="Kovrik")
            btn_arrow = telebot.types.InlineKeyboardButton(">>>", callback_data="Arrow")
            btn_zone.add(btn_I, btn_II, btn_d, btn_arrow)
            bot.edit_message_media(media=telebot.types.InputMediaPhoto(img, caption="Каталог"),
                                   chat_id=call.message.chat.id, message_id=call.message.message_id,
                                   reply_markup=btn_zone)
    if call.data == "Mouse":
        bot.send_invoice(chat_id=call.message.chat.id,
                         title="Купить мышь",
                         description="Мышь с высоким сенсором.",
                         invoice_payload="Мышь",
                         provider_token="",
                         currency="rub",
                         prices=[telebot.types.LabeledPrice("test", 100 * 100)],
                         need_email=True)

    if call.data == "Klava":
        bot.send_invoice(chat_id=call.message.chat.id,
                         title="Купить клаву",
                         description="Клавиатура с  rgb подсветкой.",
                         invoice_payload="Клавиатура",
                         provider_token="",
                         currency="rub",
                         prices=[telebot.types.LabeledPrice("test", 100 * 100)],
                         need_email=True)

    if call.data == "Kovrik":
        bot.send_invoice(chat_id=call.message.chat.id,
                         title="Купить коврик",
                         description="Коврик с красивым принтом.",
                         invoice_payload="Коврик",
                         provider_token="",
                         currency="rub",
                         prices=[telebot.types.LabeledPrice("test", 100 * 100)],
                         need_email=True)

    if call.data == "Monitor":
        bot.send_invoice(chat_id=call.message.chat.id,
                         title="Купить монитор",
                         description="Монитор 144 гц",
                         invoice_payload="Монитор",
                         provider_token="",
                         currency="rub",
                         prices=[telebot.types.LabeledPrice("test", 100 * 100)],
                         need_email=True)

    if call.data == "Cam":
        bot.send_invoice(chat_id=call.message.chat.id,
                         title="Купить камеру",
                         description="Камера 60 fps, Full HD",
                         invoice_payload="Камера",
                         provider_token="",
                         currency="rub",
                         prices=[telebot.types.LabeledPrice("test", 100 * 100)],
                         need_email=True)

    if call.data == "pc":
        bot.send_invoice(chat_id=call.message.chat.id,
                         title="Купить компьютер",
                         description="Компьютер, 16 RAM, AMD Ryzen 7 6800X, RTX 3070",
                         invoice_payload="Компьютер",
                         provider_token="",
                         currency="rub",
                         prices=[telebot.types.LabeledPrice("test", 100 * 100)],
                         need_email=True)






@bot.message_handler(content_types=['successful_payment'])
def successfull_payment(message):
    bot.send_message(message.chat.id, "Всё прошло успешно")
    with open("../payment_info.json", "r") as file:
        a = json.load(file)
        if message.from_user.username in a:
            a[f"{message.from_user.username}"]["items"].append(message.successful_payment.invoice_payload)
        else:
            new_user = {message.from_user.username:{"id":message.from_user.id, "items":[message.successful_payment.invoice_payload],"email": message.successful_payment.order_info.email}}
            a.update(new_user)
    with open("../payment_info.json", "w") as file:
        json.dump(a, file, indent=4)







@bot.pre_checkout_query_handler(func=lambda query: True)
def checkout(pre_checkout_query):
    bot.answer_pre_checkout_query(pre_checkout_query_id=pre_checkout_query.id, ok=True,
                                  error_message="Что-то пошло не так")
    print(pre_checkout_query.order_info.email)













bot.polling(none_stop=True)
