file = open("day7\input_g.txt")
lista_comandi:list = file.readlines()
for line in lista_comandi:
    if "ls" in line:
        lista_comandi.pop(lista_comandi.index(line))


class Tree():
    def __init__(self, nome):
        self.name = nome
        self.children = []
        self.data = 0

    def dir(self, nome):
        cartella = Tree(nome)
        self.children.append(cartella)
    
    def file(self, numero):
        self.data = self.data + numero

dir = Tree("Root")
current = dir
totale = 0
    
def calcola(Directory):
    dimensione = 0
    if not Directory.children:
        print("vuoto")
        dimensione = Directory.data
        #print(dimensione)
    else:
        #print("Non vuoto")
        for sottocartelle in  Directory.children:
        
            dimensione = dimensione + calcola(sottocartelle)
    
    print(dimensione)
    return dimensione
    
    
    

for line in lista_comandi:
    if "dir" in line:
        nome = line[5:]
        print("Creando cartella ", nome, " nella directory ", current.name)

        current.dir(nome)

    elif "cd" in line:
        
        nome = line[5:]
        
        
        for cartelle in current.children:
            if cartelle.name == nome:
                current = cartelle

    elif "ls" not in line and "dir" not in line:
        
        nome = line.split(" ", 1)[0]
        print("creando il file ", nome, "\n")
        numero = int(nome)
        #print(numero)
        current.file(numero)
    else:
        print(line)

totale = 0

def somma_dimensioni(Directory):
    global totale
    for cartelle in Directory.children:
        if calcola(cartelle) >= 10000:
            totale = totale + calcola(cartelle)
            print(totale)
            somma_dimensioni(Directory)
    

    return totale
        
        


calcola(dir)
somma_dimensioni(dir)
