file = open('directory.txt')
tab_directories = []
tab_dirs = []
directory = []
currentDir = "/"
listing = False
tab_all = []
for i in file:
    i = i.strip()
    if(i == "$ ls"):
        listing = True
    if(i[:4] == "$ cd" and i != "$ cd .."):
        if(len(directory) != 0):
            tab_dirs.append(currentDir)
            tab_directories.append(directory)
            directory = []
            currentDir = i[5:]
        listing = False
    if(listing == True and i != "$ ls" and i != "$ cd .."):
        directory.append(i)
tab_dirs.append(currentDir)
tab_directories.append(directory)

tab_dirs = tab_dirs[::-1]
tab_directories = tab_directories[::-1]

for i in tab_dirs:
    tab_all.append(i)
    tab_all.append(0)
    
k = 0
for i in tab_directories:
    file_sizes = 0
    for j in i:
        if(j[:3] != "dir"):
            space = j.index(" ")
            file_sizes += int(j[:space])
        else:
            lookedDir = j[4:]
            for h in range(k - 2, -1, -2):
                if(tab_all[h] == lookedDir):
                    file_sizes += tab_all[h + 1]
                    break
                
    tab_all[k + 1] = file_sizes
    k += 2
sumOfDics = 0
for i in range(1, len(tab_all), 2):
    if(tab_all[i] < 100000):
        sumOfDics += tab_all[i]
#print(sumOfDics)
#part2
availableSpace = 70000000
updateSpace = 30000000

usedSpace = tab_all[len(tab_all) - 1]
requiredSpace = availableSpace - usedSpace
howManyToDelete = updateSpace - requiredSpace
print(requiredSpace)
print(howManyToDelete)

tab_sizes = []
for i in range(1, len(tab_all), 2):
    tab_sizes.append(tab_all[i])
tab_sizes.sort()
for i in tab_sizes:
    if(i > howManyToDelete):
        print(i)
        break
print(tab_all)

            
            
        

    
    
        








