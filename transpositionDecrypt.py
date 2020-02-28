#Transposition Cipher Dencryption
#https://nostarch.com/crackingcodes (BSD Licensed)


import math, pyperclip

def main():
    # myMessage = "Cenoonommstmme oo snnio. s s c"
    myMessage = input('Enter in devrypted message: ')
    # myKey = 8
    myKey = int(input('Enter in key: '))
    plaintext = decryptMessage(myKey, myMessage)

    #print with a | (called "pipe" character) after it in case there are spaces at the end of the decrypted message

    print(plaintext + "|")

    pyperclip.copy(plaintext)

def decryptMessage(key, message):
    #The transposition decrypt function will simulate the "columns" and "rows" of the grid  that the plain text is written on by using a list of strings. first we need to calculate a few values, The number of columns in our transposition grid

    numOfColumns = int(math.ceil(len(message)/ float(key)))

    #The number of rows in our grid

    numOfRows = key

    #the number of the shaded boxes  in the last column of the grid

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    #Each string in plaintext represents a column in the grid

    plainText = [''] * numOfColumns

    #The column and row varibles point to where in the grid the next character in the encrypted message will go.

    column = 0
    row = 0

    for symbol in message:
        plainText[column] += symbol
        column += 1 #Point to the next column

        #if there are no more columns or we are at a shaded box go back to the first column and the next row:

        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1
    return ''.join(plainText)

#if transposition.py is run instead of imported module call the main() function

if __name__ == '__main__':
    main()
