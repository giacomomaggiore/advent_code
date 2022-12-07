file = open("day7\input_g.txt")
lista_comandi:list = file.readlines()
lista_comandi_reverse = lista_comandi.reverse()
for line in lista_comandi:
    if "ls" in line:
        lista_comandi.remove(line)


class Tree:
    def __init__(self, nome):
        self.name = nome
        self.children = []
        self.data = 0 

dir = Tree("root")
current = dir

def aggiungi(Parent, nome):
    temp = Tree()
    temp.name = nome

    Parent.children.append(temp)

def file(Current, file):
    Current.data = Current.data + file


def cd(Current, nome):
    temp = Current.children[Current.children.index(nome)]

for line in lista_comandi:
    if "dir" in line:
        nome = line[5:]
        aggiungi(nome)

    elif "cd" in line:
        nome = line[3:]
        cd(current, nome)

    elif "ls" not in line and "dir" not in line:
        nome = line.split(" ", 1)[0]
        numero = int(nome)
        file(current, numero)
   
