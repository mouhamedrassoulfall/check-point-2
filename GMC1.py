#exercice1
nom = input("quel est votre nom?")
print(nom)
prenom = input("quel est votre prenom?")
print(prenom)
nom_complet = nom +" "+ prenom
print("votre nom complet est " + nom_complet)

#exercice2
n = input("entrer un entier")
nn = n + n
nnn = n + n + n
resultat = int(n) + int(nn) + int(nnn)
print(resultat, "(", n, "+", nn, "+", nnn, ")")

#exercice3
nombre = int(input("Saisir un nombre: "))
if nombre % 2 == 0:
  print("paire")
else:
  print("impaire")

#exercice4
for i in list(range(2000,3201)):
    if i%7==0 and i%5!=0:
        print(i)

#exercice5
n = int(input("Saisir un nombre: "))
reponse = True
facto = 1
while reponse: 
  if n == 0:
    reponse = False
  else :
    facto *= n
    n -= 1 
  
print(facto)

#exercice6
chaine = input("Saisir une chaine ")
new_chaine = "m"
for i in range(len(chaine)):
  if i%2 == 0:
    new_chaine += chaine[i]
print(new_chaine)

#exercice7
prix= int(input("entrer un prix"))
if prix > 500 :
    prix /=2
    print(prix)
elif prix >=200 and prix<500 :
    prix -= (prix*0.3)
    print(prix)
elif prix <200 :
    prix -= (prix*0.1)
    print(prix)
