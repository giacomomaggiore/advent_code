#apro file

file = open("input.txt", "r")

lista:list = file.readlines()

sum = 0

listasomme = []
top3 = []

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
	top3.append(buff)
	sum += buff

print(sum)


		