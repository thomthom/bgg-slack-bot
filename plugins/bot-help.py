from slackbot.bot import respond_to,listen_to,default_reply
from boardgamegeek import BoardGameGeek

import re

bgg = BoardGameGeek()

@respond_to('help', re.IGNORECASE)
@listen_to('help bgg', re.IGNORECASE)
def help(message):
        print('got command help')
	help_message = "The following commands are available from the game bot: \n\n" +\
		"\t\tgame <game title> -- Search for information about a game. \n"
	message.send(help_message)

