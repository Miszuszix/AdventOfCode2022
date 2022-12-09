file = open('rucksack.txt')
points = 0
for i in file:
        half = int((len(i) - 1) / 2)
        left = i[:half]
        right = i[half:]
        for k in left:
            if(right.count(k) > 0):
                asc = ord(k)
                if(asc < 91):
                    points += asc - 38
                else:
                    points += asc - 96
                break
print(points)
file.close()
points = 0
#part2
file = open('rucksack.txt')
j = -1
first = ""
second = ""
third = ""
for i in file:
    j += 1
    if(j == 0):
        first = i[:len(i) - 1]
    if(j == 1):
        second = i[:len(i) - 1]
    if(j == 2):
        third = i[:len(i) - 1]
        for k in first:
            if(second.count(k) > 0 and third.count(k) > 0):
                asc = ord(k)
                if(asc < 91):
                    points += asc - 38
                else:
                    points += asc - 96
                break
        j = -1
print(points)









