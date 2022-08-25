#/////Nestor Emmanuel Briones Ramirez\\\\
#-1220100321 
word_without_vowels = ""

userWord = input("ingresa palabra: ")
userWord=word_without_vowels.upper()

for letter in userWord:
    if letter in "AEIOU":
        continue
    word_without_vowels += letter
    
print(word_without_vowels)

