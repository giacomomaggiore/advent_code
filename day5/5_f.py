def first_part(path:str):

    col:list = [[]]
    stack = []

    file=open(path, "r")

    for i in range(8):
        stack.append(file.readline())
    
    for i in range(1,35,4):
        buff = []
        for line in stack:
            if line[i] != " ":
                buff.append(line[i])
                
        buff.reverse()
        col.append(buff)

    moves = []

    rude_moves = file.readlines()
    rude_moves = rude_moves[2:]

    for x in rude_moves:
        buff_moves = ()
        buff_moves=x.split(" ")
        moves.append(buff_moves)

    how_many = []
    fromm =  []
    to = []
    
    for x in moves:
        how_many.append(x[1])
        fromm.append(x[3])
        to.append(x[5])

    print(col)

    for i in range(len(how_many)):
        x = int(how_many[i])
        a = int(fromm[i])
        b = int(to[i])

        for j in range(x):
            col[a].reverse()
            col[b].append(col[a][0])
            col[a].reverse()
            col[a].pop()
        
    res = ""

    for i in col:
        i.reverse()
        if len(i)>0:
            res = res + i[0]
    print("\n\n\n\n\n"+res)

    
def second_part(path:str):

    col:list = [[]]
    stack = []

    file=open(path, "r")

    for i in range(8):
        stack.append(file.readline())
    
    for i in range(1,35,4):
        buff = []
        for line in stack:
            if line[i] != " ":
                buff.append(line[i])
                
        buff.reverse()
        col.append(buff)

    moves = []

    rude_moves = file.readlines()
    rude_moves = rude_moves[2:]

    for x in rude_moves:
        buff_moves = ()
        buff_moves=x.split(" ")
        moves.append(buff_moves)

    how_many = []
    fromm =  []
    to = []
    
    for x in moves:
        how_many.append(x[1])
        fromm.append(x[3])
        to.append(x[5])

    for i in range(len(how_many)):
        x = int(how_many[i])
        a = int(fromm[i])
        b = int(to[i])

        var:list = col[a][-x:]

        for j in var:
            col[b].append(j)
        
        for s in range(x):
            col[a].pop()
    
    res = ""
    for k in col:
        k.reverse()
        if len(k)>0:
            res = res+ k[0]
    
    print("\n\n\n\n"+ res)


        







second_part("input_f.txt")