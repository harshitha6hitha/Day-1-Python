secret_number=7
guess=int(input("Guess a number between 1 and 10: "))
if guess==secret_number:
    print("Congratulations! Correct guess!")
elif guess<secret_number:
    print("Too low! Try again.")
else:
    print("Too high! Try again.")