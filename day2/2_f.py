rock = "A"
paper = "B"
scissor = "C"

rock_2 = "X"
paper_2 = "Y"
scissor_2 = "Z"

value_rock = 1
value_paper = 2
value_scissor = 3
win = 6

WIN = "Z"
LOSE = "X"
DRAW = "Y"

def calcola_punteggio(strs:str):

    if strs == rock:
        return value_rock
    elif strs == paper:
        return value_paper
    else:
        return value_scissor

def second_part(lines:list):

    tot = 0


    for line in lines:
        #caso in cui bisogna pareggiare
        if line[2] == DRAW:
            tot = tot + calcola_punteggio(line[0]) + 3
        
        elif line[2] == WIN:
            tot += 6
            if line[0] == rock:
                tot += value_paper
            
            elif line[0] == paper:
                tot += value_scissor
            
            elif line[0] == scissor:
                tot += value_rock
        
        else:
            if line[0] == rock:
                tot += value_scissor
            
            elif line[0] == paper:
                tot += value_rock
            
            elif line[0] == scissor:
                tot += value_paper
                
    return tot

def who_won(lines:list):

    total = 0

    for line in lines:
        lost = False
        draw = False

        if line[0] == rock and line[2] == rock_2:
            total = total + value_rock
            draw = True

        elif line[0] == paper and line[2] == paper_2:
            total = total + value_paper
            draw = True

        elif line[0] == scissor and line[2] == scissor_2:
            total = total + value_scissor
            draw = True


        #casi perde
        if not draw:
            if line[0] == rock and line[2] == scissor_2:
                total = total + value_scissor
                lost = True

            elif line[0] == paper and line[2] == rock_2:
                total = total + value_rock
                lost = True

            elif line[0] == scissor and line[2] == paper_2:
                total = total + value_paper
                lost = True

        #casi vince
        
        if not lost and not draw:
            total += 6

            if line[2] == scissor_2:
                total = total + value_scissor

            elif line[2] == rock_2:
                total = total + value_rock

            elif line[2] == paper_2:
                total = total + value_paper

        if draw:
            total += 3


    return total


file = open("input_f.txt", "r")

lines = file.readlines()

total = who_won(lines)

tot = second_part(lines)

print(total)
print(tot)
        

