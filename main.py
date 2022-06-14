"""
Name(s): Dakota Lee, Vennela Talapaneni
Name of Project: Hangman
"""
#i found the wordlist online somewhere and i forgot the link. so thats that i suppose

import random

file = open('words.txt','r')
text = file.read()
wordList = text.splitlines()

word = random.choice(wordList)
word = list(char for char in word)

usedChances = 0
usedLetters = []

displayWord = list(len(word)*"_")

while usedChances < 16:
  if set(usedLetters).issuperset(word) == True:
    print("You got the word! It was",''.join(word)+"!")
    exit()
    
  letterGuess = input("Guess a letter/word: ")
  letterGuess = letterGuess.lower()
  temp2 = ''.join(word)
  
  if letterGuess == temp2:
    print("You got the word! It was",''.join(word)+"!")
    exit()
    
  elif letterGuess in usedLetters:
    print("You already guessed that!")
    
  elif letterGuess not in word:
    print(letterGuess,"is not in the word.")
    usedChances += 1
    print("So far, you have guessed:", ''.join(displayWord)) 
    usedLetters.append(letterGuess)
    print("You have guessed letters:", ', '.join(usedLetters))
    print("You have",str(16-usedChances),"chance(s) left.")
    
  elif letterGuess in word:
    print(letterGuess,"is in the word.")
    temp = []
    displayWord = ''.join(displayWord)
    for i in range(len(temp2)):
      if temp2[i] == letterGuess:
        temp.append(i)
    for i in temp:
      displayWord = displayWord[:i] + letterGuess + displayWord[i+1:] 
    print("So far, you have guessed:", ''.join(displayWord))
    usedLetters.append(letterGuess)
    
print("Aw. The word was",''.join(word)+".")
exit()
