from slackbot.bot import respond_to,listen_to
from boardgamegeek import BoardGameGeek

import re, json

bgg = BoardGameGeek()

def jointwo(string1, string2, joinstr):
        return joinstr.join([x for x in (string2, string2) if x])

@respond_to('user (.*)')
@listen_to('\[\[user (.*)\]\]')
def user_info(message, username):
	print('Getting information on user ' + username)
	message.reply('Getting user information on *{}*'.format(username))

	user = bgg.user(username)

	if user == None:
		message.reply('No information found for user *{}*'.format(username))
		return

    	attachments = [{
        	'fallback' : 'User information on ' + username,
                'author_name': jointwo(user.firstname, user.lastname, ' ') + ' (' + user.name + ')',
                'author_link': 'https://boardgamegeek.com/user/' + user.name,
                'author_icon': 'https:' + user.avatarlink,
                'color': 'good',
                'thumb_url': 'https:' + user.avatarlink,
                'fields' : [
                {
                        'title' : 'Year Registered',
                        'value' : user.yearregistered,
                        'short' : True
                },
                {
                        'title' : 'Location',
                        'value' : jointwo(user.stateorprovince, user.country, ' / '),
                        'short' : True
                }]


	}]
    	message.send_webapi('', json.dumps(attachments))


@respond_to('coll (.*)')
@listen_to('\[\[coll (.*)\]\]')
def coll_info(message, username):
	print('Getting collection information for user ' + username)
        message.reply('Getting collection information for *{}*, this may take some time...'.format(username))

	coll = bgg.collection(username)

        if coll == None:
		message.reply('No collection information found for user *{}*'.format(username))
		return

	count = 0
	coll_list = ''
	for x in coll:
		if x.own == '1':
			if x.rating == None:
                                myrating = 'Not Rated'
			else:
                                myrating = "\tRating: " + str(x.rating)

			coll_list += "\n%s (<https://boardgamegeek.com/boardgame/%s|%s>) %s" % (
				x.name, 
				x.id, x.id, 
				myrating
			)
			count += 1

	if count > 0:
		coll_msg = "Found %s owned games for %s\n" % (count, username)
		coll_msg += coll_list
	else:
		coll_msg = "No owned games in the collection for " + username

	message.send_webapi(coll_msg, '', True)

