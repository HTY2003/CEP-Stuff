def letterToIndex(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    idx = alphabet.find(letter)
    #print(idx)
    if idx < 0:
        return "error: letter not in alphabet"
    return idx

def indexToLetter(idx):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if idx > 25:
        return "error: idx too large"
    elif idx < 0:
        return "error: idx too small"
    else:
        letter = alphabet[idx]
    return letter

def decodeCaesar(ct, key):
    '''
    Given the ciphertext, "ct", and the "key" to shift the alphabets by, this
    function will return the decoded message accordingly.
    '''
    pt = ""
    for letter in ct:
        if letter != " ":
            pl = indexToLetter((letterToIndex(letter) + key)%26)
            pt = pt + pl
        else:
            pt = pt + ' '
    return pt

def bruteforceCaesar(ct):
    '''
    bruteforceCaesar prints out all 26 different possible caesar shifts
    based on the ciphertext, "ct"
    '''
    for i in range(26):
        print("key-",i," ",decodeCaesar(ct, i))

def encodeCaesar(pt, key):
    '''
    Given plaintext, "pt", and the "key" to shift the alphabets by,
    this function will return the encoded message accordingly.
    '''
    ct = ""
    for letter in pt:
        if letter != " ":
            cl = indexToLetter((letterToIndex(letter) - key) % 26)
            ct = ct + cl
        else:
            ct = ct + " "
    return(ct)
     
bruteforceCaesar("cebtenzzvat vf yvxr xvpxvat lbhefrys va gur snpr fbbare be yngre lbhe abfr jvyy oyrrq")
print(decodeCaesar(encodeCaesar("the eagle has landed", 1), 1))
