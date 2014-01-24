def pourcentage(p, n):
    return (p * 100) / n

def nbFemmes(resultats):
    nbrF = 0
    for marathonien in resultats:
        if marathonien[2] == 'F':
            nbrF += 1
    return nbrF

def premier(resultats):
    gagnant = resultats[0]
    indexChrono = 3
    i = 0
    for i in range(1, len(resultats)):
        if resultats[i][indexChrono] < gagnant[indexChrono]:
            gagnant = resultats[i]
    return gagnant

marathonNice = [
    ["Larue","Arlette","F",4600],
    ["Moore","Roger","M",3700],
    ["Lapierre","Claude","M",7890],
    ["Dupont","Antoine","M",4000],
    ["Lafronte","Mélanie","F",4600],
    ["Patine","Valérie", "F", 3712],
    ["Régent","Régis","M",4356]
    ]


print('résultats du marathon de Nice : %s' % marathonNice)
print('pourcentage de femmes parmi les participants : %f %%' %
      (pourcentage(nbFemmes(marathonNice), len(marathonNice))))
print("pourcentage d'hommes parmi les participants : %f %%" %
      (100 - pourcentage(nbFemmes(marathonNice), len(marathonNice))))
print('le vainquer est %s' % premier(marathonNice))


def lesPremiers(n, resultats):
    lesPremiers = []
    if n > len(resultats):
        print('oups ! n = %i doit être < %i' % (n, len(resultats)))
    else:
        indexChrono = 3
        for d in range(0, n):
            lePremier = premier(resultats)
            lesPremiers.append(lePremier)
            resultats.remove(lePremier)
    return lesPremiers

n = int(input('nb de premiers: '))
print('les %i premiers: %s' % (n, lesPremiers(n, marathonNice)))

                  

