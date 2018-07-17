import os

def get_falseness_index(string):
    if string == 'True': return 5
    if string == 'Mostly True': return 4
    if string == 'Mostly False': return 2
    if string == 'False': return 1
    return 3

def get_article_data():
    data = []
    for i in os.listdir('parsed/'):
        with open('parsed/' + i) as f:
            raw = f.read().split('\n')
            title = raw[0]
            rating = raw[1]
            content = raw[2]
            data.append((title, rating, content))
    return data

def relevance_index(content, keywords):
    occurences = [content.lower().split(' ').count(k) for k in keywords]
    occurences = list(filter(lambda x: x > 0, occurences))

    index = (len(occurences)/len(keywords))**2 * sum(occurences)**0.5
    if index < 0.1: return None
    return index

def verify_snopes(keywords):
    article_data = get_article_data()
    data = []
    for d in article_data:
        index = relevance_index(d[0], keywords)
        if index == None:
            continue
        data.append((d[0], d[1], d[2], index))

    if data == []:
        return '', 3

    result = sorted(data, key=lambda x: x[3], reverse=True)[0]
    title = result[0]
    rating = result[1]
    return title, get_falseness_index(rating)
