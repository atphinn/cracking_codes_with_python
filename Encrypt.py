#Transposition Cipher Encryption
#https://nostarch.com/crackingcodes (BSD Licensed)

import pyperclip

def main():
    #myMessage = input('Enter a message: ')#Common sense is not so common.'
    myMessage = 'Common sense is not so common.'
    # myKey = int(input('Enter a key: ')) #8
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    #Print the encrypted string in ciphertext to the screen with a  ("pipe" character) after it in case there are spaces at the end of the encrypted message:
    print(ciphertext + '|')

    #Copy the encrypted string in ciphertet to the clipboard:
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    #Each string in ciphertext represent a column in the grid

    ciphertext = [''] * key

    #loop through each column in ciphertext:

    for column in range(key):
        currentIndex = column

        #Keep looping until currentIndex goes pass the message length
        while currentIndex < len(message):
            #Place the character at currentIndex in message at the end of the current column in the cuphertext
            ciphertext[column] += message[currentIndex]

            #move current index over
            currentIndex += key

        #convert the ciphertext list into a single string value and return it
    return ''.join(ciphertext)

#If transpositionEncrypt.py in run (instead of inport module) cal the main() function

if __name__ == '__main__':
    main()