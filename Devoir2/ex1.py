'''Exercice 1 '''

#On crée une variable qui compte le nombre de bonnes réponses 
BonnesRéponses=0

#On affiche la question, les choix de réponses à l'écran et on demande à 
#l'utilisateur d'entrer sa réponse. Si c'est la bonne réponse, on ajoute un 
#point au compte de bonnes réponses. On répète la même chose pour les 4 questions.

Q1=int(input('''Combien de degré Celsius, en moyenne, la température a-t-elle 
augmenté depuis l'année 1800?

 1: 0.4 degré Celsius
 2: 0.6 degré Celsius
 3: 2.4 degré Celsius
 4: 3.4 degré Celsius
 
Réponse: '''))

if Q1==2:
    BonnesRéponses=BonnesRéponses+1
    print("Félicitations! C'est la bonne réponse.")
else:
    print("Erreur. La bonne réponse était la réponse 2 «0.6 degré Celsius».")

Q2=int(input('''On s'attend à ce qu'elle continue d'augmenter d'ici à l'an 2100.
De combien de degrés?

 1: De 0.5 à 3.6
 2: De 1.4 à 5.8
 3: De 2.7 à 7.9
 4: De 0.6 à 2.3
 
Réponse: '''))    

if Q2==2:
    BonnesRéponses=BonnesRéponses+1
    print("Félicitations! C'est la bonne réponse.")
else:
    print("Erreur. La bonne réponse était la réponse 2 «De 1.4 à 5.8».") 

Q3=int(input('''Quel est le gaz à effet de serre le plus abondant dans l'atmosphère?

 1: La vapeur d'eau
 2: Dioxyde de carbone
 3: Méthane
 4: Monoxyde de carbone
 
Réponse: '''))

if Q3==1:
    BonnesRéponses=BonnesRéponses+1
    print("Félicitations! C'est la bonne réponse.")
else:
    print("Erreur. La bonne réponse était la réponse 1 «La vapeur d'eau».") 
    
Q4=int(input('''En quelle année est apparu le terme «effet de serre» ?

 1: 1824
 2: 1896
 3: 1958
 4: 1962
 
Réponse: '''))    

if Q4==1:
    BonnesRéponses=BonnesRéponses+1
    print("Félicitations! C'est la bonne réponse.")
else:
    print("Erreur. La bonne réponse était la réponse 1 «1824».")

#On affiche un message selon le nombre de bonnes réponses.
if BonnesRéponses==4:
    print("Excellent! Vous avez eu 4 bonnes réponses.")
elif BonnesRéponses==3:
    print("Très bien. Vous avez eu 3 bonnes réponses.")
elif BonnesRéponses<3:
    print("Vous devez améliorer vos connaissances. Vous avez eu moins de 3 bonnes réponses.")
    
    



