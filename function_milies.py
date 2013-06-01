# -*-coding:Latin-1 -*
import pickle
from characteristique_milies import *
def sauvegarder_milies(pseudo, liste_player_milies):
	pseudo=str(pseudo)
	pseudo=pseudo.capitalize()
	player_milies=pseudo+"_milies"
	try :
		with open(player_milies,'wb') as fichier:
			save_milies=pickle.Pickler(fichier)
			save_milies.dump(liste_player_milies)
	except:
		liste_player_milies=[]
def charger_milies(pseudo):
	pseudo=str(pseudo)
	pseudo=pseudo.capitalize()
	player_milies=pseudo+"_milies"
	try :
		with open(player_milies,'rb') as fichier:
			load_milies=pickle.Unpickler(fichier)
			milies_player=load_milies.load()
	except:
		milies_player=["Place1","Place2","Place3"]
	return milies_player
def changement_milies(milies_a_changer,new_milies,place_in_liste_joueur,liste_player_milies,liste_milies):
	milies_a_changer=str(milies_a_changer)
	milies_a_changer=milies_a_changer.lower()
	milies_a_changer=milies_a_changer.capitalize()
	new_milies=str(new_milies)
	new_milies=new_milies.lower()
	new_milies=new_milies.capitalize()
	try:
		place_in_liste_joueur=int(place_in_liste_joueur)
	except  ValueError:
		print("ERROR : La place doit être un chiffre.")
		return liste_player_milies
	try:
		if place_in_liste_joueur>3 or place_in_liste_joueur<0:
			print("ERROR : Il ni a que 3 place dans la liste.")
			return liste_player_milies
		else:
			if new_milies in liste_milies:
				try:
					liste_player_milies.remove(milies_a_changer)
				except:
					print("Ce milies n'est pas dans votre liste")
					return liste_player_milies
				liste_player_milies.insert(place_in_liste_joueur,new_milies)
				return liste_player_milies
			else:
				print("ERROR : ce milies n'existe pas.")
				return liste_player_milies
	except TypeError:
		print("Error : La position doit être un chiffre !")
		return liste_player_milies