#Transposition Cipher test
#https://nostarch.com/crackingcodes (BSD Licensed)

import random, sys, Encrypt, transpositionDecrypt


def main():
    random.seed(42) #set the random "seed" to a staic value

    for i in range(20):
        #Generate random messages to test. The message will have a random length:
        message = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' * random.randrange(4, 40)

        #Convert the message string to a list to shuffle
        message = list(message)
        random.shuffle(message)
        message = ''.join(message) #convert list back to string
        print('Test #%s: "%s..."' % (i + 1, message[:50]))

        #Check all possible keys for each message:
        for key in range(1, int(len(message)/2)):
            encrypted = Encrypt.encryptMessage(key, message)
            decrypted = transpositionDecrypt.decryptMessage(key, encrypted)

            #If the decryption doesnt match the original message display an error message and quit
            if message != decrypted:
                print('Mismatch with key %s and message %s.' % (key, message))
                print('Decrypted as: ' + decrypted)
                sys.exit()

    print('[+] Transposition cipher text passed.')

    #if tranpositionTest.py is run (instead of imported as a module ) call the main function

    if __name__ == '__main__':
        main()


