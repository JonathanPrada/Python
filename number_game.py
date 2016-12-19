import random

def game():
  #Generate random number between 1 and 10
  secret_num = random.randint(1, 10)
  guesses = []
  
  while len(guesses) < 5:
    #Guess a number from the player
    guess = input("Guess a number between 1-10: ")
    try:
      guess = int(guess)
    except ValueError:
      print("{} is not a number!".format(guess))
    else:
        #Compare number
        if guess == secret_num:
          print("You guessed correctly!")
          break
        elif guess < secret_num:
          print("My guess is higher than your {} guess".format(guess))
        else:
          print("My guess is lower than your {} guess".format(guess))
        guesses.append(guess)
  else:
    print("The correct guess was {}. Hard luck!".format(secret_num))
  play_again = input("Do you want to play again? Y/N: ")
  if play_again.lower() != 'n':
    game()
  else:
    print("Bye!")
        
game()
