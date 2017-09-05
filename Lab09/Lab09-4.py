
#   Allows user to play Bulls and Cows game

def main():
    import random
    num = random.randint(1000, 9999)
    print(bullsCows(num))

def bullsCows(num):
    num = str(num)
    guess = 0
    while (num != guess):
        guess = input("Try to guess the four digit number. ")
        bull = 0
        cow = 0
        for i in range(0, len(num)):
            if num[i] == guess[i]:
                bull += 1
            elif num[i] != guess[i]:
                for x in guess:
                    if num[i] == x:
                        cow += 1
        print("You have", str(bull), "bulls and", str(cow), "cows.")
    return("You guessed the number. Yayy!!") 

main()
