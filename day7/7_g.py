file = open("input_g.txt")
lista_comandi:list = file.readlines()
for line in lista_comandi:
    if "ls" in line:
        print("eliminato")
        lista_comandi.pop(lista_comandi.index(line))


class Tree:
    def __init__(self, nome):
        self.name = nome
        self.children = []
        self.data = 0 

dir = Tree("root")
current = dir

def aggiungi(Parent, nome):
    temp = Tree(nome)
    temp.name = nome

    Parent.children.append(temp)

def file(Current, file):
    Current.data = Current.data + file
    #print(Current.data)

def cd(Current, nome):
    for sottocartelle in Current.children:
        if sottocartelle.name == nome:
            temp = sottocartelle

def calcola(Directory):
    dimensione = 0
    if len(Directory.children) == 0:
        #print("vuoto")
        dimensione = Directory.data
        #print(dimensione)
    else:
        #print("Non vuoto")
        for sottocartelle in  Directory.children:
        
            dimensione = dimensione + calcola(sottocartelle)
        
    
    return dimensione
    

for line in lista_comandi:
    if "dir" in line:
        print("sto facendo una nuova dir\n")
        nome = line[5:]
        aggiungi(current,nome)

    elif "cd" in line:
        print("Cambiando directory\n")
        nome = line[5:]
        aggiungi(current, nome)
        cd(current, nome)

    elif "ls" not in line and "dir" not in line:
        
        nome = line.split(" ", 1)[0]
        print("creando il file ", nome, "\n")
        numero = int(nome)
        #print(numero)
        file(current, numero)
    else:
        print(line)
   
