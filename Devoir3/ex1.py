'''Exercice 1 '''

''' -------------- FONCTIONS -------------- '''

# On crée une fonction pour afficher la salle
def Affichersalle():
        print('                                    Sieges')
        for i in range(0,15):
            k=i+1
            print('Rangée',k, ':',*salle[i],end = '')
            print() 
        print('Légende * = Vendu')
        print('# = Disponible')
        
# On crée une fonction qui va calculer le prix        
def CalculPrix(rangee):
        if rangee<=9:
            k=200-20*(rangee-1)
        else:
            k=30
        return k     


''' -------------- DÉBUT DU PROGRAMME -------------- '''
fichierTarifs=input("Entrez le chemin d'accès de votre fichier de tarifs: ")

#On crée une liste de toutes les rangées
salle = [["#" for x in range(15)]for y in range(30)]

#Afficher le menu à l'utilisateur
print('''            Menu principal
      
      1.Afficher les places disponibles
      2.Afficher les tarifs
      3.Afficher le total des ventes
      4.Acheter un billet
      5.Quitter''')

#Demander à l'utilisateur de choisir une option
#initialiser les variables
nbbillet=0
prix=0
total=0
choix=0

while choix !=5:
    choix=int(input('Veuillez SVP choisir une option(1-5): '))
    
    #Afficher les places disponibles
    if choix==1:
        Affichersalle()
       
               
    #Afficher les tarifs
    if choix==2:
        fich=open(fichierTarifs, 'r')
        lignes=fich.read()
        print(lignes)
        fich.close()
        
    #Afficher le total des ventes
    if choix==3:
          print('Vous avez acheté', nbbillet,'pour un total de', total,'$')
     
    #Acheter un billet    
    if choix==4:
        #Offrir à l'usager de montrer les places disponibles
        autreachat='o'
        while autreachat=='o':
            question=input('Voulez-vous voir les places disponibles (o/n)?')
            if question=='o':
                Affichersalle()                
            #Demander à l'usager de choisir son siege
            rangee=int(input('Entrez le numero de rangée (1-15):'))
            siege=int(input('Entrez le numero du siege (1-30):'))
            #Autoriser l'achat seulement si le siège est disponible
            while (salle[rangee-1][siege-1] != "#"):
                print("Désolé, le siège n'est plus disponible")
                print()
                rangee = int(input("SVP entrer le numero de la rangée(1-15): "))
                siege= int(input("SVP entrer le  numero du siège(1-30): ")) 
                print()
            #Réserver la place dans la salle de spectacle après l'achat  
            print('Achat confirmé')    
            salle[rangee-1][siege-1] = "*"       
            #Calcul du prix
            prix=prix+CalculPrix(rangee)
            #Ajouter un billet au décompte
            nbbillet=nbbillet+1 
            
            #Ajuster le total selon le nombre de billet acheté
            #Demander à l'usager s'il veut faire un autre achat
            autreachat=input('Voulez-vous faire un autre achat (o/n)? ')
            
           
        total=prix    
        #S'il a terminé ses achats, il faut lui afficher un résumé de ses achats
        print('Vous avez acheté', nbbillet,'pour un total de', total,'$')
        print()
        
#Quitter le programme
print('Merci davoir magasiner avec nous, votre total de billets achetés est', nbbillet, 'pour un total de',total)
    
