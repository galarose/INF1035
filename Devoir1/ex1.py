'''Exercice 1'''

#On définit que si c'est un palindrome, c'est égale à True, donc qu'on ne sort 
#pas de la boucle tant que c'est un palindrome
Palindrome = True


while Palindrome:
    #L'utilisateur doit entrer un nombre de 5 chiffres dans la console. 
    # On transforme sa réponse en entier.
    nombre = int(input("Entrez un nombre entier de 5 chiffres:"))
    nombre2 = nombre
    reverse = 0  
    while(nombre2 > 0):
    #Manipulation mathématique pour déterminer si le nombre est un palindrome    
        dig = nombre2%10
        reverse = reverse*10+dig
        nombre2 = nombre2//10    
    if(nombre == reverse):
    #Si le nombre est un palindrome, le boucle continu et l'utilisateur se fait
    #demander d'entrer un autre nombre de cinq chiffres.    
        print("Le nombre est un palindrome! Veuillez recommencer en entrant un nombre non palindrome. ")
        Palindrome = True
    else:
    #Si le nombre n'est pas un palindrome, on sort de la boucle et on continu
    #vers la partie cryptage du code    
        print("Le nombre n'est pas un palindrome!")
        Palindrome = False

#Section cryptage 
x=nombre

#On sépare tous les chiffres du nombre selon leur position 
x1=x//10000
x2=(x-x1*10000)//1000
x3=(x-(x1*10000+x2*1000))//100
x4=(x-(x1*10000+x2*1000+x3*100))//10
x5=(x-(x1*10000+x2*1000+x3*100+x2*10))       

#On effectue l'opération de cryptage selon la formule : (chiffre+4)%10 fourni
#dans l'énoncé 
y1=(x1+4)%10
y2=(x2+4)%10
y3=(x3+4)%10
y4=(x4+4)%10
y5=(x5+4)%10

#On inverse la 1ere et la 3e position ainsi que la 2e et la 4e position et on
#reconstruit le nombre 
nombre_crypté=(y3*10000+y4*1000+y1*100+y2*10+y5)

#On imprime le résultat finale dans la console.
print("le nombre crypté est:",nombre_crypté)

   
























