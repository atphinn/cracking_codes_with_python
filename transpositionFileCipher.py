#Transposition Cipher test
#https://nostarch.com/crackingcodes (BSD Licensed)

import time, os, sys, Encrypt, transpositionDecrypt

def main():
    inputFileName = input('Please input the file name: ' )#'test.encrypted.txt'
    #BE CAREFUL!!! If a file with the outputFilename name already exists, this program will over write  that file
    outputFilename = 'test.txt'
    myKey = 10
    myMode = 'decrypt' #set to either encrypt or decrypt

    #If the input file does not exsist, the program terminates early
    if not os.path.exists(inputFileName):
        print("The files does not exsist Quitting..." % (inputFileNam))
        sys.exit()

    #if the output file already exsist, give the user a chance to quit:
    if os.path.exists(outputFilename):
        print('This will over write the file %s. (C)ontinue or (Q)uit?' %(outputFilename))
        response = input('> ')
        if not response.lower().startswith('c'):
            sys.exit()

    #read in the message from the input file:
    fileObj = open(inputFileName)
    content = fileObj.read()
    fileObj.close()

    print('%sing... ' % (myMode.title()))

    #Measure how long the encryption/decryption takes
    startTime = time.time()
    if myMode == 'encrypt':
        translated = Encrypt.encryptMessage(myKey, content)
    elif myMode == 'decrypt':
        translated = transpositionDecrypt.decryptMessage(myKey, content)
    totalTime = round(time.time() - startTime, 2)
    print('%sion time: %s seconds' % (myMode.title(), outputFilename))

    #Write out the transposition message to the out file

    outputFileObj = open(outputFilename, 'w')
    outputFileObj.write(translated)
    outputFileObj.close()

    print('Done %sing %s (%s characters). ' % (myMode, inputFileName, len(content)))
    print('%sed file is %s.' % (myMode.title(), outputFilename))


    #if transpositioCipherFile.py is run (instead of inported as a module) call the main() function

if __name__ == '__main__':
    main()