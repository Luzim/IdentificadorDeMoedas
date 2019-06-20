from operator import itemgetter
##CODIGO NÃO FUNCIONAL AINDA
def mountListCoins():
	coins = []
	coinsName = ['1 centavo','5 centavos'] #'10 centavos','25 centavos']
	list_coins = []
	coins.append(3.1415*((17.0/2.0)**2.0))
	coins.append(3.1415*((22.0/2.0)**2.0))
	#coins.append(3.1415*((20.0/2.0)**2.0))
	#coins.append(3.1415*((25.0/2.0)**2.0))

	for i in range(2):
		for j in range(2):
			aux_coin = (coinsName[i],coinsName[j])
			escala_coin = coins[i]/coins[j]
			list_coins.append((aux_coin,escala_coin))
	list_coins = sorted(list_coins, key=itemgetter(1))
	return list_coins

def compareColor(a,b,color):

	if (color == 'bronze'):
		if a > b:
			return '5 centavos','1 centavo'
		else:
			return '1 centavo','5 centavos'
	elif (color == 'ouro'):
		if a > b:
			return '25 centavos','10 centavos'
		else:
			return '10 centavos','25 centavos'
	else:
		if a > b:
			return '1 real','50 centavos'
		else:
			return '50 centavos','1 real'

def select_color(a):
	if (a >= 8 and a <= 14):
		return 'bronze'
	elif (a >=15 and a <= 23):
		return 'ouro'
	else:
		return 'prata'
def compareCoins(a,b,listCoins):
	c = a/b;
	for i in range(len(listCoins)):
		if(c < listCoins[i][1]):
			if i == 0:
				print(listCoins[i][1])
				return listCoins[i][0][0],listCoins[i][0][1]
			else:
				aux_a = listCoins[i][1]-c
				aux_b = c - listCoins[i-1][1]
				if aux_a < aux_b:
					print(listCoins[i][1])
					return listCoins[i][0][0],listCoins[i][0][1]
				else:
					print(listCoins[i-1][1])
					return listCoins[i-1][0][0],listCoins[i-1][0][1]
	print(listCoins[len(listCoins)-1][1])
	return listCoins[len(listCoins)-1][0][0],listCoins[len(listCoins)-1][0][1]

list_result = mountListCoins()
moeda_1,moeda_2 = compareCoins(33751.0,41696.0,list_result)
print(moeda_1 + " - "+moeda_2)
moeda_1,moeda_2 = compareCoins(28676.0,33751.0,list_result)
print(moeda_1 + " - "+moeda_2)
#moeda_1,moeda_2 = compareCoins(32020.0,27121.0,list_result)
#print(moeda_1 + " - "+moeda_2)