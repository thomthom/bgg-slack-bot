from slackbot.bot import respond_to,listen_to,default_reply
from boardgamegeek import BoardGameGeek

import re

bgg = BoardGameGeek()

#@default_reply
#def my_default_hanlder(messsage):
#    print('got default handler')
#    message.reply('Im sorry, this bot does not understand you, please try the *help* command')

@respond_to('help', re.IGNORECASE)
@listen_to('help bgg', re.IGNORECASE)
def help(message):
        print('got command help')
	help_message = "The following commands are available from the game bot: \n\n" +\
		"\t\tgame <game title> -- Search for information about a game. \n"
	message.send(help_message)

@respond_to('game (.*)')
def game(message, something):
    print('got game request')
    message.reply('Getting information on *{}*'.format(something))
    bgg = BoardGameGeek()
    g = bgg.game(something)

    game_message = "\nTitle: " + g.name +\
	"\nID: " + g.id +\
	"\nDescription: " + g.description
    message.send(game_message)

