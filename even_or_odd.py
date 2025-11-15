import random

win = 0
lose = 0
print("WELCOME TO THE GAME FOR EXIT ENTER EXIT")
while True:
    player = input("Enter guss (even, odd) : ").lower()
    if player not in ["even", "odd", "zoj", "fard", "exit", "0"]:
        print("Error: Invalid choice")
        continue
    if player in ["exit", "0"]:
        print(f"your right guesses {win}, wrong guesses {lose} times.")
        print("goodbye!")
        break
    number = random.randint(1, 20)
    if number % 2 == 0 and player in ["even", "zoj"]:
        win += 1
        print(f"You won! The number is {number}.")
        print(f"your correct guesses {win}, wrong guesses {lose} times.")
    elif number % 2 == 1 and player in ["odd", "fard"]:
        win += 1
        print(f"You won! The number is {number}.")
        print(f"your right guesses {win}, wrong guesses {lose} times.")
    else:
        lose += 1
        print(f"You lose number was {number}.")
        print(f"your right guesses {win}, wrong guesses {lose} times.")



