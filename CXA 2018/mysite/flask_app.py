from flask import Flask, render_template, request, redirect, url_for, session
import base64
from _keyword import *
from snopes import *
from news_check import *
from _twitter import *
from twitter.error import TwitterError

app = Flask(__name__, static_url_path='')
app.config["DEBUG"] = True

twitter = init_twitter()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=["GET","POST"])
def show_results():
    if request.method == "GET":
        return redirect(url_for('index'))
    else:
        userinput = request.form["userphrase"]
        twitter_username = request.form['username']

        if twitter_username != '':
            try:
                posts = calc_post_data(twitter, twitter_username)
                return render_template('twitter.html', posts=posts, username=twitter_username)
            except TwitterError:
                return render_template('error.html', message='Username not found')

        keywords = TexTract(userinput).keyword()

        rating, metadata = get_rating(keywords)

        title, index = verify_snopes(keywords)
        if title == '':
            final = rating
        else:
            metadata = [[title, 'https://www.snopes.com/', 'https://usercontent1.hubstatic.com/13942932_f520.jpg','']] + metadata
            final = round((rating * 0.3 + index * 0.7)*10)/10
        return render_template('result.html', searchtext=userinput, rating=final, metadata=metadata)

@app.route('/loading/<encodedtext>', methods=["GET"])
def test2(encodedtext):
    mytext = base64.b64decode(encodedtext)
    mylist = [2,[[1,2,3],[4,5,6],[7,8,9]]]
    return render_template('result.html', searchtext = mytext, biglist = mylist)
