import random
from Words import words

print("\n\nWelcome to: Hangman")
print("===========================")
print("This program runs hangman. Guess the word letter \nby letter with little mistakes to win. Good luck!")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

word = random.choice(words)
while "-" in word or " " in word:
  word = random.choice(words)
word = word.upper()

guess_list = []
lives = 7

while True:
  new_word = ""
  guess_string = ""
  for i in word:
    if i in guess_list:
      new_word = new_word + i  
    else:
      new_word = new_word + "_"
  
  if "_" not in new_word or lives == 0:
    break
  
  for i in guess_list:
    guess_string = guess_string + i + " "
      
  print("The current word is:", new_word)

  if len(guess_list) > 0:
    print("The letters you have guessed are:", guess_string)
  print("The number of lives you have left are:", lives)

  user_guess = input("Enter a letter here to guess: ").upper()
  
  counter = 0
  while counter <= 2:
    if user_guess.isalpha() == False or len(user_guess) > 1:
      user_guess = input("\nPlease only enter a letter: ").upper()
      counter = 0
    counter = counter + 1

    if user_guess in guess_list:
      user_guess = input("You have already guessed that. Please try again: ").upper()
      counter = 0
    counter = counter + 1

  guess_list.append(user_guess)

  if user_guess in word:
    print("\nCORRECT!")

  else:
    print("\nINCORRECT!")
    lives = lives - 1

if lives == 0:
  print("\nYou lost! The word was:", "\"" + str(word) + "\"")
else:
  print("\nYou have sucessfully guessed the word", "\"" + str(word) + "\"" + "!!!")
  print("Thank you for playing!")
