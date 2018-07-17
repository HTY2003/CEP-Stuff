import json
import requests

def get_sentiment(text):
	data = str(text).encode('utf-8')
	r = requests.post(url='http://text-processing.com/api/sentiment/', data={u'text': data})
	return json.loads(r.text)['label']

def get_metadata(articles):
	return list(zip([a['title'] for a in articles],
			 [a['url'] for a in articles],
			 [a['urlToImage'] for a in articles],
			 [a['publishedAt'] for a in articles]))

def normalise_rating(d):
	values = d.values()
	def num_above(n, values):
		return len(list(filter(lambda v: v > n, values)))
	return {num_above(0.5, values) > len(values)/3*2: 5,
			len(values)/3*2 >= num_above(0.5, values) > len(values)/2: 4,
			len(values)/2 >= num_above(0.5, values) > len(values)/3: 2,
			len(values)/3 >= num_above(0.5, values): 1}[True]

def get_rating(keywords):
	query = 'https://newsapi.org/v2/everything?q={}&language=en&sortBy=relevancy&apiKey=e37f7131f1ef4a08bdb215dd4d3abaec'
	full = query.format('AND'.join(keywords))
	print(full)
	r = requests.get(query)
	frequency_map = dict.fromkeys(keywords)
	for k in frequency_map:
		frequency_map[k] = 0

	j = json.loads(r.text)
	try:
		articles = j['articles'][:11]
	except KeyError:
		return 3, []
	for a in articles:
		for k in keywords:
			title = ''
			description = ''
			try:
				title = a['title'].lower()
				description = a['description'].lower()
			except AttributeError:
				pass
			if k in title + description:
				frequency_map[k] += 1

	for k in frequency_map:
		if len(articles) != 0:
			frequency_map[k] /= len(articles)

	return normalise_rating(frequency_map), get_metadata(articles)
