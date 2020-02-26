#Caesar Chipher Hacker
#https://nostarch.com/crackingcodes (BSD Licensed)

#message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
message = input('Enter encrypted message: ')
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.`~@#$%^&*()+-=[]{}|;:<>,/'

#loop through every possible key

for key in range(len(SYMBOLS)):
    #It is important to set translated to the blank string so that the previous iteration's value for translated is cleared:
    translated = ''

    #Is the same as the caesar chipher program, Loop through each symbol in the message
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            #Handle wrap arround
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

                #Append decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            #Append with out encrypting/decrypting:
            translated = translated + symbol

    #Display every possible decryption
    print('Keys #%s: %s\n\n' % (key, translated))


