'''Exercice 3'''

#On demande à l'utilisateur d'entrer un nombre impair
n = int(input("Entrez un nombre impair: "))

#On calcule la taille de la hauteur de la pyramide
hauteur = int((n+1)/2)

# On affiche la moitié de la pyramide jusqu'à sa hauteur maximale
# C'est la partie ou la taille des lignes horizontales est croissante

i=1
while i < hauteur+1:
    for j in range(1,i+1):
        print(j, end = ' ') 
    print()
    i=i+1
    
# On affiche la deuxième moitié de la pyramide
# C'est la partie ou la taille des lignes horizontales est décroissante
#On commence à hauteur-1, car pour faire un sommet
#il ne faut qu'une seule ligne plus longue que les autres au milieu de la pyramide
    
pyramide = hauteur - 1    
k = 1    
while pyramide > 0:
    for k in range(1,pyramide+1):
        print(k, end = ' ') 
    print()
    pyramide = pyramide - 1
