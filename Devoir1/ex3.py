'''Exercice 3'''

#On commence par demander à l'utilisateur d'entrer dans la console le nombre
#d'unités vendues. Et on transforme sa réponse en entier.
quantite=int(input("Combien d'unités ont été vendues?: "))

#À chaque fois que la quantité est inférieur ou égale à zéro, ça va envoyer 
#un message d'erreur et demander à l'utilisateur de recommencer. On va sortir
#de la boucle et calculer le rabais lorsque la quantité sera suppérieur à 0. 
while quantite<=0:
    print("Vous devez fournir un nombre d'unités supérieur à zéro. Recommencez.")
    quantite=int(input("Combien d'unités ont été vendues?: "))   

#Quantité entre 1-9, 0% de rabais
if quantite<10 and quantite>0:
    total=quantite*99
    rabais=0

#Quantité entre 10-19, 20% de rabais    
if quantite<20 and quantite>9:
    total=(quantite*99)*0.8
    rabais=(quantite*99)*0.2

#Quantité entre 20-49, 30% de rabais    
if quantite<50 and quantite>19:
    total=(quantite*99)*0.7
    rabais=(quantite*99)*0.3

#Quantité entre 50 et 99, 40% de rabais     
if quantite<100 and quantite>49:
    total=(quantite*99)*0.6
    rabais=(quantite*99)*0.4

#Quantité de 100 et plus, 50% de rabais    
if quantite>99:
    total=(quantite*99)*0.5
    rabais=(quantite*99)*0.5

#On imprime dans la console le coût total ainsi que le montant du rabais
#En format monétaire  
print("Le coût total est de:", "{:.2f}$".format(total))
print("Le montant du rabais est de:", "{:.2f}$".format(rabais))


