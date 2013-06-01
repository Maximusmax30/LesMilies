# -*-coding:Latin-1 -*
import pickle

def ouvrir_compte(pseudo, mot_de_passe):
	pseudo=str(pseudo)
	pseudo=pseudo.capitalize()
	mot_de_passe=str(mot_de_passe)
	try:
		with open('comptes','rb') as fichier:
			load_compte=pickle.Unpickler(fichier)
			compte=load_compte.load()
	except EOFError:
		compte={}
	except FileNotFoundError:
		compte={}
		with open('comptes','wb') as fichier:
			save_compte=pickle.Pickler(fichier)
			save_compte.dump(compte)
	pseudo=str(pseudo)
	pseudo=pseudo.capitalize()
	mot_de_passe=str(mot_de_passe)
	compte[pseudo]=mot_de_passe
	
	with open('comptes','wb') as fichier:
		save_compte=pickle.Pickler(fichier)
		save_compte.dump(compte)
def verifie_compte(pseudo, mot_de_passe):
	pseudo=str(pseudo)
	pseudo=pseudo.capitalize()
	mot_de_passe=str(mot_de_passe)
	
	with open('comptes','rb') as fichier:
		load_compte=pickle.Unpickler(fichier)
		compte=load_compte.load()
	if pseudo in compte.keys():
		if mot_de_passe==compte[pseudo]:
			return True
		else:
			return False
	else:
		return False