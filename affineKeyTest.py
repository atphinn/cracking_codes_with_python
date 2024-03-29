#This program proves that tbe keyspace of the affine cipher is limited to less that len(SYMBOLS) ^ 2.

import affineCypher, cryptomath

message = 'Make things as simple as possible, but not simpler.'

for keyA in range(2,80):
    key = keyA * len(affineCypher.SYMBOLS) + 1
    
    if cryptomath.gcd(keyA, len(affineCypher.SYMBOLS)) == 1:
        print(keyA, affineCypher.encryptMessage(key, message))