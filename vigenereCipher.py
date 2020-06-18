#Vigenere Cipher
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
    
    #myMessage = """Alan Mathison Turing was a British mathematician, logician, cryptanalyst, and computer scientist."""
    #myMessage = "Adiz Avtzqeci Tmzubb wsa m Pmilqev halpqavtakuoi, lgouqdaf, kdmktsvmztsl, izr xoexghzr kkusitaaf."
    myMessage = input('Enter message to de/encrypt: ')
    #myKey = 'ASIMOV'
    myKey = input('In put 6 string key: ')
    #myMode = 'decrypt' #set to either 'encrypt' or 'decrypt'
    myMode = input('''set to either 'encrypt' or 'decrypt: ''')
    
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    
    print()
    print('%sed message:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('The message hase been copied to the clipboard.')
    
    
def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = [] #Stores the encrypted/decrypted message string
    
    keyIndex = 0
    key = key.upper()
    
    for symbol in message: #Loop through each symbol in message
        num = LETTERS.find(symbol.upper())
        if num != -1: # -1 means symbol.upper() was not found in LETTERS
            if mode == 'encrypt':
                num += LETTERS.find(key[keyIndex]) #Add if encrypting.
            elif mode == 'decrypt':
                num -= LETTERS.find(key[keyIndex])#Subtract if decrypting
                
            num %= len(LETTERS) # Handle wrap around
            
            #Add the encrypted/decrypted symbol to the end of translated
            if symbol.isupper():
                translated.append(LETTERS[num])
            elif symbol.islower():
                translated.append(LETTERS[num].lower())
                
            keyIndex += 1 # Move to the next letter in the key.
            if keyIndex == len(key):
                keyIndex = 0
        else:
            #Append the symbol without encrypting/decrypting
            translated.append(symbol)
            
    return ''.join(translated)

# If vigenerecipher.py is run (instead of imported as a module), call the main fuction


if __name__ == '__main__':
    main()