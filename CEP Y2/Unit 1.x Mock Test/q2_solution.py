def odds(lst):
    retlst = []
    i = 0
    for item in lst:
        if i % 2 == 0:
            retlst.append(item)
        i = i + 1
    return retlst
        

print(odds([]))#[]
print(odds(['a']))#['a']
print(odds(['a','b']))#['a']
print(odds(['a','b','c']))#['a','c']
print(odds(['a','b','c','d','e','f','g','h'])) #['a','c','e','g']


def odds_r(lst):
    if lst == []:
        return []
    else:
        return list(lst[0]) + odds(lst[2:])
    
print(odds_r([]))#[]
print(odds_r(['a']))#['a']
print(odds_r(['a','b']))#['a']
print(odds_r(['a','b','c']))#['a','c']
print(odds_r(['a','b','c','d','e','f','g','h'])) #['a','c','e','g']


def evens(lst):
    return odds(lst[1:])


print(evens([]))#[]
print(evens (['a']))#[]
print(evens (['a','b']))#['b']
print(evens (['a','b','c']))#['b']
print(evens (['a','b','c','d','e','f','g','h']))#['b','d','f','h']


def is_palindrome(text):
    i = 0
    for i in range(len(text)//2):
        if text[i].lower() != text[-i-1].lower():
            return False
    return True

print(is_palindrome("Able was I ere I saw Elba")) #True
print(is_palindrome("NeverOddOrEven")) #True
print(is_palindrome("Hannah"))#True
print(is_palindrome("ac"))#False


def is_palindrome_r(text):
    if len(text) == 0 or len(text) == 1:
        return True
    elif text[0].lower() != text[-1].lower():
        return False    
    else:
        return is_palindrome_r(text[1:-1])

print(is_palindrome_r("Able was I ere I saw Elba")) #True
print(is_palindrome_r("NeverOddOrEven")) #True
print(is_palindrome_r("Hannah"))#True
print(is_palindrome_r("ac"))#False



