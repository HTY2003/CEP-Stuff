import string

def removeLeadingTrailingPunct(word):
    if word == "":
        return ""
    else:
        if word[0] in string.punctuation:
            return removeLeadingTrailingPunct(word[1:])
        elif word[-1] in string.punctuation:
            return removeLeadingTrailingPunct(word[:-1])
        else:
            return word
    
print(removeLeadingTrailingPunct("?&veg-halo,,,"))


def addWord(d, word):
    if word in d:
        d[word] = d[word] + 1
    else:
        d[word] = 1


def total_words(hist):
    return sum(hist.values())


def different_words(hist):
    return len(hist)


def most_common(hist):
    freqList = []
    for k,v in freqWord.items():
        freqList.append((v,k))
    freqList.sort(reverse=True)
    for i in range(10):
        print(freqList[i][1],"\t", freqList[i][0])
    return freqList
        
freqWord = {}
with open("alice.txt") as infile:
    for row in infile:
        wordlist = row.strip().split(' ')
        if wordlist != [""]:
            for word in wordlist:
                word = word.strip() #remove \n
                word = word.lower() #convert to lowercase
                word = removeLeadingTrailingPunct(word)                
                if word != "":
                    if "-" in word:
                        for w in word.split("-"):
                            if w != "":
                                addWord(freqWord, removeLeadingTrailingPunct(w))
                    else:
                        addWord(freqWord, word)



print( 'Total number of words:', total_words(freqWord))
print( 'Number of different words:', different_words(freqWord))
print( 'The 10 most common words are:')
t = most_common(freqWord)
print(freqWord.get("`i")) #None - if found in entry, deduct 1m

    
    
    
    
    
