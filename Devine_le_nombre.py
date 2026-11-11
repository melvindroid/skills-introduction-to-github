
#!/usr/bin/env python3

import random

print("DEVINE LE NOMBRE")
print("Je pense à un nombre entre 1 et 100.")

nombre_secret = random.randint(1, 100)

essais = 0

while True:

    proposition = int(input("Devine le nombre : "))

    essais = essais + 1

    if proposition < nombre_secret:
        print("C'est plus grand !")

    elif proposition > nombre_secret:
        print("C'est plus petit !")

    else:
        print("Bravo ! Tu as trouvé le nombre !")
        print("Nombre d'essais :", essais)
        break
