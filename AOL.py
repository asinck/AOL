import sys, random

import AOL_Keys as AOL

#this can take up to two arguments:
#chance is the chance of success
#mod is the "out of"; the default is two, meaning there are two
#possibilities.
#if no parameters are provided, then it's a 1/2 (50%) chance of
#returning true.
def myRand(chance=1, mod=2):
    return random.randint(0,20)%mod < chance

#this returns a random index in the given range
def randIndex(end):
    return random.randint(0, end-1)

#this returns a random replacement from the translation table
def randResult(key):
    if type(AOL.words[key]) == type([]):
        end = len(AOL.words[key])
        return AOL.words[key][randIndex(end)]
    else:
        return AOL.words[key]

#this does the actual translations
def translate(wordlist):
    returnString = ""
    newWord = ""

    if wordlist[0] == "@ignore":
        returnString = ' '.join(wordlist[1:])
    else:
        for word in wordlist:
            newWord = word
            #90% chance of translating each word
            if myRand(9,10):
                if (word.lower() in AOL.words):
                    newWord = randResult(word.lower())
                else:
                    for substitution in AOL.subs:
                        #50% chance of substituting letters around, if the
                        #substitution is in the word
                        if substitution in newWord and myRand():
                            newWord = newWord.replace(substitution, AOL.subs[substitution])
                #50% chance of raising the case
                if myRand():
                    newWord = newWord.upper()
            returnString += newWord + " "
        
        #swap some letters around
        buildString = ""
        for i in range(0, len(returnString)-1, 2):
            if myRand(1,6):
                buildString += returnString[i+1] + returnString[i]
            else:
                buildString += returnString[i] + returnString[i+1]
        
        #add some random acronyms to the end
        for i in range(randIndex(10)):
            if myRand(3,4):
                length = len(AOL.addons)
                buildString += AOL.addons[randIndex(length)] + " "
                
        for i in range(randIndex(20)):
            if myRand(3,4):
                if myRand(4,5):
                    buildString += "!"
                else:
                    buildString += "1"
        
        returnString = ""
        for i in buildString.split():
            #do some capitalization
            if myRand():
                returnString += i.upper() + " "
            else:
                returnString += i.lower() + " "
                        
    return returnString
    
#run if called directly
if __name__ == "__main__":
    #yes, I should use error checking. but this is easier and faster.
    try:
        print translate(sys.argv[1:])
    except:
        pass
