file = open("input_g.txt", "r")
lista = file.readlines()

lista_gruppi = [[0 for x in range(3)] for y in range(len(lista)//3)] 
print(len(lista_gruppi))

punteggio = 0
punteggio2 = 0


def dividi_lista(lista):
    lunghezza = len(lista)

def cerca_duplicato(stringa):
    string1 = stringa[0: len(stringa)//2]
    string2 = stringa[len(stringa)//2:len(stringa)]
    for i in range(len(string1)):
        for j in range(len(string2)):
            if string1[i] == string2[j]:
                return string1[i]


def priorita(n):
    if ( ord(n) >= 97 and ord(n) <= 122 ):
        return ord(n) - 96
    if ( ord(n) >= 65  and ord(n) <= 90):
        return (ord(n)) - 65 + 27 

for stringhe in lista:
    punteggio = punteggio + priorita(cerca_duplicato(stringhe))

i = 0
while i < len(lista)/3:
    lista_gruppi[i][0] = lista[i*3]
    lista_gruppi[i][1] = lista[i*3+1]
    lista_gruppi[i][2] = lista[i*3+2]

    i = i+1

print(lista_gruppi[0][0])

i = 0
while i < len(lista_gruppi):
    dim = max(len(lista_gruppi[i][0]),len(lista_gruppi[i][1]),len(lista_gruppi[i][2]))
    for a in lista_gruppi[i][0]:
        if a != "\n":
            for b in lista_gruppi[i][1]:
                if b != "\n" and a == b:
                    for c in lista_gruppi[i][2]:
                        if a != "\n" and b != "\n" and c != "\n":
                            if a == b and a == c and b == c:
                                prov = a
    
    print(prov, i)

    punteggio2 = punteggio2 + priorita(prov)
    i = i + 1

print(punteggio2)