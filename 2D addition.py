l1 = [[1,2],[3,4]]
l2 = [[5,6],[7,8]]
ResAdd = [[0,0],[0,0]]

for i in range(2):
    for g in range(2):
        ResAdd = l1[i][g]+l2[i][g]
    
for i in range(2):
    for g in range(2):
        print(ResAdd[i][g], end = " ")
