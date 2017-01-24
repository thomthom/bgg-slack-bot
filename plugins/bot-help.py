from slackbot.bot import respond_to,listen_to,default_reply
from boardgamegeek import BoardGameGeek

import re
import sys

bgg = BoardGameGeek()

@respond_to('help', re.IGNORECASE)
@listen_to('\[\[help\]\]', re.IGNORECASE)
def help(message):
#        print('got command help')
#	print(message.__dict__)
#	b = message.body
#	print(b)
#	print(b['ts'])

	help_message = "The following commands are available from the game bot:\n\n" +\
		"*search* `game name`\n\t\tSearch for games called _game name_. Does not need to be exact.\n" +\
		"*game* `game title`\n\tGet information about _game title_. Must be the exact name of the game.\n" +\
		"*game* `BGG ID`\n\tGet information about the game with this _BGG ID_.\n\n" +\
		"*user* `BGG username`\n\tGet information on a BGG user.\n" +\
		"*coll* `BGG username`\n\tGet a list of the owned games for a user." +\
		""
	message.send(help_message)

