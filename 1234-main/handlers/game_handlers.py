from lexicon.lexicon import lexicon
from keyboards.keyboards import game_kb, yes_no_kb
import service.service as game_funcs
from service.stats import update_stats

def register_game_handlers(bot):
    @bot.message_handler(func=lambda message: message.text == lexicon.yes_button)
    def yes_register_game_handlers(message):
            bot.send_message(
                chat_id=message.chat.id,
                text=lexicon.yes,
                reply_markup=None
            )
    @bot.message_handler(func=lambda message: message.text == lexicon.no_button)
    def no_game_handler(message):
        bot.send_message(
             chat_id=message.chat.id,
             text=lexicon.not_went
        )
    @bot.message_handler(func=lambda message: message.text in (lexicon.paper, lexicon.rock, lexicon.scissors))
    def process_game_button(message):

        bot_choice = game_funcs.get_bot_choice()
        bot.send_message(
            chat_id=message.chat.id,
            text="Я выбрал " + bot_choice
        )

        winner = game_funcs.get_winner(bot_choice, message.text)
        update_stats(message.chat.id, winner)
        bot.send_message(
            chat_id=message.chat.id,
            text=winner,
            reply_markup=yes_no_kb
        )