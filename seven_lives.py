import random
lives = 7
words= ['fries', 'pizza','stars','latte','money']
secret_word = random.choice(words)
clue = list ('?????')
heart = u'\u2764'
print(heart)
guessed_word_correctly = False

def update_clue(guessed_letter, secret_word,clue):
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index = index + 1

while lives > 0:
    print(clue)
    print("lives left😨:" + heart * lives)
    guess = input("guess a letter or the whole word: ")

    if guess == secret_word:
        guessed_word_correctly = True
        break

    if guess in secret_word:
        update_clue(guess, secret_word, clue)
    else:
        print("thats wrong child 😔, you lost A LIFE :0")
        lives = lives - 1
        
if guessed_word_correctly == True:
    print("YOU WON KID 🥰!! the secret word was",secret_word)
else:
    print("thats ok child 😔, the word was" ,secret_word, "btw")
