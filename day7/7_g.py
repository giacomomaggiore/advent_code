file = open("day7\input_g.txt")
lista_comandi:list = file.readlines()
lista_comandi_reverse = lista_comandi.reverse()



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
        pass
    elif "cd" in line:
        pass
    elif "ls" in line:
        pass
    else:
        pass

