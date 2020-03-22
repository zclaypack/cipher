'''
Cipher
Python 3.7.4
An encryption tool made in Python, based on ROT13
'''

#Vriables
alphabet = "abcdefghijklmnopqrstuvwxyz"

#Encrypt Function
def encrypt(message, key):
    translatedMessage = []
    for i in message:
        location = alphabet.index(i)
        newLocation = int(location) + int(key)
        if newLocation >= (len(alphabet)):
            finalLocation = newLocation%(len(alphabet))
            encryptedLetter = alphabet[finalLocation]
            translatedMessage.append(encryptedLetter)
        else:
            encryptedLetter = alphabet[newLocation]
            translatedMessage.append(encryptedLetter)
    return(translatedMessage)

#Decrypt Function
def decrypt(message, key):
    translatedMessage = []
    for i in message:
        location = alphabet.index(i)
        if int(key) <= (len(alphabet)):
            newLocation = int(location) - int(key)
            if newLocation < 0:
                finalLocation = int((len(alphabet))) + int(newLocation)
                encryptedLetter = alphabet[finalLocation]
                translatedMessage.append(encryptedLetter)
            else:
                encryptedLetter = alphabet[newLocation]
                translatedMessage.append(encryptedLetter)
        else:
            aNewLocation = int(key)%(len(alphabet))
            finalLocation = int(location) - aNewLocation
            encryptedLetter = alphabet[finalLocation]
            translatedMessage.append(encryptedLetter)
    return(translatedMessage)