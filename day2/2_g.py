#APERTURA FILE DI INPUT
#su ogni riga ci sono due caratteri che denotano i simboli carta forbice e sasso
file = open("input2_g.txt", "r")

#LETTERE DEL PRIMO GIOCATORE
rock = "A"
paper = "B"
scissors = "C"

#LETTERE DEL SECONDO GIOCATORE
rock_o = "X"
paper_o = "Y"
scissors_o = "Z"

#PARTE DUE VALORI
vittoria = "Z"
pareggio = "Y"
sconfitta = "X"


#PUNTEGGI
punteggio_rock = 1
punteggio_paper = 2
punteggio_scissors = 3

punteggio_draw = 3
punteggio_win = 6

punteggio_totale = 0
punteggio_totale_2 = 0

def assegna_vincita(partita:list):
    score = 0

    if partita[1] == rock_o:
        score = score + punteggio_rock
        if partita[0] == rock:
            score = score + punteggio_draw
        elif partita[0] == scissors:
            score = score + punteggio_win
    
    elif partita[1] == paper_o:
        score = score + punteggio_paper
        if partita[0] == rock:
            score = score + punteggio_win
        elif partita[0] == paper:
            score = score + punteggio_draw
            
    elif partita[1] == scissors_o:
        score = score + punteggio_scissors
        if partita[0] == paper:
            score = score + punteggio_win
        elif partita[0] == scissors:
            score = score + punteggio_draw

    return score

def guarda_mosse(mossa_1, mossa_2):
    return [mossa_1, mossa_2]

def parte_due(partita):
    punteggio_due = 0

    if partita[1] == vittoria: #VITTORIA PER ME
        if partita[0] == paper:
            punteggio_due =assegna_vincita([paper, scissors_o])
        
        elif partita[0] == rock:
            punteggio_due =assegna_vincita([rock, paper_o])
            
        elif partita[0] == scissors:
            punteggio_due =assegna_vincita([scissors, rock_o])


    if partita[1] == pareggio: #PAREGGIO PER ME
        if partita[0] == paper:
            punteggio_due =assegna_vincita([paper, paper_o])
            
        elif partita[0] == rock:
            punteggio_due =assegna_vincita([rock, rock_o])

        elif partita[0] == scissors:
            punteggio_due =assegna_vincita([scissors, scissors_o])

    if partita[1] == sconfitta: #SCONFITTA PER ME
        if partita[0] == paper:
            punteggio_due =assegna_vincita([paper, rock_o])

        elif partita[0] == rock:
            punteggio_due =assegna_vincita([rock, scissors_o])

        elif partita[0] == scissors:
            punteggio_due =assegna_vincita([scissors, paper_o])

    print(punteggio_due)
    return punteggio_due

lista_partite:list = (file.readlines())
for partita in lista_partite:
    
    #variabile temporanea
    match = guarda_mosse(partita[0], partita[2])
    
    punteggio_totale = punteggio_totale + assegna_vincita(match)

for partita in lista_partite:

    match = guarda_mosse(partita[0], partita[2])

    punteggio_totale_2 = punteggio_totale_2 + parte_due(match)

print(punteggio_totale_2)