#numéro 4.4 processeur

# Ce programme permet de détecter le type de processeur.

# Par AS 29-09-2026

#limite # Ne détecte pas les CPU autre que Intel et AMD

import platform
#aucune constantes

#variable
cpu: str

#logique
cpu = platform.processor()
if "Intel" in cpu:
    print("Vous avez un processeur Intel")
elif "AMD" in cpu:
    print("Vous avez un processeur AMD")
elif "x86_64" in cpu:
    print("Vous exécutez le code Python d'une façon qui rend impossible la détection exacte du processeur")
else:
    print("Votre CPU est inconnu du programme")