from slackbot.bot import respond_to,listen_to,default_reply
from boardgamegeek import BoardGameGeek

import re
import sys

bgg = BoardGameGeek()

@respond_to('help', re.IGNORECASE)
@listen_to('[[help]]', re.IGNORECASE)
def help(message):
        print('got command help')
	help_message = "The following commands are available from the game bot:\n\n" +\
		"\t*search* `text`\t\t\tSearch for information on `text`.\n" +\
		"\t*game* `game title`\tGet information about `game title`. Must be the exact name of the game.\n" +\
		"\t*game* `BGG ID`\t\t\tGet information about the game with this `BGG ID`.\n\n" +\
		""
	message.send(help_message)

