'''
Cipher
Python 3.7.4
An encryption tool made in Python, based on ROT13
'''

import functions

#User Interface/Inputs *Welcome Statements*
userChoice = input("Would you like to Encrpyt or Decrypt a message (E or D): ")
userChoice = userChoice.lower()

#User Pick Encryption
if userChoice == "e":
    userMessage = input("Enter the message you would like to encrypt: ")
    userMessage = userMessage.lower()
    userKey = input("Enter the key you would like to encrypt with: ")
    encryptedMessage = functions.encrypt(userMessage, userKey)
    print("Your encrypted message using the Key #{} is: ".format(userKey))
    print(*encryptedMessage, sep='')

#User Pick Decryption
elif userChoice == "d":
    userMessage = input("Enter the message you would like to decrypt: ")
    userMessage = userMessage.lower()
    userKey = input("Enter the key you would like to decrypt with: ")
    decryptedMessage = functions.decrypt(userMessage, userKey)
    print("Your decrypted message using the Key #{} is: ".format(userKey))
    print(*decryptedMessage, sep='')

#Error
else:
    print("Error! You did not enter the D or E key! Program Terminated :(")
    exit()


    
