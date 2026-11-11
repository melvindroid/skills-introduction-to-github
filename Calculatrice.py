#!/usr/bin/env python3

print ("CALCULATRICE")

print ("1_Addition")
print ("2_Soustraction")
print ("3_Multiplication")
print ("4_Division")

choix = input ("Choisis une opération")

entrée1 = float(input("Entre le premier mombre"))

entrée2 = float(input("entre le deuxième nombre"))

if choix == "1":
    print ("Résultat", entrée1 + entrée2)

elif choix == "2":
    print ("Résulat", entrée1 - entrée2)

elif choix == "3":
    print ("Résulat", entrée1 * entrée2)

elif choix == "4":
    print ("Résultat", entrée1 / entrée2)

else:

    print("choix invalide")


