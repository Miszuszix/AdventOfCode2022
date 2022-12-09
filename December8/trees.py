file = open('trees.txt')
height = 0
width = 0
tab = []
visible = True
for i in file:
    i = i.strip()
    if(height < 1):
        width += (len(i) - 2)
    tab_temp = []
    for j in i:
        tab_temp.append(int(j))
    tab.append(tab_temp)
    height += 1
edges = height * 2 + width * 2

def vertical(x, y):
    global visible
    global edges
    visible = True
    
    for i in range(x - 1, -1, -1):
        if(tab[x][y] <= tab[i][y]):
            visible = False
            break
    if(visible == True):
        edges += 1
    else:
        visible = True
        for i in range(x + 1, height):
            if(tab[x][y] <= tab[i][y]):
                visible = False
                break
        if(visible == True):
            edges += 1
        
def horizontal(x, y):
    global visible
    global edges
    visible = True
    
    for i in range(y - 1, -1, -1):
        if(tab[x][y] <= tab[x][i]):
            visible = False
            break
    if(visible == True):
        edges += 1
    else:
        visible = True
        for i in range(y + 1, width + 2):
            if(tab[x][y] <= tab[x][i]):
                visible = False
                break
        if(visible == True):
            edges += 1

for i in range(1, height - 1):
    for j in range(1, width + 1):
        vertical(i,j)
##        print(i, j, visible)
        if(visible == False):
            horizontal(i,j)
##            print(i,j, visible, "HORIZONTAL")
print(edges)
for i in tab:
    print(i)
##part2
def viewingScore(x,y):
    scores = [0,0,0,0]
    score = 1
    for i in range(x - 1, -1, -1):
        if(tab[x][y] > tab[i][y]):
            scores[0] += 1
        if(tab[x][y] <= tab[i][y]):
            scores[0] += 1
            break
        
    for i in range(x + 1, height):
        if(tab[x][y] > tab[i][y]):
            scores[1] += 1
        if(tab[x][y] <= tab[i][y]):
            scores[1] += 1
            break
        
    for i in range(y - 1, -1, -1):
        if(tab[x][y] > tab[x][i]):
            scores[2] += 1
        if(tab[x][y] <= tab[x][i]):
            scores[2] += 1
            break
        
    for i in range(y + 1, width + 2):
        if(tab[x][y] > tab[x][i]):
            scores[3] += 1
        if(tab[x][y] <= tab[x][i]):
            scores[3] += 1
            break
    for i in scores:
        score *= i
    return score
tab_scores = []
for i in range(1, height - 1):
    for j in range(1, width + 1):
        tab_scores.append(viewingScore(i,j))
print()
print(max(tab_scores))
    
    




                
