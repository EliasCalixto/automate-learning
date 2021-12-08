grid = [['.','.','.','.','.','.'],
        ['.','o','o','.','.','.'],
        ['o','o','o','o','.','.'],
        ['o','o','o','o','o','.'],
        ['.','o','o','o','o','o'],
        ['o','o','o','o','o','.'],
        ['o','o','o','o','.','.'],
        ['.','o','o','.','.','.'],
        ['.','.','.','.','.','.']]

def characPic(A):
    X=0
    Y=0
    
    for i in A:
        loop(A,X,Y)
        Y+=1

def loop(matriz,x,y):
    for i in matriz:
        for j in i:
            try:
                print(matriz[x][y],end='')
                x += 1
            except:
                pass

characPic(grid)
