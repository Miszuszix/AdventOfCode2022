file = open('signals.txt')
##k = 1
##signal = 1
##cycle = 0
##result = 0
##for i in file:
##    i = i.strip()
##    cycle += 1
##    if(cycle == -20 + k * 40):
##        result += cycle * signal
##        k += 1
##    if(i[0] == 'a'):
##        cycle += 1
##        if(cycle == -20 + k * 40):
##            result += cycle * signal
##            k += 1
##        value = i[5:]
##        signal += int(value)
##print(result)
##print(cycle)
##part2

cycle = 0
k = 1
signal = 1
string = ""
CRT = 0
for i in file:
    i = i.strip()
    cycle += 1
    if(CRT <= signal + 1 and CRT >= signal - 1):
        string += "#"
        CRT += 1
    else:
        string += "."
        CRT += 1
    if(cycle == 40):
        print(string)
        string = ""
        cycle = 0
        CRT = 0
    if(i[0] == 'a'):
        cycle += 1
        if(CRT <= signal + 1 and CRT >= signal - 1):
            string += "#"
            CRT += 1
        else:
            string += "."
            CRT += 1
        if(cycle == 40):
            print(string)
            string = ""
            cycle = 0
            CRT = 0
        value = i[5:]
        signal += int(value)
