file = open("day4\input_g.txt", "r")
lista = file.readlines()
counter = 0

def sovrapposizione(a,b,c,d):
    
    if a <= c and b >= d:
        print("trovato")
        return 1
    elif c <= a and d >= b:
        print("trovato")
        return 1
    else:
        return 0

def intersezione(a,b,c,d):
    
    if a <= c and b >= c:
        print("trovato")
        return 1
    elif c <= a and d >= a:
        print("trovato")
        return 1
    else:
        return 0 

for righe in lista:
    a, b = righe.split(",", 1)
    #print(a)
    a1, a2 = a.split("-", 1)
    #print(b)
    b1, b2 = b.split("-", 1)
    a = int(a1)
    b = int(a2)
    c = int(b1)
    d = int(b2)
    print(type(a), type(b), type(c), type(d))
    print(a,b,c,d)

    counter = counter + intersezione(a,b,c,d)

    
print(counter)