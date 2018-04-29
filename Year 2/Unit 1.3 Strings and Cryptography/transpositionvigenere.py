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
    #pass

def encryptMessage():
    msg = input('Enter a message to encrypt: ')
    cipherText = scramble2Encrypt(msg)
    print('The encrypted message is: ', cipherText)


print(scramble2Encrypt('baba black sheep'))
print(scramble2Decrypt('aabaksepbb lc he'))
print(scramble2Decrypt(scramble2Encrypt("hello")))


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

def vigenereIndex(keyLetter,plainTextLetter):
    keyIndex = letterToIndex(keyLetter)
    ptIndex = letterToIndex(plainTextLetter)
    newIdx = (ptIndex + keyIndex) % 26
    return indexToLetter(newIdx)

print(vigenereIndex('d', 't')) 
print(vigenereIndex('a', 'h'))
print(vigenereIndex('v', 'e'))
print(vigenereIndex('i', 'e'))
print(vigenereIndex('n', 'a'))
print(vigenereIndex('c', 'g'))
print(vigenereIndex('i', 'l'))
print(vigenereIndex('d', 'e'))
print(vigenereIndex('a', 'h'))
print(vigenereIndex('v', 'a'))
print(vigenereIndex('i', 's'))
print(vigenereIndex('n', 'l'))
print(vigenereIndex('c', 'a'))
print(vigenereIndex('i', 'n'))
print(vigenereIndex('d', 'd'))
print(vigenereIndex('a', 'e'))
print(vigenereIndex('v', 'd'))

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

print(encryptVigenere("davinci", "theeaglehaslanded")) #whzmnithhvaycvgey
print(encryptVigenere("turing", "theeaglehaslanded")) #mbvmnmeyyifrthumq


def decryptVigenere(key, cipherText):
    '''
    Given the key and cipherText, work backwards to find the plaintext
    '''
    #pass

print(decryptVigenere('davinci', 'whzmnithhvaycvgey')) #expected output: theeaglehaslanded
print(decryptVigenere('turing', 'mbvmnmeyyifrthumq')) #expected output: theeaglehaslanded
