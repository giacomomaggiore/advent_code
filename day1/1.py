#apro file

file = open("input.txt", "r")

lista:list = file.readlines()

sum = 0

listasomme = []

for line in lista:

	if line != "\n":
		sum += int(line)


	else:
		listasomme.append(sum)
		sum = 0

sum=0
for i in range(3):
	buff = max(listasomme)
	listasomme.remove(buff)
	sum += buff

print(sum)


		