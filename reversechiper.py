#reversechiper.py
#https://nostarch.com/crackingcodes (BSD Licensed)

# varible with the message to be encoded
#message = 'Three can keep a secret, if two of them are dead.'
#takes in an user inputed message
message = input('Enter message: ')
#Varible to store the reversed message
translated = ''

#find the length of the message
i = len(message) - 1

#loops through message backwards and stores it in the translated var
while i >= 0:
    translated = translated + message[i]
    i = i - 1

#prints out the message sotred in traslated var
print(translated)