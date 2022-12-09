file = open('kalorie.txt')
elves = []
calories = 0
for i in file:
        if(len(i) != 1):
            calories += int(i[:len(i) - 1])
        else:
            elves.append(calories)
            calories = 0
print(max(elves))

#part2
elves.sort(reverse = True)
calories = 0
for i in range(3):
        calories += elves[i]
print(calories)        
