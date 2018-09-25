
import random 


''' -------------- FONCTIONS -------------- '''

#On crée une fonction qui lit la table et détermine qui est le gagnant de la 
# partie

def gagnant(joueur):
    
  #On utilise une boucle for pour regarder dans chaque élément dans la liste
  for m in range(0,3):
      
    #emplacement horizontal
    if tictactoe[m][0] == joueur \
    and tictactoe[m][1] == joueur \
    and tictactoe[m][2] == joueur:
      joueur_gagnant = True
      return joueur_gagnant
  
    #emplacement vertical
    elif tictactoe[0][m] == joueur \
    and tictactoe[1][m] == joueur \
    and tictactoe[2][m] == joueur:
      joueur_gagnant = True
      return joueur_gagnant
  
    #emplacement diagonal (de gauche à droite)
    elif tictactoe[0][0] == joueur \
    and tictactoe[1][1] == joueur \
    and tictactoe[2][2] == joueur:
      joueur_gagnant = True
      return joueur_gagnant
  
    #emplacement diagonal (de droite à gauche)
    elif tictactoe[0][2] == joueur \
    and tictactoe[1][1] == joueur  \
    and tictactoe[2][0] == joueur: 
      joueur_gagnant = True
      return joueur_gagnant
  
  else:
    joueur_gagnant = False
    return joueur_gagnant


''' -------------- DÉBUT DU PROGRAMME -------------- '''

jeu = False
while jeu == False:
    
    #Premièrement, on crée une liste initiale représentant les trois rangées
    # du jeu de Tic-Tac-Toe
    tictac = [["","",""],["","",""],["","",""]] 
    tictactoe=tictac

    # On détermine au hasard le joueur qui va commencer le jeu    
    joueurA = random.randrange(0,2)
    
    if joueurA == 0:
        joueurB = 1
    else:
        joueurB = 0

    # On boucle les tour de jeu. (9 au max)
    tour = 1
    while (tour <=9):
        rangee = random.randrange(0,3)
        colonne = random.randrange(0,3)    
        position = tictac[rangee][colonne] 
    
        # On ne peut pas jouer deux fois sur la même case, alors on s'assure
        # que la case est vide
        while (position != ""):
            rangee = random.randrange(0,3)
            colonne = random.randrange(0,3)
            position = tictac[rangee][colonne] 
    
        # le joueur qui commence joue au tours impairs et le joueur 
        # qui joue en deuxième joue au tours pairs.
        if tour%2==0:
            resultat = joueurB
        else:
            resultat = joueurA
        
        
        tictac[rangee][colonne] = resultat
        tour = tour + 1
    

    # On change les 0 et 1 par O et X dans une nouvelle liste
    for i in range(0,3):
        for j in range(0,3):
            if tictac[i][j] == 0:
                tictactoe[i][j] = "O"
            else:
                tictactoe[i][j] = "X"

    # Ici, renvoit une erreur s'il y a deux gagnant. (Il ne peut y en avoir qu'un)
    if gagnant("O") == True and gagnant("X") == True:
        jeu= False
    else:
        jeu = True
    

#boucle, pour afficher le résultat du jeu.  
for i in range(0,3):
    print(*tictactoe[i])

print()


''' -------------- RÉSULTATS -------------- '''


if gagnant("O") == True:
    print("Le joueur O a gagné la partie!")

elif gagnant("X") == True:
    print("Le joueur X a gagné la partie!")

else:
    print("C'est une partie nulle! Il n'y a aucun gagnant.")


