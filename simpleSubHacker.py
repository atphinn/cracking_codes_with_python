#Simple Substitution Cipher Hacker
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import os, re, copy, pyperclip, simpleSubCipher, wordPatterns, makeWordPatterns





LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
nonLettersOrSpacePattern = re.compile('[^A-Z\s]')

def main():
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'

#Determin the possible valid ciphertext translations:
    print('Hacking...')
    letterMapping = hackSimpleSub(message)

    #Display the results to the user
    print('Mapping:')
    print(letterMapping)
    print()
    print('Original ciphertext:')
    print(message)
    print()
    print('Copying hacker message to clipboard:')
    hackedMessage = decryptWithCipherletterMapping(message, letterMapping)
    pyperclip.copy(hackedMessage)
    print(hackedMessage)


def getBlankCipherletterMapping():
    #Return a dictionary value that is a blank cipherletter mapping:

    return{'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': [], 'H': [], 'I': [], 'J': [], 'K': [], 'L': [], 'M': [], 'N': [], 'O': [], 'P': [], 'Q': [], 'R': [], 'S': [], 'T': [], 'U': [], 'V': [], 'W': [], 'X': [], 'Y': [], 'Z': []}

def addLettersToMapping(letterMapping, cipherword, candidate):
    #The letterMapping parameter takes a dictionary value that stores a cipherletter mapping, which is copied by the function. The cipherword parameter is a string value of the ciphertext
    #The candidate parameter is a possible English word that the cipherword could decrypt to. This function adds the letters in the candidate as potential decryption letters for the cipherletters in the cipherletter mapping 

    for i in range(len(cipherword)):
        if candidate[i] not in letterMapping[cipherword[i]]:
            letterMapping[cipherword[i]].append(candidate[i])


def intersectMappings(mapA, mapB):
    #To intersect two maps, create a blank map and then add only potential decryption letters if they exist in BOTH maps

    intersectMappings = getBlankCipherletterMapping()
    for letter in LETTERS:

        #An empty list means "any letter is possible". In this case copy the other map entirely
        if mapA[letter] == []:
            intersectMappings[letter] = copy.deepcopy(mapB[letter])
        elif mapB[letter] == []:
            intersectMappings[letter] = copy.deepcopy(mapA[letter])
        else:
            #If a letter in mapA[letter] exists in mapB[Letter], add the letter to intersectedMapping[letter]
            for mappedLetter in mapA[letter]:
                if mappedLetter in mapB[letter]:
                    intersectMappings[letter].append(mappedLetter)
 
    return intersectMappings


def removeSolvedLettersFormMapping(letterMapping):
    #Cipherletters in the mapping the map to  only one letter are "solved" and can be removed from the other letters. For example, if 'A' maps to potential letters ['M','N'], and maps to ['N'] from the list of what 'A' could map to. So 'A' then to ['M']. Note that now that 'A' maps to only one letter, we remove 'M' from the list of letters for every other letter, we remove 'M' from the list of letters for every other letter.

    loopAgain = True
    while loopAgain:
        #First assume that we will not loop again:
        loopAgain = False

        #solvedLetters will be a list of uppercase letter that have one and only one possible mapping in letterMapping

        solvedLetters = []
        for cipherletter in LETTERS:
            if len(letterMapping[cipherletter]) == 1:
                solvedLetters.append(letterMapping[cipherletter][0])

        #If a letter is solved, then it cannot possibly be a potential decryption letter for a different ciphertext letter, so we should remove if from those other list
        for cipherletter in LETTERS:
            for s in solvedLetters:
                if len(letterMapping[cipherletter]) != 1 and s in letterMapping[cipherletter]:
                    letterMapping[cipherletter].remove(s)
                    if len(letterMapping[cipherletter]) == 1:
                        #A new letter is now solved, so loop again:
                        loopAgain = True

    return letterMapping


def hackSimpleSub(message):
    intersectedMap = getBlankCipherletterMapping()
    cipherwordList = nonLettersOrSpacePattern.sub('', message.upper()).split()

    for cipherword in cipherwordList:
        #get a New Cipherletter mapping for each ciphertext word:

        candidateMap = getBlankCipherletterMapping()

        wordPattern = makeWordPatterns.getWordPattern(cipherword)
        if wordPattern not in wordPatterns.allPatterns:
            continue #This word was not in our dictionary, so continue. Add the letters of each candidate to the mapping

        for candidate in wordPatterns.allPatterns[wordPattern]:
            addLettersToMapping(candidateMap, cipherword, candidate)

            #INtersect the new mapping with the existing intersected mapping
        
        intersectedMap = intersectMappings(intersectedMap, candidateMap)
    
    return removeSolvedLettersFormMapping(intersectedMap)

def decryptWithCipherletterMapping(ciphertext, letterMapping):
    #Return a string of the ciphertext decrypted with the letter mapping, with any ambiguous decrypted letters replace with an underscore.
    #First create a simple sub key from the letterMApping mapping

    key = ['x'] * len(LETTERS)
    for cipherletter in LETTERS:
        if len(letterMapping[cipherletter]) == 1:
            #If there's only one letter, add it to the key
            keyIndex = LETTERS.find(letterMapping[cipherletter][0])
            key[keyIndex] = cipherletter
        else:
            ciphertext = ciphertext.replace(cipherletter.lower(), '_')
            ciphertext = ciphertext.replace(cipherletter.upper(), '_')
    key = ''.join(key)

    #With the key we've created, decrypt the ciphertext
    return simpleSubCipher.decryptMessage(key, ciphertext)

if __name__ == '__main__':
    main()