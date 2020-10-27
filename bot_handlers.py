from config import bot
from telegram import ParseMode
from buttons import *
from texts import *
from functions import *


@bot.message_handler(commands=["start"])
def send_menu(message):
    send_text(HELLO, message.from_user.id, keyboard=set_keyboard(main_buttons))


@bot.message_handler(content_types=["text", "document", "audio", "photo"])
def get_text_messages(message):
    id = message.from_user.id

    ## Main menu
    sender, kwargs = {
        HOMEWORK: (send_text, dict(message=WHICH_SBJ, id=id, keyboard=set_keyboard(subjects_buttons))),
        SCHEDULE: 1,
        DOCUMENTS: 1
    }.get(message.text, (send_text, dict(message="No such command", id=id)))
    sender(**kwargs)

    if message.text == HOMEWORK:
        send_text(WHICH_SBJ, id, keyboard=set_keyboard(subjects_buttons))
    elif message.text == SCHEDULE:
        send_text(WHICH_GRP, id, keyboard=set_keyboard(groups_buttons))
    elif message.text == DOCUMENTS:
        send_text(WHICH_DOCS, id, keyboard=set_keyboard(documents_buttons))
    elif message.text == CNTNCTS:
        send_text(CONTACTS, id, parse=ParseMode.HTML)
    elif message.text == HIST_POINTS:
        send_text(POINTS_HISTORY, id)


    ## Subjects

    elif message.text == HISTORY:
        send_photo(PIC_NAME_HIST, path=HIST_HMW_PATH, id=id, desc=DESC_HIST)
    elif message.text == ENGLISH:
        send_text(ENG_TEXT, id)
    elif message.text == MATH:
        send_photo(PIC_NAME_MATH, path=MATH_HMW_PATH, id=id, desc=DESC_MATH)
    elif message.text == INFORM:
        send_text(INF_TEXT, id, parse=ParseMode.HTML)
    elif message.text == TERVER:
        send_photo('t.png', path=TERV_HMW_PATH, id=id)
        send_photo('t1.png', path=TERV_HMW_PATH, id=id)

    ## Documents

    elif message.text == ENGTEXTS:
        send_text(WHICH_TXT_NB, id, keyboard=set_keyboard(eng_texts_buttons))
    elif message.text == DOC_ENG:
        send_doc(DOC_NAME_ENG, path=ENGL_DOC_PATH, id=id)
    elif message.text == DOC_INF:
        send_text(DOC_NAME_INFORM, id=id)

    ## English texts

    elif message.text == "1":
        send_photo("1.png", path=ENGL_DOC_PATH, id=id)
    elif message.text == "2":
        send_photo("2.png", path=ENGL_DOC_PATH, id=id)
    elif message.text == "3":
        send_photo("3.png", path=ENGL_DOC_PATH, id=id)
    elif message.text == "4":
        send_photo("4.png", path=ENGL_DOC_PATH, id=id)
    elif message.text == "5":
        send_photo("5.png", path=ENGL_DOC_PATH, id=id)
    elif message.text == "6":
        send_photo("6.png", path=ENGL_DOC_PATH, id=id)
    elif message.text == "7":
        send_photo("7.png", path=ENGL_DOC_PATH, id=id)
    elif message.text == "8":
        send_photo("8.png", path=ENGL_DOC_PATH, id=id)

    ## Schedule

    elif message.text == "ЕГЭ":
        send_photo(PIC_NAME_EGE, path=SCHEDULE_PATH, id=id)
    elif message.text == "СПО":
        send_photo(PIC_NAME_SPO, path=SCHEDULE_PATH, id=id)

    ## Wrong command

    else:
        send_text(IDONTKNOW, id, keyboard=set_keyboard(main_buttons))


if __name__ == "__main__":
    bot.polling(none_stop=True)
