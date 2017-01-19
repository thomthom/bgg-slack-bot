from slackbot.bot import respond_to,listen_to
from boardgamegeek import BoardGameGeek

# Import regex lib
import re

bgg = BoardGameGeek()

@respond_to('search (.*)')
@listen_to('\[\[search (.*)\]\]')
def game_search(message, searchtext):
    print('got search request')
    message.reply('Searching for information on *{}*'.format(searchtext))
    games = bgg.search(searchtext)

    if len(games):
        # There are games
        if len(games) == 1:
            game_message = "\nOne game found:"
        else:
            game_message = "\nFound " + str(len(games)) + " games with that search: \n"
        
        for g in games:
            game_message += format_search_message(g)
    else:
        game_message = "\nNo games found for that search"

    message.send_webapi(game_message, None, True)

def format_search_message(game):
    if game is None:
        return

    msg = "\n%s ( <https://boardgamegeek.com/boardgame/%s|%s> )" % (
        game.name,
        game.id,
        game.id
        )

    return msg

