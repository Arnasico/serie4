#numéro 4.5 Nombre de coeurs de processeur

# Ce programme permet d'afficher le nombre de core de processeur

#Par AS 29-09-2026

#limite # ne donne pas de message si le nombre de core n'est pas dans les 5 valeurs données comme c'est mon cas (12)
#pas de constante

#variable
coeurs: str

import multiprocessing

#logique
print("Vous avez", multiprocessing.cpu_count(), "coeurs.")
coeurs = "❤️" * multiprocessing.cpu_count()
print(coeurs)

if coeurs == 2 * "❤️":
    print("dual-core,boff")
elif coeurs == 4 * "❤️":
    print("quad-core,pas mal! Si on est en 2012 oui")
elif coeurs == 8 * "❤️":
    print("super, mais so 2020...")
elif coeurs == 16 * "❤️":
    print("toute une machine")
elif coeurs == 20 * "❤️":
    print("best of the west")