palabraSinVocal = ""

userWord = input("Ingresa una palabra:")
userWord = userWord.upper()

for letra in userWord:
    if letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        continue
    palabraSinVocal += letra
print(palabraSinVocal)
