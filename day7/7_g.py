file = open("day7\input_g.txt")
lista_comandi:list = file.readlines()
for line in lista_comandi:
    if line[0:3] == "$ ls":
        lista_comandi.remove(line)

    
print(lista_comandi)