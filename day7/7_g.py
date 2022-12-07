file = open("day7\input_g.txt")
lista_comandi:list = file.readlines()
directory = []


class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

directory = Tree()
current = Tree()


def aggiungi_directory(Parent, Children):
    Parent.children.append(Children)

def cd(Current):
    current = Current

def inserisci_file(Parent, file):
    Parent.data = file

for line in lista_comandi:
    if "$ ls" in line:
        lista_comandi.remove(line)

for line in lista_comandi:
    
        


print(lista_comandi)