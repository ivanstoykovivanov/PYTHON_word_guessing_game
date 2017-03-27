from random import randrange
from distutils.command.clean import clean

###################################
#####  Word Guessing Game   #######
###################################

def generateRandomWord() :
    words = ["swordfish", "apple" , "cocktail", "cactus", "zebra" ]     # Array of words to choose from 
    randNumber = randrange(len(words))       # Generate random word from array 
    randWord = words[randNumber]
    return randWord

def writeWord(word, correctlyGuessedLetters ) :   
    # Check if array of guessed letters is empty
    if correctlyGuessedLetters : 
        # Check letters and write them if correct  
        for i in range(len(word)):
            match = False
            for j in range(len(correctlyGuessedLetters)) : 
                if word[i] == correctlyGuessedLetters[j] : 
                    print (word[i] , end = ' ')
                    match = True
            if match :
                continue  
            else: 
                print("_" , end = ' ')
        print("")
    else : 
        for i in range(len(word)):
            print("_", end = '  ')
        print("")
        
def checkLetter(word, correctlyGuessedLetters): 
    print("\n")
    letter = input("Enter a letter : ")
    
    for i in range(len(word))  :
        if word[i] == letter : 
            saveLetter(letter, correctlyGuessedLetters )
            return True
    return False         

def updateTries(result, tries):
    if(result) : 
        print()
    else : 
        print("Wrong \n")
        tries -= 1
        print("You have {} tries left ".format(tries))
    return tries

def saveLetter(letter, savedLetters):
    savedLetters.append(letter)
    return savedLetters
    
def cleanRepeatingLetters(word) :
    arr = []
    for i in word: 
        arr.append(i)
    
    for i in range(len(arr)):
        for j in range(i + 1, len(arr) - 1 ) : 
            if arr[i] == arr[j] :
                arr.remove(arr[j])
    return arr

# Main function        
def play ():
    tries = 3                           # Number of tries before you lose the game
    correctlyGuessedLetters = []        # Letters already guessed correctly by the player : 
    randomWord = generateRandomWord()   #Word to guess 
    win = None                          #Flag
    
    while (tries > 0 )  :
        cleanedWord = cleanRepeatingLetters(randomWord)         # Isolate the non-repeated letters
        if(len(correctlyGuessedLetters) == len(cleanedWord)) :  # Check if there are unguessed letters 
            win = True
            break; 
        else :  
            writeWord(randomWord, correctlyGuessedLetters)
            result = checkLetter(randomWord, correctlyGuessedLetters) ; 
            tries  = updateTries(result, tries) 
            win = False
    if(win == True ):
        print("YOU WIN ! ")
    else : 
        print("GAME OVER")
        print("The word is : {}".format(randomWord) ) 

#####################################

play()

