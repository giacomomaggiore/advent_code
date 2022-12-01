#day 1 by giacomo
#cerca l'elemento massinmo nella lista
def cerca_massimo(lista:list):
	massimo = 0
	calorie_elfo = 0
	for i in lista:
		if i != "\n":
			i = int(i) #
			calorie_elfo = calorie_elfo + i
		if i == "\n":
			if calorie_elfo > massimo:
				massimo = calorie_elfo
			calorie_elfo = 0

	return massimo


def cerca_tre_massimi(lista:list):
	lista_calorie = []
	calorie_elfo = 0
	for i in lista:
		if i != "\n":
			i = int(i) #
			calorie_elfo = calorie_elfo + i
		if i == "\n":
			lista_calorie.append(calorie_elfo)
			calorie_elfo = 0


	max1 = max(lista_calorie)
	lista_calorie.remove(max1)
	max2 = max(lista_calorie)
	lista_calorie.remove(max2)
	max3 = max(lista_calorie)
	lista_calorie.remove(max3)

	return max1 + max2 + max3		



file = open("input_g.txt", "r")

lista:list = file.readlines()
for i in lista:
	print(i)

print(cerca_massimo(lista))
print(cerca_tre_massimi(lista))