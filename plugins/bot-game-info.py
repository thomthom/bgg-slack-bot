from slackbot.bot import respond_to,listen_to
from boardgamegeek import BoardGameGeek

# Import regex lib
import re
# Import json lib
import json

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

    message.send_webapi(game_message, '', True)

def format_search_message(game):
    if game is None:
        return

    msg = "\n%s (%s) <https://boardgamegeek.com/boardgame/%s|%s>" % (
        game.name,
	game.yearpublished,
        game.id,
        game.id
        )

    return msg

@respond_to('game (.*)')
@listen_to('\[\[game (.*)\]\]')
def game_search(message, gametext):
	print('got game request for %s' % gametext)

	if unicode(gametext, 'utf-8').isnumeric():
		message.reply('Getting game info for ID *{}*'.format(gametext))
		game = bgg.game(None, gametext)
	else:
                message.reply('Getting game info for *{}*'.format(gametext))
                game = bgg.game(gametext, None)

        if game == None:
                message.reply('No information found for *{}*'.format(gametext))
                return

    	attachments = [
    	{
        	'fallback': 'Information on ' + game.name,
        	'author_name': game.name + ' (' + str(game.yearpublished) + ')',
        	'author_link': 'https://boardgamegeek.com/boardgame/' + str(game.id),
		'author_icon': game.thumbnail,
        	'text': game.description,
        	'color': 'good',
#           	'image_url': game.image,
        	'thumb_url': game.thumbnail,
		'fields' : [
                {
                        'title' : 'BGG ID',
                        'value' : game.id,
                        'short' : True
                },
		{
			'title' : 'Player Count',
			'value' : str(game.minplayers) + '-' + str(game.maxplayers),
			'short' : True
		},
		{
                        'title' : 'Playing Time',
                        'value' : game.playingtime,
                        'short' : True

		},
		{
                        'title' : 'Designer(s)',
                        'value' : ', '.join(game.designers),
                        'short' : True
		},
		{
                        'title' : 'Categories',
                        'value' : ', '.join(game.categories),
                        'short' : True
		},
                {
                        'title' : 'Mechanics',
                        'value' : ', '.join(game.mechanics),
                        'short' : True
                }]

    	}]
    	message.send_webapi('', json.dumps(attachments))

