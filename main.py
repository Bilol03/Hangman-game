import os
import random
import hangman_art
import hangman_words

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)

line_list = ""
for i in chosen_word:
  line_list += "_"

line_list = list(line_list)

res = False
lives = 6
while not res:

    print(line_list)

    guess = input("Guess a letter: ").lower()
    if guess in line_list:
        print(f"You have already guessed {guess}")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            os.system('clear')
            line_list[position] = letter
    if guess not in chosen_word:
        os.system('clear')
        print(f"You have guessed {guess}, that is not correct you are loosing your live")
        lives -= 1
        if lives == 0:
            res = True
            print("You Lose")
    if "_" not in line_list:
        res = True
        print("You win")

    
    print(hangman_art.stages[lives])

