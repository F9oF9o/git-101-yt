import random

score = 0
lives    = 3
words = ['Tone', 'Ja','Jinny','Jom','Jeep']

while (len(words)>0) and (lives>0):
    random.shuffle(words)
    secret_word = words.pop()
    clue = list('?'*len(secret_word))

  
