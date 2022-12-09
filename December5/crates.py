file = open('crates.txt')
tabcrates = ["", "", "", "", "", "", "", "", ""]
string = ""
for i in file:
    for j in range(1, len(i), 4):
        if(i[j] != " "):
            index = tabcrates[round((j - 1) / 4)]
            index += i[j]
            tabcrates[round((j - 1) / 4)] = index
print(tabcrates)
file.close()
file = open('instructions.txt')
steps = []
for i in file:
    i = i.strip()
    tab = []
    if(i[6] != " "):
        string = i[5] + i[6]
        tab.append(string)
        tab.append(i[13])
        tab.append(i[18])
    else:
        tab.append(i[5])
        tab.append(i[12])
        tab.append(i[17])
    steps.append(tab)
for i in steps:
    stack = tabcrates[int(i[1]) - 1]
    target_stack = tabcrates[int(i[2]) - 1]
    crates = stack[:int(i[0])]
    tabcrates[int(i[2]) - 1] = crates + target_stack
    tabcrates[int(i[1]) - 1] = stack[int(i[0]):]
##    for j in range(int(i[0])):
##        target_stack = stack[0] + target_stack
##        stack = stack[1:]
##        tabcrates[int(i[1]) - 1] = stack
##        tabcrates[int(i[2]) - 1] = target_stack
string = ""
for i in tabcrates:
    string += i[0]
print(string)
