from slackbot.bot import respond_to,listen_to,default_reply
from boardgamegeek import BoardGameGeek

import re

bgg = BoardGameGeek()

#@default_reply
#def my_default_hanlder(messsage):
#    print('got default handler')
#    message.reply('Im sorry, this bot does not understand you, please try the *help* command')

@respond_to('game (.*)')
@listen_to('\[\[game (.*)\]\]')
def game(message, something):
    print('got game request')
    message.reply('Getting information on *{}*'.format(something))
    bgg = BoardGameGeek()
    g = bgg.game(something)

    game_message = "\nTitle: " + g.name +\
	"\nID: " + g.id +\
	"\nDescription: " + g.description
    message.send(game_message)

