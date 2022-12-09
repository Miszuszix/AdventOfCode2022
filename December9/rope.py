file = open('rope.txt')
pisitions = {}
def isTouching(head, tail):
    touching = False
    sameColumnOrRow = False
    if(tail[0] == head[0]):
        sameColumnOrRow = True
    if(tail[1] == head[1]):
        sameColumnOrRow = True
        
    if(tail[0] == head[0] and tail[1] == head[1]):
        touching = True
    
    if(touching != True):
        if(tail[0] + 1 == head[0] or tail[0] - 1 == head[0]):
            touching = True
        else:
            touching = False
    if(touching != True):
        if(tail[1] + 1 == head[1] or tail[1] - 1 == head[1]):
            touching = True
        else:
            touching = False
    if(touching != True):
        if(tail[0] + 1 == head[0] and tail[1] + 1 == head[1]):
            touching = True
        elif(tail[0] + 1 == head[0] and tail[1] - 1 == head[1]):
            touching = True
        elif(tail[0] - 1 == head[0] and tail[1] - 1 == head[1]):
            touching = True
        elif(tail[0] - 1 == head[0] and tail[1] + 1 == head[1]):
            touching = True
        else:
            touching = False
    print(sameColumnOrRow, "columnROW")
    return touching

head = [0,0]
tail = [0,0]
for i in file:
    i = i.strip()
    step = int(i[2])
    print(isTouching(head, tail))
    match(i[0]):
        case "R":
            head[1] += step
        case "L":
            head[1] -= step
        case "U":
            head[0] += step
        case "D":
            head[0] -= step









