import random

print("Welcome to Guessing Game!")

def two_player():
    choice = input("Two Player?(Y/N)").lower()
    return choice

def gen_random_num(l_limit, u_limit):
    print(f"\nGuess from {l_limit} to {u_limit}! xD")
    number = random.randint(l_limit,u_limit)
    return number

def ask_user():
    guess = int(input("Input your guess: "))
    return guess

def check_guess(guess, number):
    if guess < number:
        print("Too Low! Try again.")
        return False
        
    if guess > number:
        print("Too high! Try again.")
        return False
        
    if guess == number:
        print("\nCongratulations! You are correct!")
        return (True)

    

two_player = two_player()
guesses = []
gameon = True
l_limit = int(input("Pick the range of numbers to guess from, input the lower limit: "))
u_limit = int(input("Input the upper limit: "))
number = gen_random_num(l_limit, u_limit)

while gameon:
    
    if two_player == 'n':
        guess = ask_user()
        
        if check_guess(guess, number):
            guesses.append(guess)
            print(f"It took you {len(guesses)} guesses to reach the correct number")

            choice = input("\n\nDo you want to play again?(Y/N): ").lower()
            if choice == 'n':
                print("\n\nThanks for playing!")
                gameon = False

            else:
                number = gen_random_num(l_limit, u_limit)
                guesses = []

        else:
            guesses.append(guess)
    
    elif two_player == 'y':
        
        first_player = input("First player, input your name: ")
        second_player = input("Second player, input your name: ")
        
        startsfirst = 0
        if startsfirst == 0:
            first_player_score = 0
            print(f"{first_player} starts first")
            while startsfirst == 0:
                guess = ask_user()
                if check_guess(guess, number):
                    guesses.append(guess)
                    if len(guesses) < 10:
                        first_player_score = ((10 - len(guesses)) + 1) * 100
                    if len(guesses) > 10 and len(guesses) < 20:
                        first_player_score = (100 - (10*len(guesses)))
                        
                    print(f"It took {first_player} {len(guesses)} guesses to reach the correct number. {first_player} your score is {first_player_score}")
                    startsfirst = 1
                    guesses = []
                    
                else:
                    guesses.append(guess)
            
        if startsfirst == 1:
            second_player_score = 0
            number = gen_random_num(l_limit, u_limit)
            print(f"{second_player}'s turn")
            while gameon:
                guess = ask_user()
                if check_guess(guess, number):
                    guesses.append(guess)
                    if len(guesses) < 10:
                        second_player_score = ((10 - len(guesses)) + 1) * 100
                    if len(guesses) > 10 and len(guesses) < 20:
                        second_player_score = (100 - (10*len(guesses)))
                        
                    print(f"It took {second_player} {len(guesses)} guesses to reach the correct number. {second_player} your score is {second_player_score}")
                    guesses = []
                    choice = input("\n\nDo you want to play again?(Y/N): ").lower()
                    if choice == 'n':
                        print("\n\nThanks for playing!")
                        
                        if first_player_score > second_player_score:
                            print(f"{first_player} wins!")
                            print(f"1. {first_player}: {first_player_score}\n2. {second_player}: {second_player_score}")
                        else:
                            print(f"{second_player} wins")
                            print(f"2. {second_player}: {second_player_score}\n2. {first_player}: {first_player_score}")

                        gameon = False

                    else:
                        number = gen_random_num(l_limit, u_limit)
                        guesses = []
            

                else:
                    guesses.append(guess)