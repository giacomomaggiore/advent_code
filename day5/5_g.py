file = open("input_g.txt")
lista = [[" " for x in range(8)] for y in range(9)] 
righe = [[" " for x in range(9)] for y in range(8)]
colonne = [[" " for x in range(8)] for y in range(9)]
comandi_lista = [[0,0,0] for x in range(501)]

j = 1
k = 0
for i in range(8):
	stringa = file.readline()
	#print(stringa)
	j = 1
	a = 0
	while j < 36:
		righe[k][a] = ((stringa[j]))
		j = j + 4
		a = a + 1

	k = k + 1
#print(len(righe))
#print(righe)


i = 0
j = 0
k = 0
while i < 8:
	k = 0
	j = 0
	while j < 9:
		colonne[j][i] = righe[i][j]
		j = j + 1
	i = i + 1
print("\n")
for i in colonne:
	i = i.reverse()


file.readline()
file.readline()

k = 0
comandi = file.readlines()
for comando in comandi:
	comando = comando.replace("move", " ")
	comando = comando.replace("from","")
	comando = comando.replace("to","")
	comando = comando[2: len(comando)]


	a,b,c = comando.split("  ")
	#a,b,c = comandi_lista[k]
	
	comandi_lista[k][0] = int(a)
	comandi_lista[k][1] = int(b)
	comandi_lista[k][2] = int(c)
	k = k + 1

	#print(comando)
	#print(comando[-2]) #ultimo numero


def elimina(colonne): 
	for colonna in colonne:
		print(colonna)

		i = len(colonna) -1
		while i >= 0:
			if colonna[i] == " ":
				colonna.pop(i)
			i = i -1
elimina(colonne)
print(colonne)

def trova_ultimo(lista:list):
	i = len(lista)-1
	
	while i >= 0:
		#print(type(lista[i]))
		if lista[i] != " ":
			return i
			i = i - 1

def sposta(colonna1, colonna2):
	temp = len(colonna1)-1
	print(colonna1, temp)
	
	colonna2.append(colonna1[temp])
	colonna1.pop(temp)
	
for istruzione in comandi_lista:
	#print(istruzione)
	for volte in range(istruzione[0]):
		a = istruzione[1]-1
		b = istruzione[2]-1
		#print(a,b)
		#print(istruzione[1], istruzione[2])
		#print(colonne[a], colonne[b])
		sposta(colonne[a], colonne[b])
		#print(colonne)

def trova_ultimo_2(lista:list):
	i = len(lista)-1
	#print(lista[0])

	while i >= 0:
		if lista[i] != " ":
			
			return lista[i]
		#print(type(lista[i]))
			
		i = i -1
		
#print(colonne)
risultato = []
i = 0
while i < len(colonne):
	#print(colonne[i])
	temp = trova_ultimo_2(colonne[i])
	risultato.append(temp)
	i = i + 1

#print(colonne)
#print(risultato)
	
risultato_stringa = ""
for x in risultato:
	risultato_stringa = risultato_stringa + x

print(risultato_stringa)