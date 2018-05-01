def letterToIndex(ch):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    idx = alphabet.find(ch)
    if idx < 0:
        print ("error: letter not in the alphabet", ch)
    return idx

def indexToLetter(idx):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    if idx > 25:
        print ('error: ', idx, ' is too large')
        letter = ''
    elif idx < 0:
        print ('error: ', idx, ' is less than 0')
        letter = ''
    else:
        letter = alphabet[idx]
    return letter

def scramble2Encrypt(plainText):
    '''
    Scramble the plaintext according to odd or even characters
    The resultant ciphertext is the concatenation of the odd character string
    and the even character string.
    Returns the scrambled ciphertext.
    '''
    evenChars = ""
    oddChars = ""
    charCount = 0
    for ch in plainText:
        if charCount % 2 == 0:
            evenChars = evenChars + ch
        else:
            oddChars = oddChars + ch
        charCount = charCount + 1
    cipherText = oddChars + evenChars
    return cipherText

def scramble2Decrypt(cipherText):
    '''
    Descramble the cipherText.
    Split the ciphertext to half
    First half consist of odd characters in the original text
    Second half consist of even characters in original text
    We may have one more character in the
    even character string than we do in the odd character string.
    We compare the lengths of the two strings. If the odd-numbered
    character string is shorter than the even, we simply concatenate
    the last character from the even string onto the plaintext.
    Returns the unscrambled plaintext.

    '''
    halfLength = len(cipherText) // 2
    oddChars = cipherText[:halfLength]
    evenChars = cipherText[halfLength:]
    plainText = ""

    for i in range(halfLength):
        plainText = plainText + evenChars[i]
        plainText = plainText + oddChars[i]

    if len(oddChars) < len(evenChars):
        plainText = plainText + evenChars[-1]

    return plainText

def encryptMessage():
    msg = input('Enter a message to encrypt: ')
    cipherText = scramble2Encrypt(msg)
    print('The encrypted message is: ', cipherText)

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

def vigenereIndex(keyLetter,plainTextLetter):
    keyIndex = letterToIndex(keyLetter)
    ptIndex = letterToIndex(plainTextLetter)
    newIdx = (ptIndex + keyIndex) % 26
    return indexToLetter(newIdx)

def encryptVigenere(key,plainText):
    cipherText = ""
    keyLen = len(key)
    for i in range(len(plainText)):
        ch = plainText[i]
        if ch == ' ':
            cipherText = cipherText + ch
        else:
            cipherText = cipherText + vigenereIndex(key[i%keyLen],ch)
    return cipherText

def decryptVigenere(key, cipherText):
    '''
    Given the key and cipherText, work backwards to find the plaintext
    '''
    plaintext = ""
    keyLen = len(key)
    for item in range(len(cipherText)):
        ch = cipherText[item]
        if ch == " ":
            plaintext += " "
        else:
            for i in range(26):
                if (letterToIndex(key[item%keyLen]) + i) % 26 == letterToIndex(ch):
                    plaintext += indexToLetter(i)

    return plaintext

print(bruteforceCaesar("VEZNUT".lower()))
print(decryptVigenere('PROGRAMMINGLANGUAGE'.lower(), 'EPHNFNTMANJPSVMHPNMAFGUGHKFPNZPMCNUSODTJQUUEDQIQGMIYONYTSIRPRPUEUVTYTGAOZIIECKKNZTQEXNIP'.lower()))
print(bruteforceCaesar("JCQTLQVOJTWKA".lower()))
print(decryptVigenere('AWESOME'.lower(), "WdijsMperidozhOhinsxGoitmhurgoxmrqrtoggaqxocilvqvtkfmwxhajmftagoiqwabswavwrrytqvw".lower()))
print(encodeCaesar("nestedciphers", 15))
print(encryptVigenere('REALLYDIFFICULT'.lower(), encodeCaesar("mostofyouwontbeabletodecipherthisbecauseofhowharditis".lower(), 19)))
print(scramble2Encrypt("anunknowncipher?"))
