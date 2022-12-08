file = open("day8\input_g.txt")
counter = 0
righe = file.readlines()

for line in righe:
    counter = counter + 2

print(counter)
print("\n")


for elementi in range(len(righe[0])-2):
    counter = counter + 2

print(counter)
print("\n")

i = 1
j = 1

def visibile_riga(riga):
    i = 1
    j = 0
    flag = 0 
    while i < len(riga)-1:
        while j < len(riga)-1:
            if i != j:
                if int(riga[i]) <= int(riga[j]):
                    print(riga[i], riga[j], "non visibile\n")
                    
                    return 0
                    
                    
                    

            j = j + 1
        print(riga[i], "VISIBILE\n")
        return 1
        
        i = i +1
    
    return 0  

def visibile_colonna(riga):    
    i = 1
    j = 0
    while i < len(riga)-1:
        while j < len(righe):
            if i != j:
                if riga[i] < righe[i][j]:
                    print("albero non visibile")
                    return 0
            j = j + 1
        
        print("visibile colonna")
        i = i + 1
    
    return 1
    
i = 1
for line in righe:
    visibile_riga = visibile_riga(line)
    visibile_colonna = visibile_colonna(line)

print(counter)