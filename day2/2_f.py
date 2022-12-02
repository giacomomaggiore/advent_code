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

print(total)
        

