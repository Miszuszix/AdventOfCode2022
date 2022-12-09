file = open('substream.txt')
substream = False
bound = 14
n = 0
for i in file:
    for j in range(len(i) - 3):
        string = i[j:j+bound]
        for k in range(bound):
            if(string.count(string[k]) == 1):
                substream = True
            else:
                substream = False
                break
        n += 1
        if(substream == True):
            print(n + 13)
            break
            
