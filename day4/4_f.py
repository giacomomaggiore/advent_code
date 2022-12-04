def firstPart(lines:list):

    leftlist = []
    rightlist = []

    for line in lines:
        leftlist.append(line.split(",")[0])
        rightlist.append(line.split(",")[1])


    
    i=0
    intersections = 0

    for el in leftlist:
        
        er = rightlist[i]

        if (int(el.split("-")[0]) <= int(er.split("-")[0])) and (int(el.split("-")[1]) >= int(er.split("-")[1])):
            intersections += 1
        elif (int(el.split("-")[0]) >= int(er.split("-")[0])) and (int(el.split("-")[1]) <= int(er.split("-")[1])):
            intersections += 1

        i+=1

    return intersections, leftlist, rightlist

def secondPart(leftlist:list, rightlist:list):

    overlap = 0
    i=0

    el:str

    for a in leftlist:

        b:str = rightlist[i]

        el = a.split("-")
        er = b.split("-")

        el[0] = int(el[0])
        el[1] = int(el[1])
        er[0] = int(er[0])
        er[1] = int(er[1])

        if el[1] >= er[0] and el[1]<= er[1]:
            overlap+=1
        elif el[0] >= er[0] and el[0]<= er[1]:
            overlap+=1
        elif er[1] >= el[0] and er[1] <= el[1]:
            overlap+=1
        elif er[0] >= el[0] and er[0] <= el[1]:
            overlap +=1
        else:
            print(el + er)

        i+=1

    return overlap

file = open("input_f.txt", "r")

lines = file.readlines()

sol = firstPart(lines)

print(sol[0])

print(secondPart(sol[1], sol[2]))
