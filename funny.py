from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

updater = Updater("6348259626:AAGtOuKGB0HmJYVBhH-GoVp8As1jwPPJryA", use_context=True)

def start(update):
    update.message.reply_text(
        "Hello my friend! Welcome to the FunnyBot. Type /help to see available commands."
    )

def help(update):
    update.message.reply_text(
        """Available Commands:
        /youtube - Get the YouTube URL
        """
    )


def youtube_url(update):
    update.message.reply_text("YouTube Link => https://www.youtube.com/")


def unknown(update):
    update.message.reply_text(f"Sorry '{update.message.text}' is not a valid command")

def unknown_text(update):
    update.message.reply_text(f"Sorry, I can't recognize your input: '{update.message.text}'")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.start_polling()
