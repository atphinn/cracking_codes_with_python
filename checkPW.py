print('Enter your password: ')
typedPassword = input()
if typedPassword == 'swordfish ':
    print('[+] saccess granted!!')
elif typedPassword == 'mary':
    print('Hint: The password maybe a fish!')
elif typedPassword == '12345':
    print('That is a really obvious password')
else:
    print('[-] access denied!!')
print('done')