from fonctions_principales import *

def main():
    #------------------------------------------------#
    # L'uttilisateur choisit quel automate uttiliser #
    #------------------------------------------------#

    nbr_automates = 40
    # mode de saisie sécurisé
    choice = int(input("Choisissez un automate /n"))
    while choice < 1 or choice > nbr_automates:
        print("choix invalid")
        choice = int(input("Choisissez un automate  /n"))

    #-----------------------------#
    # afficher l'automate choisit #
    #-----------------------------#
            
    # selection du fichier automate
    automate_origine = "EX-" + str(choice)  + ".txt"
    # affichage de l'automate
    print("Voici l'automate d'origine : ")
    afficher_automate(automate_origine)

    #----------------------------------------#
    # affichage des propriétés de l'automate #
    #----------------------------------------#

    # standard
    réponse_standard = est_standard(automate_origine) # réponse prend la valeur de "oui" ou de "non"
    print("l'automate est standard : " + réponse_standard)
    # déterministe
    réponse_déterministe = est_déterministe(automate_origine) # réponse prend la valeur de "oui" ou de "non"
    print("l'automate est déterministe : " + réponse_déterministe)
    # déterministe complet
    réponse_déterministe_complet = est_déterministe_complet(automate_origine) # réponse prend la valeur de "oui" ou de "non"
    print("l'automate est déterministe complet : " + réponse_déterministe_complet)
    
    #--------------------------------------#
    # affichage des options sur l'automate #
    #--------------------------------------#

    #--- création des fichiers par defaults ---#
    automate_standard = automate_origine
    automate_déterministe = automate_origine
    automate_déterministe_complet = automate_origine
    automate_minimisé = automate_origine

    #--- Standardisation ---#

    # vérifie si l'automate est deja standard ou pas
    if est_standard(automate_origine) == "non":
        # demande sécurisé pour la standardisation
        choice = int(input("Voulez vous standradiser l'automate ?  /n 0 : non, 1 : oui /n"))
        while choice not in [0, 1] :
            print("choix invalid")
            choice = int(input("Voulez vous standradiser l'automate ?  /n 0 : non, 1 : oui /n"))
        # si l'uttilisateur choisit de standardiser l'automate : 
        if choice == 1:
            # standardisation de l'automate
            automate_standard = standardiser(automate_origine) # automate_standard est un string de nom "automate_standard.txt"
            # affichage de l'automate standardisé
            print("Voici l'automate standardisé : ")
            afficher_automate(automate_standard)

    #--- Déterminisation ---#
            
    # vérifie si l'automate est deja déterminisé ou pas
    if est_déterministe(automate_origine) == "non":
        # demande sécurisé pour la déterminisation
        choice = int(input("Voulez vous déterminiser l'automate ?  /n 0 : non, 1 : oui /n"))
        while choice not in [0, 1] :
            print("choix invalid")
            choice = int(input("Voulez vous déterminiser l'automate ?  /n 0 : non, 1 : oui /n"))
        # si l'uttilisateur choisit de déterminiser l'automate : 
        if choice == 1:
            # déterminisation de l'automate
            automate_déterministe = déterminisation(automate_origine) # automate_déterministe est un string de nom "automate_determinist.txt"
            # affichage de l'automate déterminisé
            print("Voici l'automate déterminisé : ")
            afficher_automate(automate_déterministe)
            # par définition, si l'automate d'origine n'est pas déterminisé, il n'est pas non plus complet
            # donc on remplace le fichier de l'automate deterministe complet (de base l'automate d'origine) par ce nouveau automate déterministe
            automate_déterministe_complet = automate_déterministe

    #--- déterminisation complète ---#
            
    # vérifie si l'automate est deja déterminisé et complet ou pas
    if est_déterministe_complet(automate_déterministe_complet) == "non":
        # demande sécurisé pour la déterminisation complète
        choice = int(input("Voulez vous déterminiser et compléter l'automate ?  /n 0 : non, 1 : oui /n"))
        while choice not in [0, 1] :
            print("choix invalid")
            choice = int(input("Voulez vous déterminiser et compléter l'automate ?  /n 0 : non, 1 : oui /n"))
        # si l'uttilisateur choisit de déterminiser et complété l'automate : 
        if choice == 1:
            # complition de l'automate déja déterminisé
            automate_déterministe_complet = complition(automate_déterministe) # automate_déterministe_complet est un string de nom "automate_determinist_complet.txt"
            # affichage de l'automate déterminisé
            print("Voici l'automate déterminisé complet : ")
            afficher_automate(automate_déterministe_complet)

    #--- minimisation ---#
    choice = int(input("Voulez vous minimiser l'automate ?  /n 0 : non, 1 : oui /n"))
    while choice not in [0, 1] :
        print("choix invalid")
        choice = int(input("Voulez vous minimiser l'automate ?  /n 0 : non, 1 : oui /n"))
    # si l'uttilisateur choisit de voir le complément de l'automate : 
    if choice == 1:
        # création de la minimisation de l'automate
        automate_minimisé = minimisation(automate_déterministe_complet) # automate_minimisé est un string de nom "automate_minimisé.txt"
        # affichage de l'automate minimisé
        print("Voici l'automate minimisé : ")
        afficher_automate(automate_minimisé)

    #--- complémentarisation ---#
    
    # demande sécurisé pour la complémentarisation
    choice = int(input("Voulez vous le complément de l'automate ?  /n 0 : non, 1 : oui /n"))
    while choice not in [0, 1] :
        print("choix invalid")
        choice = int(input("Voulez vous le complément de l'automate ?  /n 0 : non, 1 : oui /n"))
    # si l'uttilisateur choisit de voir le complément de l'automate : 
    if choice == 1:
        # création du complément de l'automate
        automate_complémentaire = complémentarisation(automate_minimisé) # automate_complémentaire est un string de nom "automate_complémentaire.txt"
        # affichage de l'automate complémentaire
        print("Voici l'automate complémentaire : ")
        afficher_automate(automate_complémentaire)