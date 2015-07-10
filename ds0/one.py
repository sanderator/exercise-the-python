fichier = input("une phrase") #1

i = 0 #2

while i < len(fichier) and fichier[i] != " " : #3
    print(fichier[i], end="") #4
    i += 1 #5
