#addidtion
l1 = [[1,2],[3,4]]
l2 = [[5,6],[7,8]]
ResAdd = [[0,0],[0,0]]


for i in range(2):
    for g in range(2):
        ResAdd[i][g] = l1[i][g]+l2[i][g]
    
for i in range(2):
    for g in range(2):
        print(ResAdd[i][g], end = "*")

#minus

l3 = [[1,2],[3,4]]
l4 = [[5,6],[7,8]]
ResMinus = [[0,0],[0,0]]

for i in range(2):
    for g in range(2):
        ResMinus[i][g] = l3[i][g]-l4[i][g]
    
for i in range(2):
    for g in range(2):
        print(ResMinus[i][g], end = "*")

#print diagonals

list5 = []
print("What dimension do you want?")
question = int(input(">"))

for i in range(question):
    temp = []
    for g in range(question):
        x = int(input("enter your element"))
        temp.append(x)
    list5.append(temp)
for i in range(question):
    print(list5[i][i])

