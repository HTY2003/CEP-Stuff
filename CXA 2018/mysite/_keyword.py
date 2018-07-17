from nltk.corpus import brown, stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from collections import Counter
import operator
from math import log

stopword = stopwords.words('english')
word = lambda x: list(WordNetLemmatizer().lemmatize(word, pos='v') for word in word_tokenize(x.replace('[^\w\s]','').lower()) if word not in stopword and len(word) > 1)
brownbase = Counter(i.lower() for i in brown.words())
brownlen = len(brown.words())

class TexTract:
    def __init__(self, text):
        self.word = word(str(text))
        print(self.word)
        self.frequency = dict(Counter(self.word))
        self.tfidf = {}
        self.keywords = []
        for words in self.frequency.keys():
            print(words)
            self.tfidf[words] = self.frequency[words] * log((brownlen+len(self.word)) / (brownbase[words]+self.frequency[words]))
        self.tfidf = sorted(self.tfidf.items(), key=operator.itemgetter(1))
        print(self.tfidf)
        if len(self.tfidf) > 10: self.temp = list(item[0] for item in self.tfidf[round(len(self.word)*0.40):])
        elif len(self.tfidf) > 6: self.temp = list(item[0] for item in self.tfidf[round(len(self.word)*0.20):])
        else: self.temp = list(item[0] for item in self.tfidf)
        for wor in self.word:
            if wor in self.temp and wor not in self.keywords: self.keywords.append(wor)
    def __str__(self): return str(self.keywords)
    def keyword(self): return self.keywords
print(TexTract("Finally, Hilary Clinton and ‘President’ Donald Trump end up [married] to each other!"))
