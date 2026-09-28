import telebot
import webbrowser

bot = telebot.TeleBot("none api key ^_^")


@bot.message_handler(commands=["start"])
def main(message):
    bot.send_message(message.chat.id, "Hello World!")


@bot.message_handler(commands=["hello"])
def main(message):
    bot.send_message(
        message.chat.id,
        f"Hello {message.from_user.first_name} {message.from_user.last_name}",
    )


@bot.message_handler()
def idx(message):
    if message.text.lower() == "w3school":
        bot.reply_to(
            message,
            "is time to learning!!!Weee :3",
        )
        webbrowser.open("https://www.w3schools.com")


bot.infinity_polling()
""" bot.polling(non_stop=True) """
