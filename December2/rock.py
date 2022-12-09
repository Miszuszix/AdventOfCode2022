file = open('rock.txt')
points = 0
j = 0
first = ""
second = ""
for i in file:
##        match i[0]:
##            case "A":
##                first = "rock1"
##            case "B":
##                first = "paper2"
##            case "C":
##                first = "scissors3"
##        match i[2]:
##            case "X":
##                second = "rock1"
##            case "Y":
##                second = "paper2"
##            case "Z":
##                second = "scissors3"
##        points2 = int(second[len(second) - 1])
##        if(first == second):
##            points += points2 + 3
##        elif(first == "rock1" and second == "paper2"):
##            points += points2 + 6
##        elif(first == "paper2" and second == "scissors3"):
##            points += points2 + 6
##        elif(first == "scissors3" and second == "rock1"):
##            points += points2 + 6
##        else:
##            points += points2
#part2
        match i[0]:
            case "A":
                first = "rock"
            case "B":
                first = "paper"
            case "C":
                first = "scissors"
        match i[2]:
            case "X":
                match first:
                    case "rock":
                        points += 3
                    case "paper":
                        points += 1
                    case "scissors":
                        points += 2
            case "Y":
                match first:
                    case "rock":
                        points += 4
                    case "paper":
                        points += 5
                    case "scissors":
                        points += 6
            case "Z":
                match first:
                    case "rock":
                        points += 8
                    case "paper":
                        points += 9
                    case "scissors":
                        points += 7
print(points)



