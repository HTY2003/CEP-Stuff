import twitter
import re
from news_check import *
from _keyword import *

def init_twitter():
	api = twitter.Api(consumer_key='64qCEhrYD571ViT6bKzD3c2Yq',
					  consumer_secret='8fzwyatnPQ6S6LrwehW2eQXk0w8FruttpzXdFKwjFS0VHD1eCj',
					  access_token_key='1016311172591640576-5ajAPIBzHJKKQB31FBGo7NhGn9eEdo',
					  access_token_secret='deDxrXOEDXSSEAtoXk6c6D9xdTxNQVnzQ8gfeePvuwMKZ',
					  tweet_mode='extended')
	return api

def calc_post_data(api, username):
	posts = api.GetUserTimeline(screen_name=username, count=7)
	posts = [p.full_text for p in posts]
	posts_old = posts
	posts = [p.lower() for p in posts]
	posts = [re.sub(r'^https?:\/\/.*[\r\n]*', '', p, flags=re.MULTILINE) for p in posts]

	posts_new = []
	for p in posts:
		_p = ''
		for w in p.split(' '):
			if 't.co/' not in w:
				_p += w + ' '

		for c in _p:
			if c not in '0123456789abcdefghijklmnopqrstuvwxyz ':
				_p = _p.replace(c, ' ')
		posts_new.append(_p)
	posts = posts_new

	print(posts)
	data = []
	for idx, p in enumerate(posts):
		keywords = TexTract(p).keyword()
		print(keywords)
		rating, _ = get_rating(keywords)
		print('rating is: ' + str(rating))
		data.append((posts_old[idx], rating))
	return data
