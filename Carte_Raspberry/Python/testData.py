# -------------------------------------------------------------- #
##### ---------- LECTURE DE LA MATRICE DE DONNEES ---------- #####
# -------------------------------------------------------------- #

# Initialisation du dictionnaire de données
data = {}

lines = open("./data.txt").read().splitlines() # Ouverture du fichier et récupération du tableau des lignes
lines = lines[1:] # Retrait des en-têtes situés à la première ligne du fichier (alpha,beta,AngleservoA,AngleservoB,AngleservoC)

# On parcourt l'intégralité des lignes du fichier data.txt
for i in range(0, len(lines)):
    # On sépare les valeurs de chaque ligne en une liste
    values = lines[i].strip().split(',')

    # Ajout des données dans le dictionnaire sous le format suivant:
    # data[alpha,beta]=(angleServoA, angleServoB, angleServoC)
    data[float(values[0]),float(values[1])]=(float(values[2]),float(values[3]),float(values[4]))

print(data)