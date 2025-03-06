from lexicon.lexicon import lexicon

def get_start_score():
    return{
        'game': 0,
        'wins': 0,
        'losses': 0,
        'nobody_wins': 0
    }

def update_stats(chat_id, result):
    scores[chat_id]['games'] += 1
    if result == lexicon.player_winner:
        scores[chat_id]['wins'] += 1
    elif result == lexicon.bot_winner:
        scores[chat_id]['losses'] += 1
    else:
        scores[chat_id]['nobody_wins'] += 1
    print(scores)
scores = {}
