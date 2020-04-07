#Affine Cypher
#https://nostarch.com/crackingcodes (BSD Licensed)

import sys, pyperclip, cryptomath, random

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

def main():
    #myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believeing that it was human" -Alan Turing"""
    myMessage = """5QG9ol3La6QI93!xQxaia6faQL9QdaQG1!!axQARLa!!AuaRLQADQALQG93!xQxaGaAfaQ1QX3o1RQARL9Qda!AafaARuQLX1LQALQI1iQX3o1R"Q-5!1RQP36ARu"""
    myKey = 2894
    myMode = 'decrypt' #set to either encrypt or decrypt.
    
    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (myMode))
    
def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('Cipher is weak if KeyA is 1. Choose a different key.')
    
    if keyB == 0 and mode == 'encrypt':
        sys.exit('Cipher is weak if KeyB is 0. Choose a different key.')
        
    if keyA < 0 or keyB < 0 or keyB> len(SYMBOLS) -1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s' % (len(SYMBOLS) - 1))
    
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key. ' % (keyA, len(SYMBOLS)))
        
def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    cipherText = ''
    
    for symbol in message:
        if symbol in SYMBOLS:
            #Encrypt the symbol
            symbolIndex = SYMBOLS.find(symbol)
            cipherText += SYMBOLS[(symbolIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            cipherText += symbol #Append the symbol without encrypting
    return cipherText

def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plainText = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))
    
    for symbol in message:
        if symbol in SYMBOLS:
            #Decrypt the symbol
            symbolIndex = SYMBOLS.find(symbol)
            plainText += SYMBOLS[(symbolIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]     
        else:
            plainText += symbol #Append the symbol without decrypting.
    return plainText

def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB
        
        
#If affineChipher.py is run (Instead of imported as a module), call the main() function

if __name__ == "__main__":
    main()
    