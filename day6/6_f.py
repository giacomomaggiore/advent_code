def funct(string:str, chars:int):

    for i in range(len(string)-chars):

        l = []

        for j in range(chars-1):
            a = string[i:i+chars].count(string[i+j])
            if a !=1:
                l.append(a)
        
        if len(l) == 0:
            return i+chars
        

file = open("input_f.txt", "r")

string = file.readline()

res1 = funct(string,4)

res2 = funct(string, 14)

print(res1)
print(res2)