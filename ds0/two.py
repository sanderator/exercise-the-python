fichier = input("une phrase: ") #1
lettre = input("une lettre: ")

i = 0 #2

for l in fichier: #3
    if l == lettre:
        i += 1
        
print('%i occurrences de %s' % (i, lettre))
