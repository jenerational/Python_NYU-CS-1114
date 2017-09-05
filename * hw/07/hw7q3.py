#  Jennie Walker HW 7.3
# November 2 2015 

def main():
    import random
    int1 = random.randint(1, 100)
    print("I thought of a number between 1 and 100! Guess it! ")
    #sets number of guesses at 5
    guessLeft = 5
    print("You have 5 guesses")
    print(randGuess(int1))

def randGuess(int1):
    guess = int(input("Try to guess what it is: "))
    #calculates bounds
    upperGuess = 100
    lowerGuess = 1
    #calculates number of guesses taken
    guessNum = 0
    while (int1 != guess):
        if guessNum < 5:
            if (int1 < guess):
                upperGuess = guess
                print("Wrong guess. Guess is in range", str(lowerGuess), "to", str(upperGuess))
                guessNum += 1
                guess = int(input("Try to guess what it is: "))
            else:
                lowerGuess = guess
                print("Wrong guess. Guess is in range", str(lowerGuess), "to", str(upperGuess))
                guessNum += 1
                guess = int(input("Try to guess what it is: "))
        else:
            return "You have used up all your guesses. Try again!"
    endStatement = "You guessed the number in", str(guessNum+1), "guesses."
    return endStatement

main() 

