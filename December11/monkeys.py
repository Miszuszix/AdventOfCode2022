file = open('monkeys.txt')
k = 0
monkeys = []
items = []
operations = []
tests = []
true = []
false = []
checking = []
for i in file:
    i = i.strip()
    #print(i)
    if(k == 0):
        monkeys.append(int(i[7]))
        checking.append(0)
    if(k == 1):
        i = i[16:].replace(" ", "").split(',')
        i = [int(x) for x in i]
        items.append(i) 
    if(k == 2):
        index = i.index("=")
        i = i[index + 6:].replace(" ", "")
        operations.append(i)
    if(k == 3):
        index = i.index("y") + 2
        tests.append(int(i[index:]))
    if(k == 4):
        index = i.index("y") + 2
        true.append(int(i[index:]))
    if(k == 5):
        index = i.index("y") + 2
        false.append(int(i[index:]))
        k = -2
    k += 1
#part2
#for m in range(20):
def oblicz(a):
    for m in range(a):
        for i in range(len(monkeys)):
            checking[i] += len(items[i])
            match(operations[i][0]):
                    case "*":
                        addition = False
                    case "+":
                        addition = True
            for j in range(len(items[i])):
                if(addition == True):
                    item = (items[i][j] + int(operations[i][1:]))
                    if(item % tests[i] == 0):
                        items[true[i]].append(item)
                    else:
                        items[false[i]].append(item)
                else:
                    if(operations[i][1:] == "old"):
                        item = items[i][j] * items[i][j]
                    else:
                        item = items[i][j] * int(operations[i][1:])
                    if(item % tests[i] == 0):
                        items[true[i]].append(item)
                    else:
                        items[false[i]].append(item)
            items[i] = []
checking.sort(reverse = True)
result = checking[0] * checking[1]
print(result)
        











    
