file = open('rope.txt')
sameColumnOrRow = False
vertical = None
reverse = False
step = 0
touching = False
def isTouching(head, tail):
    global sameColumnOrRow
    global vertical
    global touching
    
    if(tail[0] == head[0]):
        sameColumnOrRow = True
        vertical = False
    else:
        sameColumnOrRow = False
        vertical = None
    if(sameColumnOrRow == False):
        if(tail[1] == head[1]):
            sameColumnOrRow = True
            vertical = True
        else:
            vertical = None
        
    if(tail[0] == head[0] and tail[1] == head[1]):
        touching = True
    
    if(sameColumnOrRow == True):
        if(tail[0] + 1 == head[0] or tail[0] - 1 == head[0]):
            touching =  True
    if(sameColumnOrRow == True):
        if(tail[1] + 1 == head[1] or tail[1] - 1 == head[1]):
            touching =  True
    if(tail[0] + 1 == head[0] and tail[1] + 1 == head[1]):
        touching =  True
    elif(tail[0] + 1 == head[0] and tail[1] - 1 == head[1]):
        touching =  True
    elif(tail[0] - 1 == head[0] and tail[1] - 1 == head[1]):
        touching =  True
    elif(tail[0] - 1 == head[0] and tail[1] + 1 == head[1]):
        touching =  True

head = [0,0]
tail = [0,0]
positions = {"00" : 1}
for i in file:
    appended = False
    i = i.strip()
    step = int(i[2:])
    match(i[0]):
        case "R":
            head[1] += step
            reverse = False
        case "L":
            head[1] -= step
            reverse = True
        case "U":
            head[0] += step
            reverse = False
        case "D":
            head[0] -= step
            reverse = True
    touching = False
##    print(touching, "TOUCHING BEFORE")
##    print(head, tail)
    isTouching(head, tail)
##    print(touching, "TOUCHING")
##    print(sameColumnOrRow, "COLUMNROW")
##    print(vertical, "VERTICAL")
##    print(reverse, "REVERSE")
##    print(step, "STEP")
##    print(head)
##    print(tail, "BEFORE")
    if(touching == False):
##        print("NOT TOUCHING")
        if(sameColumnOrRow == True):
            if(vertical == True):
                if(reverse == True):
                    for j in range(step, 1, -1):
                        tail[0] -= 1
                        positions[str(tail[0]) + str(tail[1])] = 1
                else:
                    for j in range(0 ,step - 1):
                        tail[0] += 1
                        positions[str(tail[0]) + str(tail[1])] = 1
            elif(vertical == False):
                if(reverse == True):
                    for j in range(step, 1, -1):
                        tail[1] -= 1
                        positions[str(tail[0]) + str(tail[1])] = 1
                else:
                    for j in range(0 ,step - 1):
                        tail[1] += 1
                        positions[str(tail[0]) + str(tail[1])] = 1
        else:
            if(head[0] - tail[0] == 1):
                tail[0] += 1
                if(reverse == True):
                    tail[1] -= 1
                    positions[str(tail[0]) + str(tail[1])] = 1
                    appended = True
                    for j in range(step - 2, 0, -1):
                        if(tail[0] != head[0] or tail[1] != head[1]):
                            tail[1] -= 1
                        if(tail[0] != head[0] or tail[1] != head[1]):
                            positions[str(tail[0]) + str(tail[1])] = 1
                        else:
                            tail[1] += 1
                else:
                    tail[1] += 1
                    positions[str(tail[0]) + str(tail[1])] = 1
                    appended = True
                    for j in range(0 ,step - 2):
                        if(tail[0] != head[0] or tail[1] != head[1]):
                            tail[1] += 1
                        if(tail[0] != head[0] or tail[1] != head[1]):
                            positions[str(tail[0]) + str(tail[1])] = 1
                        else:
                            tail[1] -= 1
            elif(tail[0] - head[0] == 1):
                tail[0] -= 1
                if(reverse == True):
                    tail[1] -= 1
                    positions[str(tail[0]) + str(tail[1])] = 1
                    appended = True
                    for j in range(step - 2, 0, -1):
                        if(tail[0] != head[0] or tail[1] != head[1]):
                            tail[1] -= 1
                        if(tail[0] != head[0] or tail[1] != head[1]):
                            positions[str(tail[0]) + str(tail[1])] = 1
                        else:
                            tail[1] += 1
                else:
                    tail[1] += 1
                    positions[str(tail[0]) + str(tail[1])] = 1
                    appended = True
                    for j in range(0 ,step - 2):
                        if(tail[0] != head[0] or tail[1] != head[1]):
                            tail[1] += 1
                        if(tail[0] != head[0] or tail[1] != head[1]):
                            positions[str(tail[0]) + str(tail[1])] = 1
                        else:
                            tail[1] -= 1
            if(appended == False):
                if(head[1] - tail[1] == 1):
                    tail[1] += 1
                    if(reverse == True):
                        tail[0] -= 1
                        positions[str(tail[0]) + str(tail[1])] = 1
                        for j in range(step - 2, 0, -1):
                            if(tail[0] != head[0] or tail[1] != head[1]):
                                tail[0] -= 1
                            if(tail[0] != head[0] or tail[1] != head[1]):
                                positions[str(tail[0]) + str(tail[1])] = 1
                            else:
                                tail[0] += 1
                    else:
                        tail[0] += 1
                        positions[str(tail[0]) + str(tail[1])] = 1
                        for j in range(0 ,step - 2):
                            if(tail[0] != head[0] or tail[1] != head[1]):
                                tail[0] += 1
                            if(tail[0] != head[0] or tail[1] != head[1]):
                                positions[str(tail[0]) + str(tail[1])] = 1
                            else:
                                tail[0] -= 1
                elif(tail[1] - head[1] == 1):
                    tail[1] -= 1
                    if(reverse == True):
                        tail[0] -= 1
                        positions[str(tail[0]) + str(tail[1])] = 1
                        for j in range(step - 2, 0, -1):
                            if(tail[0] != head[0] or tail[1] != head[1]):
                                tail[0] -= 1
                            if(tail[0] != head[0] or tail[1] != head[1]):
                                positions[str(tail[0]) + str(tail[1])] = 1
                            else:
                                tail[0] += 1
                    else:
                        tail[0] += 1
                        positions[str(tail[0]) + str(tail[1])] = 1
                        for j in range(0 ,step - 2):
                            if(tail[0] != head[0] or tail[1] != head[1]):
                                tail[0] += 1
                            if(tail[0] != head[0] or tail[1] != head[1]):
                                positions[str(tail[0]) + str(tail[1])] = 1
                            else:
                                tail[0] -= 1
##    print(positions)
##    
##    print(tail)
##    print()

print(positions)
print(len(positions))

