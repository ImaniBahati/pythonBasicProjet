import random
choix = ['Da','Bo','Ma']
score_perdue = 0
score_gagné = 0
score_égalité = 0
score_nul = 0

while True :
	cpu = random.choice(choix)
	joueur = str(input('Veuillez saisir un de ton choix entre Da : Danse, Bo : Boire ou Ma : Manger et pour finir taper Fin : ')).capitalize()
	
	if joueur == cpu:
		print('égalité')
		score_égalité += 1
	
	elif joueur == 'Da' :
		if cpu == 'Bo' :
			print(" vous perdez, on ne peux boire sans danser ")
			score_perdue += 1
		elif cpu == 'Ma' :
			print('vous avez gagné, on mange avant de danser')
			score_gagné += 1
			
	elif joueur == 'Bo' :
		if cpu == 'Da' :
			print(" vous avez gagné, on danse en buvant ")
			score_gagné += 1
		elif cpu == 'Ma' :
			print('vous perdez, on mange avant de boire')
			score_perdue += 1
	
	elif joueur == 'Ma' :
		if cpu == 'Bo' :
			print(" vous avez gagné, on peux boire en mangeant")
			score_gagné += 1
		elif cpu == 'Da' :
			print('vous perdez, on ne danse pas sans manger')
			score_perdue += 1
			
	elif joueur == 'Fin':
		print('resultat :')
		print(f"Hors jeu : {score_nul}")
		print(f"Perdue :{score_perdue}")
		print(f"Gagné :{score_gagné}")
		print(f"Egal :{score_égalité}")
		break
		
	else :
		print("Vous avez choisi ce qu'on t'a pas dit de choisir ")
		score_nul += 1