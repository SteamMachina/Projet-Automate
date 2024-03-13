#---------------------------#
# compter le nombre d'états #
#---------------------------#
def nbr_états(fichier):
    # on ouvre le fichier en mode lecture et on le nomme f
    with open(fichier, "r", encoding="utf-8") as f:
        # on fait une liste de toutes les lignes du fichier
        lignes = f.readlines()
        # on compte le nombre de ligne
        nbr_lignes = len(lignes)
        return nbr_lignes

#----------------------------------#
# compter le nombre de transitions #
#----------------------------------#
def nbr_transitions(fichier):
    # on ouvre le fichier en mode lecture et on le nomme f
    with open(fichier, "r", encoding="utf-8") as f:
        nbr_transitions = 0
        # on stock les lignes dans une liste
        line = f.readline()
        for i in line:
            # en comptant le nombre de séparations entre les informations, on compte le nombre de transitions
            if i == "-":
                nbr_transitions += 1
        return nbr_transitions