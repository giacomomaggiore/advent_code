file = open("input_g.txt", "r")
lista = file.readlines()
punteggio = 0
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
print(punteggio)