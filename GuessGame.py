secret = "Giraffe"
guess = ""
guesscount = 0
guesslimit = 3
outofguesses = False

while guess != secret and not(outofguesses):
    if guesscount < guesslimit:
        guess = input("Enter Your Guess:")
        guesscount+=1
    else:
        outofguesses = True
        break

if outofguesses:
    print("Out Of Guesses, You Lost!!")

else:
    print("You Won!!")