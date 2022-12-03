def calcolaPunteggio(chars:list):

    tot = 0

    for char in chars:
        if ord(char) >= ord('a') and  ord(char) <= ord('z'):
            tot += (ord(char)-96)
        else:
            tot += (ord(char)-64+26)

    return tot

def firstPart(lines:list):

    chars = []

    for line in lines:
        ln = len(line)
        ln = int(ln/2)

        part1 = line[:ln]
        part2 = line[ln:]

        for i in range(ln):
            if part1[i] in part2:
                chars.append(part1[i])
                break


    return calcolaPunteggio(chars)

def secondPart(lines:list):

    chars = []

    lines = dividiInput(lines)

    for line in lines:
        minor = min(line, key=len)
        print(minor)

        for i in range(len(minor)-1):
            if (minor[i] in line[0]) and (minor[i] in line[1]) and (minor[i] in line[2]):
                chars.append(minor[i])
                break

    print(chars)
        
    return calcolaPunteggio(chars)

def dividiInput(lines:list):
    newlines = []
    
    buff = ()

    for i in range(len(lines)):

        if i%3 == 0:
            buff = (lines[i], lines[i+1], lines[i+2])
            print(buff)
            newlines.append(buff)
    
    return newlines


file = open("input_f.txt")

lines = file.readlines()

res = firstPart(lines)

res2 = secondPart(lines)

print(res)

print(res2)