'''Exercice 2'''

#On demande premièrement à l'utilisateur d'entrer le nombre crypté.
#On transforme sa réponse en entier.
nombre_crypté=int(input("Entrez le nombre crypté:"))

#Section cryptage 
x=nombre_crypté

#On sépare tous les chiffres du nombre selon leur position 
x1=x//10000
x2=(x-x1*10000)//1000
x3=(x-(x1*10000+x2*1000))//100
x4=(x-(x1*10000+x2*1000+x3*100))//10
x5=(x-(x1*10000+x2*1000+x3*100+x4*10)) 

#On a déterminer que si le chiffre était entre 0 et 3, il y avait un reste 
#lorsqu'on appliquait le modulo et qu'en faisant +6 on revenait au chiffre 
#original. Sinon, le reste était de 0 alors on avait juste à enlevé le 4 
#précédement ajouté.
if x1<4:
    y1=(x1+6)
else:
    y1=(x1-4)
    
if x2<4:
    y2=(x2+6)
else:
    y2=(x2-4)
    
if x3<4:
    y3=(x3+6)
else:
    y3=(x3-4)
    
if x4<4:
    y4=(x4+6)
else:
    y4=(x4-4)

if x5<4:
    y5=(x5+6)
else:
    y5=(x5-4)    
    
#On reforme le nombre selon les positions originales.    
nombre_décrypté=(y3*10000+y4*1000+y1*100+y2*10+y5)

#On imprime le résultat dans la console.
print("Le nombre décrypté est:",nombre_décrypté)





