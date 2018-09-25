'''Exercice 2 '''

#On importe la librairie random pour créer une variable aléatoire uniforme [1,6]

import random 
#Pour créer les dés, on utilise la fonction randint pour détermer un nombre aléatoire
#sur le range 1 à 6
dé1=random.randint(1,6)
dé2=random.randint(1,6)
somme=dé1+dé2
print("Lancer", dé1,"+", dé2, "=", somme)

#Si le jeu n'est pas gagné ou perdu automatiquement, la somme détermine le point.
point=somme
if somme in (4,5,6,8,9,10):
    print("Le point est:",point)
    

#Cas dans lequel le joueur gagne automatiquement    
if somme in (7,11):
    print("Le joueur a gagné.")
    
#Cas dans lequel le joueur perd automatiquement   
elif somme in (2,3,12):
    print("Le joueur a perdu.")

#Cas dans lequel le jeu continu    
elif somme in (4,5,6,8,9,10):
    dé1=random.randint(1,6)
    dé2=random.randint(1,6)
    somme2=dé1+dé2
    print("Lancer", dé1,"+", dé2, "=", somme2)
    
    #Tant que la somme des deux dés n'est pas égale au point ou à 7, le jeu 
    #continue, c'est à dire que le joueur relance les deux dés
    while somme2!=point and somme2!=7:     
        dé1=random.randint(1,6)
        dé2=random.randint(1,6)
        somme2=dé1+dé2
        print("Lancer", dé1,"+", dé2, "=", somme2)
    
    #Cas dans lequel le jeu arrête, car le joueur a gagné    
    if somme2==point:    
        print("Le joureur a gagné.")
    #Cas dans lequel le jeu arrête car le joueur a perdu
    if somme2==7:
        print("Le joueur a perdu.")
