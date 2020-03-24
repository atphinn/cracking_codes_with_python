#Transposition Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import pyperclip, detectingEnglish, transpositionDecrypt

def main():
    #You might want to copy & paste this from the source code 
    
    myMessage = """AaKoosoeDe5 b5sn ma reno ora'lhlrrceey e  enlh na  indeit n uhoretrm au ieu v er Ne2 gmanw,forwnlbsya apor tE.no euarisfatt  e mealefedhsppmgAnlnoe(c -or)alat r lw o eb  nglom,Ain one dtes ilhetcdba. t tg eturmudg,tfl1e1 v  nitiaicynhrCsaemie-sp ncgHt nie cetrgmnoa yc r,ieaa  toesa- e a0m82e1w shcnth  ekh gaecnpeutaaieetgn iodhso d ro hAe snrsfcegrt NCsLc b17m8aEheideikfr aBercaeu thllnrshicwsg etriebruaisss  d iorr."""
    hackedMessage = hackTransposition(myMessage)
     
    if hackedMessage == None:
         print('Failed to hack encryption, ')
    else:
        print('Copying hacked message to clipboard: ')
        print(hackedMessage)
        pyperclip(hackedMessage)
        
def hackTransposition(message):
    print('Hacking....')
    
    #Python programs can be stopped any time by pressing ctr + D (Linux and Mac) or ctr + C (Windows)
    
    print('(Press Ctrl + C (On windows) of Ctrl + D (On Mac OS or Linux) to quit anytime.)')
    #Brute force by looping through every key
    
    for key in range(1, len(message)):
        print('Trying ket #%s...' % (key))
        
        decryptedText = transpositionDecrypt.decryptMessage(key, message)
        
        if detectingEnglish.isEnglish(decryptedText):
            #Ask user if this is the correct decryption
            
            print()
            print('Possible ecryption hack: ')
            print('Key %s: %s' % (key,decryptedText[:100]))
            print()
            print('Enter D if done, anything else to continue hacking: ')
            
            response = input('> ')
            
            if response.strip().upper().startswith('D'):
                return decryptedText
            
    return None


if __name__ == '__main__':
    main() 