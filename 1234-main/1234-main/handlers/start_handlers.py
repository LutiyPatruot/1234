from lexicon.lexicon import lexicon
from keyboards.keyboards import yes_no_kb
from service.stats import scores, get_start_score

def register_start_handler(bot):
    @bot.message_handler(commands=["start"])
    def start_handler(message):
        print(1)
        chat_id=message.chat.id
        bot.send_message(
        chat_id=chat_id,
        text=lexicon.start,
        reply_markup=yes_no_kb
        )
        if chat_id not in scores:
            scores[chat_id] = get_start_score()
            print(scores)

def register_start_handler(bot):
    @bot.message_handler(commands=["help"])
    def start_handler(message):
        bot.send_message(
            chat_id=message.chat.id,
            text=lexicon.help,
            reply_markup=yes_no_kb
     )
    @bot.message_handler(commands=["stats"])
    def stats_handler(message):
            chat_id=message.chat.id
            stat_message = lexicon.stats.format_map(scores[chat_id])
            bot.send_message(
                chat_id=chat_id,
                text=lexicon.help,
                reply_markup=yes_no_kb
     )