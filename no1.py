# numéro 4.1 Marchand


# Ce programe permet de déterminer quel type d'achat est le plus avantageux entre trois format.
# Il permet également de calculer le coût final de chacun des formats après certains rabais et l'économie réalisé par rapport à l'achat en vrac

# Par AS 29-09-2026

#limite #si la quantité de rabais devient gigantesque, le code peut s'allourdir rapidement

from typing import Final
import math
#CONSTANTES
POIDS_PETIT: Final = 2 # poids du petit sac en kilo
POIDS_GROS: Final = 5 # poids du gros sac en kilo
TAUX_RABAIS_PETIT: Final = 0.10
TAUX_RABAIS_GROS: Final = 0.15

#variables
poids_desire: float # masse de produit désiré en kilo #demandé
prix_de_base: float # prix du produit en dollar par kilo #demandé
prix_vrac: float
prix_petit: float
prix_gros: float
quantité_petit: float #nombre de petits sacs
quantité_gros: float #nombre de gros sacs
poids_acheté_petit: float#poids acheté par rapport aux poids et nombre de sac
poids_acheté_gros: float
économie: float#l'argent économisé comparé au vrac
#logique
poids_desire = float(input("De quel quantité avez-vous besoin(en kilogrammes)?"))
prix_de_base = float(input("Quel est le prix du produit par kilo?"))
quantité_petit = math.ceil(poids_desire / POIDS_PETIT)
quantité_gros = math.ceil(poids_desire / POIDS_GROS)
poids_acheté_petit = POIDS_PETIT * quantité_petit
poids_acheté_gros = POIDS_GROS * quantité_gros
prix_vrac = poids_desire * prix_de_base
prix_petit = prix_de_base * poids_acheté_petit * (1-TAUX_RABAIS_PETIT)
prix_gros = prix_de_base * poids_acheté_gros * (1-TAUX_RABAIS_GROS)
print(f"Les prix sont les suivants: vrac:{prix_vrac:.2f}$ petit: {prix_petit:.2f}$ gros: {prix_gros:.2f}$")
print("Le choix le plus avantageux est ",end="")
if prix_vrac < prix_petit and prix_vrac < prix_gros:
    print("le vrac")
if prix_petit < prix_gros and prix_petit < prix_vrac:
    économie = prix_vrac - prix_petit
    print(f"le petit, vous avez acheté {poids_acheté_petit}kg de produit et économisé {économie:.2f}$")
if prix_gros < prix_petit and prix_gros < prix_vrac:
    économie = prix_vrac - prix_gros
    print(f"le gros, vous avez acheté {poids_acheté_gros}kg de produit et économisé {économie:.2f}$")











