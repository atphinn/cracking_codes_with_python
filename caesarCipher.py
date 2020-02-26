#Caesar Cihpher
#https://nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

#This is the string to be encrypted/decrypted
# message = 'This<is<my<secret<message/'
message = input('Enter message: ')
#The encryption / Decryption key

#key = 13
key = int(input('Enter key to use: '))
#Wheather the program  encrypts or decrypts.
#mode = 'decrypt' #set to either encrypt or decrypt
mode = input("Type Decrypt or encrypt: ")
#Every posible symbol that can be encrypted:

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()+-=[]{}|;:<>,/'

#Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    #Note: Only symbols in the SYMBOLS string can be encrypted/decrypted:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        #Perform encrypton/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        #handle Wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)


        translated = translated + SYMBOLS[translatedIndex]

    else:
        #Append the symbol without encrypting/decrypting:
        translated = translated + symbol

#Output the translated string:
print(translated)
pyperclip.copy(translated)
