import random

def guess_the_number():
    number_to_guess = random.randint(1, 1000)
    attempts = 0
    
    print("\nWelcome to the number guessing game!")
    print("I have chosen a number between 1 - 100. Guess what!")
    
    while True:
        try:
            guess = int(input("Enter your guess number: "))
            attempts += 1
            
            if guess < number_to_guess:
                print("Too small! Try again.")
            elif guess > number_to_guess:
                print("Too big! Try again.")
            else:
                print(f"Congratulations! on guessing the correct number in {attempts} tries")
                break
        except ValueError:
            print("Enter a valid number!")

# Jalankan game
if __name__ == "__main__":
    guess_the_number()
