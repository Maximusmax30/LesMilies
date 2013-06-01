# -*-coding:Latin-1 -*
import os # On importe le module os
import pickle
from gestion_compte import *
from function_milies import *
from liste_milies import *
from commandes_milies import *
from characteristique_milies import *
from random import randrange
os.chdir("D:/programme/Python/PROJET/Les Milies")
print("Bienvenue sur le jeu des Milies alpha0.1")
continue_partie=True
continuer_partie=True
changement="1"
while continue_partie==True:
        print("Menu :")
        print("1 : Jouer")
        print("2 : Voir les Milies")
        print("3 : Creer un compte")
        print("4 : Quitter")
        choix=input("Votre choix :")
        try:
                choix=int(choix)
        except ValueError:
                print("Votre choix doit être un chiffre !")
        if choix==4:
                continue_partie=False
        if choix==3:
                pseudo=input("Votre pseudo : ")
                mdp=input("Votre mot  de passe : ")
                compte=ouvrir_compte(pseudo, mdp)
        if choix==2:
                print("----------------")
                for elt in milies:
                        print("{}".format(elt))
                print("----------------")
        if choix==1:
                verification_compte_j1=False
                verification_compte_j2=False
                while verification_compte_j1==False:
                        pseudo_j1=input("Votre pseudo J1 : ")
                        mdp_j1=input("Votre mot  de passe J1: ")
                        verification_compte_j1=verifie_compte(pseudo_j1, mdp_j1)
                liste_j1_milies=charger_milies(pseudo_j1)#fonction a def voir le prog sur gestion mdp pour aide.
                sauvegarder_milies(pseudo_j1, liste_j1_milies)
                while verification_compte_j2==False:
                        pseudo_j2=input("Votre pseudo J2 : ")
                        mdp_j2=input("Votre mot  de passe J2: ")
                        verification_compte_j2=verifie_compte(pseudo_j2, mdp_j2)
                liste_j2_milies=charger_milies(pseudo_j2)#fonction a déf
                sauvegarder_milies(pseudo_j2, liste_j2_milies)
                print("Connexion des deux comptes effectué !")
                while continuer_partie==True:
                        print("Menu :")
                        print("1 : Lancer partie")
                        print("2 : Changer Milies J1")
                        print("3 : Changer Milies J2")
                        choix=input("Votre choix :")
                        try:
                                choix=int(choix)
                        except ValueError:
                                print("Votre choix doit être un chiffre !")
                        if choix==2:
                                changer_milies=True
                                print("----------------")
                                for elt in milies:
                                        print("{}".format(elt))
                                        print("----------------")
                                while changer_milies==True:
                                        print(liste_j1_milies)
                                        milies_a_changer=input("Entrez le nom du Milies que vous voulez échanger : ")
                                        new_milies=input("Entrez le nom du Milies à ajouter : ")
                                        place_liste_j1=input("En quel position doit-il être ? (1 à 3)")
                                        liste_j1_milies=changement_milies(milies_a_changer,new_milies,place_liste_j1,liste_j1_milies,milies)
                                        choix=input("En changer un autre ? (o/n)")
                                        choix=choix.upper()
                                        if choix=="O":
                                                sauvegarder_milies(pseudo_j1, liste_j1_milies)
                                        else:
                                                changer_milies=False
                                                sauvegarder_milies(pseudo_j1, liste_j1_milies)
                                                print("Vos choix on bien été sauvegardé !")
                        if choix==3:
                                changer_milies=True
                                print("----------------")
                                for elt in milies:
                                        print("{}".format(elt))
                                        print("----------------")
                                while changer_milies==True:
                                        print(liste_j2_milies)
                                        milies_a_changer=input("Entrez le nom du Milies que vous voulez échanger : ")
                                        new_milies=input("Entrez le nom du Milies à ajouter : ")
                                        place_liste_j2=input("En quel position doit-il être ? (1 à 3)")
                                        liste_j2_milies=changement_milies(milies_a_changer,new_milies,place_liste_j2,liste_j2_milies,milies)
                                        choix=input("En changer un autre ? (o/n)")
                                        choix=choix.upper()
                                        if choix=="O":
                                                sauvegarder_milies(pseudo_j2, liste_j2_milies)
                                        else:
                                                changer_milies=False
                                                sauvegarder_milies(pseudo_j2, liste_j2_milies)
                                                print("Vos choix on bien été sauvegardé !")
                        if choix==1:
                                cmd=CommandMilies()
                                choix_milies=input("blabla: ")
                                print("|-----------------------------|")
                                print("|Charactéristique de",choix_milies)
                                print("|-----------------------------|")
                                for cle, valeur in griffal.items():
                                        print("|{} : {}".format(cle, valeur))
                                print("|-----------------------------|")
                                                        
                                                        
                                                        
                                                        
os.system("pause")
