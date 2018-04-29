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


print(scramble2Encrypt('baba black sheep'))
print(scramble2Decrypt('aabaksepbb lc he'))
print(scramble2Decrypt(scramble2Encrypt("hello")))


