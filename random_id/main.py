import random
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup


# def start(update, context):
#     user_id = update.message.from_user.id
#     random_id = random.randint(100000, 999999)
#     context.user_data['id'] = random_id
#     update.message.reply_text(f"Assalomu Alaykum, bu sizning random \n\nID raqamingiz: <b>{random_id}</b>",
#                               parse_mode="HTML")


def inline_btn(btn_type=None, ctg=None, tip=None, bts=None):
    if btn_type == "call":
        btn = [
            [InlineKeyboardButton("Bog'lanish uchun👨🏻‍💻", url="https://t.me/Welkin_Manager")]
        ]

    return InlineKeyboardMarkup(btn)


def btns(tip=None):
    bts = []
    # if tip == "contact":
    #     bts.append([KeyboardButton("📞 Raqamni yuborish",
    #                                request_contact=True)])

    # if tip == "region":
    #     bts = [[KeyboardButton("Tashkent"), KeyboardButton("Farg'ona")],
    #            [KeyboardButton("Andijon"), KeyboardButton("Jizzax")],
    #            [KeyboardButton("Sirdaryo"), KeyboardButton("Surxondaryo")],
    #            [KeyboardButton("Samarqand"), KeyboardButton("Buxoro")],
    #            [KeyboardButton("Namangan"), KeyboardButton("Navoiy")],
    #            [KeyboardButton("Xorazm"), KeyboardButton("Qashqadaryo")],
    #            [KeyboardButton("Orqaga 🔙")]
    #            ]

    if tip == "lang":
        bts = [
            [KeyboardButton("🇺🇿 Uzbek tili")],
            [KeyboardButton("🇷🇺 Руский язык")],
            [KeyboardButton("🇺🇸 English")],
        ]

    elif tip == "connection":
        bts = [
            [KeyboardButton("Bog'lanish📲")],
            [KeyboardButton("Orqaga 🔙"),KeyboardButton("Keyingisi🔜")],
        ]

    elif tip == "my_id":
        bts = [
            [KeyboardButton("ID olish 🎲"), KeyboardButton("ID olmadm ❌")],
            [KeyboardButton("Orqaga🔙"), KeyboardButton("Bog'lanish 📲")],
        ]
    return ReplyKeyboardMarkup(bts, resize_keyboard=True)


def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"👋🏻 Assalomu Alaykum botga xush kelibsiz\n<b>Tilni tanlang</b> 👇🏻",
                              reply_markup=btns("lang"), parse_mode="HTML")


def message_handler(update, context):
    msg = update.message.text

    # Tillar
    if msg == "🇺🇿 Uzbek tili":
        update.message.reply_text(f"ID olishdan oldin biz bilan bog'laning biz sizni qaysi maktabda ish faoliyat olib"
                                  "borishingizni bilishimiz va bazaga qo'shishimiz kerak, "
                                  "bog'lanishingiz mumkin 👇🏻", reply_markup=btns("connection"))

    elif msg == "🇷🇺 Руский язык":
        update.message.reply_text(f"Пожалуйста, свяжитесь с нами перед получением удостоверения личности"
                                  "нам нужно знать, что вы идете и добавляете в базу данных, "
                                  "вы можете связаться👇🏻", reply_markup=btns("connection"))

    elif msg == "🇺🇸 English":
        update.message.reply_text(f"Please contact us before getting ID"
                                  "we need to know what you are going to add to the database "
                                  "you can contact👇🏻", reply_markup=btns("connection"))

    # ID olish uchun bog'lanish
    elif msg == "Bog'lanish📲":
        update.message.reply_text("UniCard Admin bilan bog'lanish👨🏻‍💻",
                                  reply_markup=inline_btn("call"), parse_mode="HTML")

    # Contact
    elif msg == "Keyingisi🔜":
        update.message.reply_photo(photo=open("photo_2023-03-24_14-01-03.jpg", "rb"),
                                   caption="Sizga random ID berilgandan so'ng 👆🏻 \nSite da <b>Tasdiqlash ko'dni "
                                           "kiriting"
                                           "</b> bo'sh katagiga kiriting.",
                                   reply_markup=btns("my_id"), parse_mode="HTML")

    # ID olish
    elif msg == "ID olish 🎲":
        user_id = update.message.from_user.id
        random_id = random.randint(100000, 999999)
        context.user_data['id'] = random_id
        update.message.reply_text(f"UniCard, uchun 1 martalik random \n\nID raqamingiz: <b>{random_id}</b>",
                                  parse_mode="HTML")
    
    elif msg == "ID olmadm ❌":
        chat_id = update.message.chat_id
        context.bot.send_document(chat_id=chat_id, document=open("YordamPDF.pdf", "rb"), filename='YordamPDF.pdf',
                                  caption="<b>Unicard</b> loyihasi haqida va to'g'ri boshqarish sistemadan to'g'ri "
                                          "foydalani to'g'risida elektron tushuncha PDF.\nQo'shimcha ma'lumotlar "
                                          "uchun👇🏻", reply_markup=inline_btn("call"), parse_mode="HTML")

    elif msg == "Bog'lanish 📲":
        update.message.reply_text("Agarda foydalanish va o'z ID raqamingizni olishda muammolar tug'ulgan bo'lsa.\nBiz "
                                  "bilan"
                                  "bog'lanishingiz mumkin 👇🏻",
                                  reply_markup=inline_btn("call"), parse_mode="HTML")

    # orqaga qaytish
    elif msg == "Orqaga🔙":
        update.message.reply_text("Siz random ID raqamingzni olishdan oldin UniCard Admini bilan bog'lanishingiz va\n"
                                  "ma'lumotlarni to'ldirishingiz kerak👇🏻",
                                  reply_markup=btns("connection"))

    elif msg == "Orqaga 🔙":
        update.message.reply_text("Til tanlashda adashdingizmi unda boshqa tilda murojat qiling👇🏻",
                                  reply_markup=btns("lang"))


def main():
    updater = Updater("6268136991:AAFiMH6cV77iOceXf33lx1wvdZb5KUIV91Y", use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(MessageHandler(Filters.text, message_handler))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
