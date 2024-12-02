import random
nombre_aleatoire = random.randint(1,100)
solution = random.randint(1,100)
nbr = 0
tentative = 0
while nombre_aleatoire != nbr:
    nbr = int(input("Valeur ?"))
    tentative = tentative + 1
    if nbr > solution:
        print("-")
    elif nbr < solution:
        print("+")
    else :
        print("gagné")
        print(f"La réponse était {solution} et il vous & fallu {tentative} coups")

