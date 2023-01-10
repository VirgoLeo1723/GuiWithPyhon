import random as rd
import string as str
from Words import words

def get_word(words):
    word=rd.choice(words)
    while ' ' in word or '-' in word:
        word=rd.choice(words)
    return word

def play():
    temp=get_word(words)
    ans=list(temp)
    al=set(str.ascii_lowercase)
    used_word=set()
    input_word=""
    checker=0

    print("Hangman start right now!!! \nLet's guess a letter each time")
    
    while checker==0:
        input_letter=input("Assume letter: ").lower()
        if input_letter in al-used_word: 
            used_word.add(input_letter)
        else:
            print("You've already chosen this word, try again.")

        input_word=[letter if letter in used_word else "_" for letter in ans]
        print(f"Letter used: {' '.join(used_word)}")
        print(f"Hold on, It's almose there {''.join(input_word)}\n")

        if not('_'in input_word): checker=1
    
    print("Hurayyyyy!!!!!!!")
play()