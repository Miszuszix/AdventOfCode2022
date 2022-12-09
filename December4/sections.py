file = open('sections.txt')
j = 0
contains = 0
string = ""
for i in file:
                tab1 = []
                tab = []
                string = ""
                i = i.strip()
                j+=1
                for k in i:
                    if(k != ","):
                        string += k
                    else:
                        tab.append(string)
                        string = ""
                tab.append(string)
                for k in tab:
                    index = k.index("-")
                    left = k[:index]
                    right = k[index + 1:]
                    tab1.append(int(left))
                    tab1.append(int(right))
##                if(tab1[0] >= tab1[2] and tab1[1] <= tab1[3]):
##                    contains += 1
##                elif(tab1[2] >= tab1[0] and tab1[3] <= tab1[1]):
##                    contains += 1
                if(tab1[0] >= tab1[2] and tab1[0] <= tab1[3]):
                        contains += 1
                elif(tab1[1] >= tab1[2] and tab1[1] <= tab1[3]):
                        contains += 1
                elif(tab1[2] >= tab1[0] and tab1[2] <= tab1[1]):
                        contains+= 1
                elif(tab1[3] >= tab1[0] and tab1[3] <= tab1[1]):
                        contains += 1
print(contains)











