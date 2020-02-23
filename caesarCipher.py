#Caesar Cihpher
#https://nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

#This is the string to be encrypted/decrypted
message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'

#The encryption / Decryption key

key = 13

#Wheather the program  encrypts or decrypts.
mode = 'decrypt' #set to either encrypt or decrypt

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
