from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
updater = Updater("6348259626:AAGtOuKGB0HmJYVBhH-GoVp8As1jwPPJryA", use_context=True)

def start(update, context):
    update.message.reply_text(
        "Hello my friend! Welcome to the FunnyBot. Type /help to see available commands."
    )

def help(update, context):
    update.message.reply_text(
         """Available Commands:
        /links - Get the URLs of SEOULTECH
        /gmail - Get the Gmail URL
        /git - Get the URL of Github
        /joke - Get a random 아재개그
        /youtube - Get Youtube URL
        /rand <min> <max> - Generate a random number within the specified range
        /rps - play Rock Paper Scissors game with funnyBot
        """
    )
def links(update, context):
    update.message.reply_text(
        """SEOULTECH Homepage URL => https://www.seoultech.ac.kr
        SUIS(통합정보) URL => https://suis.seoultech.ac.kr
        Portal URL => https://portal.seoultech.ac.kr
        e-class URL => https://eclass.seoultech.ac.kr
        Everytime URL => https://everytime.kr
        """
    )

def gmail_url(update, context):
    update.message.reply_text(
        "Gmail link here => https://mail.google.com"
    )

def youtube_url(update, context):
    update.message.reply_text("YouTube Link => https://www.youtube.com/")

def git_url(update, context):
    update.message.reply_text("Github Link => https://github.com")

def get_random_joke():
    jokes = [
        "아몬드가 죽으면? 다이아몬드",
        "소가 죽으면? 다이소",
        "미소의 반대말은? 당기소",
        "해가 울면? 해운대",
        "고양이가 지옥에 가면? 헬로키티",
        "이 세상에서 가장 야한 음식은 무엇일까요?버섯",
        "피카츄가 담배를 주우면서 하는 말은? 피까",
        "모든 사람을 일어나게 하는 숫자는? 다섯",
        "이 세상에서 가장 멋진 사람은? 너",
        "소나무가 삐지면? 칫솔",
        "오리가 얼면? 언덕",
        "가장 비싼 새는? 백조",
        "항상 미안해하는 연예인은? 지성",
        "고등학생이 싫어하는 나무는? 야자나무",
        "정말 큰 학은? 대학",
        "딸기가 도망가면? 딸기잼",
        "세상에서 가장 달콤한 술은? 입술",
        
    ]
    return random.choice(jokes)

def joke(update, context):
    update.message.reply_text(get_random_joke())

def random_number_generator(update, context):
    try:
        if len(context.args) != 2:
            raise ValueError("Invalid command format. Use /random_number <min> <max>")

        min_value, max_value = map(int, context.args)
        if min_value >= max_value:
            raise ValueError("Minimum value must be less than the maximum value")

        random_number = random.randint(min_value, max_value)
        update.message.reply_text(f"Random number: {random_number}")
    except ValueError as e:
        update.message.reply_text(str(e))

def play_rps(update, context):
    if not context.args:
        update.message.reply_text("Please choose one: /rps rock|paper|scissors")
        return

    user_choice = context.args[0].lower()
    bot_choice = random.choice(['rock', 'paper', 'scissors'])

    result = determine_winner(user_choice, bot_choice)

    reply_message = f"You chose {user_choice}, and the bot chose {bot_choice}.\nResult: {result}"
    update.message.reply_text(reply_message)

def determine_winner(player_choice, bot_choice):
    if player_choice == bot_choice:
        return "It's a tie!"
    elif (
        (player_choice == 'rock' and bot_choice == 'scissors') or
        (player_choice == 'scissors' and bot_choice == 'paper') or
        (player_choice == 'paper' and bot_choice == 'rock')
    ):
        return "You win!"
    else:
        return "You lose!"

def unknown(update, context):
    update.message.reply_text(f"Sorry '{update.message.text}' is not a valid command")

def unknown_text(update, context):
    update.message.reply_text(f"Sorry, I can't recognize your input: '{update.message.text}'")


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('links', links))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('git', git_url))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('joke', joke))
updater.dispatcher.add_handler(CommandHandler('rand', random_number_generator))
updater.dispatcher.add_handler(CommandHandler('rps', play_rps))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(Filters.command, unknown))
updater.start_polling()
