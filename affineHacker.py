#Affine Cipher Hacker
#https://nostarch.com/crackingcodes (BSD Licensed)

import pyperclip, affineCypher, detectingEnglish, cryptomath

SILENT_MODE = False

def main():
    myMessage = """"5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafARuQLX1LQALQI1iQX3o1RN"Q-5!1RQP36ARu"""

    hackedMessage = hackAffine(myMessage)

    if hackedMessage != None:
        #The plaintext is displayed on the screen. For the convenice of the user, we copy the text of the code to the clip board
        print('Copying hacked message to clipboard: ')
        print(hackedMessage)
        pyperclip.copy(hackedMessage)
    else:
        print('Failed to hack encryption')

def hackAffine(message):
    print('Hacking....')

    #Python programs can be stopped at any time by pressing ctrl-C(Windows) or Ctrl - D (MacOs an Linux)

    print('(Press Ctrl-C or Ctrl-D to quit at any time.) ')

    #Brute force by looping through every possible key.
    for key in range(len(affineCypher.SYMBOLS) ** 2):
        keyA = affineCypher.getKeyParts(key)[0]
        if cryptomath.gcd(keyA, len(affineCypher.SYMBOLS)) != 1:
            continue

        decryptedText = affineCypher.decryptMessage(key, message)
        if not SILENT_MODE:
            print('Tried Key %s...(%s)' % (key, decryptedText[:40]))

        if detectingEnglish.isEnglish(decryptedText):
            #Check with the user id the decrypted key has been found.
            print()
            print('Possible encryption hack: ')
            print('Key: %s' % (key))
            print('Decrypted message: ' + decryptedText[:200])
            print()
            print('Enter D for done, or just press Enter to continue hacking: ')

            response = input('> ')

            if response.strip().upper().startswith('D'):
                return decryptedText
    return None

#If affineHacker.py is run (instead of imported as a module), call the main() function:

if __name__ == '__main__':
    main()

        
