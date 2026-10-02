import random
print(" WELCOME TO NUMBER GUESSING GAME")
secret_number = random.randint(1, 50)
chances = 5
for i in range(chances):
    guess = int(input(f"Chance {i+1}/{chances} - Guess (1-50): "))
    if guess == secret_number:
        print(f"You won! Number was {secret_number}")
        break
    elif guess < secret_number:
        print("Too Low!")
    else:
        print("Too High!")
else:
    print(f"Game Over! Number was {secret_number}")
