import random
randNum = random.randint(1,100)
userguess = None
guesses = 0

while (userguess != randNum):
    userguess = int(input("Enter your guess: "))
    guesses += 1

    if (userguess == randNum):
        print("You guessed it right")
    elif(userguess > randNum):
        print("Lower number please")
    else:
        print("Higher number please")

print(f"You have guessed the correct number {randNum} in {guesses} attempts")
with open("highscore.txt","r") as f:
    highscore = int(f.read())

if(guesses < highscore):
    print("You have just broke the highscore")
    with open("highscore.txt","w") as f:
        f.write(str(guesses))
