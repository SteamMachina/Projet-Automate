from fonctions_secondaires import *

#----------------------#
# afficher un automate #
#----------------------#
def afficher_automate(automate):
    pass

#-------------------------------------#
# vérifier si l'automate est standard #
#-------------------------------------#
def est_standard(automate): # return "oui" ou "non"
    pass

#-----------------------------------------#
# vérifier si l'automate est déterministe #
#-----------------------------------------#
def est_déterministe(automate): # return "oui" ou "non"
    pass

#-------------------------------------------------#
# vérifier si l'automate est déterministe complet #
#-------------------------------------------------#
def est_déterministe_complet(automate) : # return "oui" ou "non"
    # ssi l'automate est déterministe, on peut le compléter
    if est_déterministe(automate) == "oui":
        # on ouvre le fichier en mode lecture et on le renomme "a"
        with open(automate, "r", encoding="utf-8") as a:
            # on crée une liste des différentes lignes du fichier
            for i in range(nbr_états(automate)):
                # pour chaque ligne on crée des sous liste des mots séparés par un "-"
                mots = a.readline().split("-")
                # on verifie que chaque état mène à un autre état pour quaque transition
                for i in range(1, len(mots)):
                    # si le mot est vide, cela signifie qu'il manque une transition
                    if mots[i].strip() == "":
                        # s'il manque une transition, l'automate n'est pas complet
                        return "non"
        # si l'algorithme n'a pas constaté de mot vide, cela signifie que chaque état mène à un autre état pour chaque transition
        # donc l'automate est complet
        return "oui"
    
#-------------------------------------#
# vérifier si l'automate est minimisé #
#-------------------------------------#
def est_minimisé(automate):
    pass

#-------------------------#
# standardiser l'automate #
#-------------------------#
def standardiser(automate):
    pass

#-------------------------#
# determiniser l'automate #
#-------------------------#
def déterminisation(automate):
    pass

#---------------------------------------#
# complition d'un automate déterministe #
#---------------------------------------#
def complition(automate):
    pass

#-----------------------------------------#
# mininisation d'un automate déterministe #
#-----------------------------------------#
def minimisation(automate):
    pass

#-----------------------------------#
# complémentarisation de l'automate #
#-----------------------------------#
def complémentarisation(automate):
    pass