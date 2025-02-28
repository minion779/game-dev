# 2D  list - Rows and  Columns

num = [[0,1,2],
        [4,6,7],
        [7,8,9],
        [3,5,10],
        [11,12,13]]


print(num[1][1])

#iteration
for i in range(len(num)):
    for g in range(len(num[i])):
        print(num[i][g])
#appending

num.append([10,20,40])
print(num)

#deleting

#a list

del num[1]
print(num)

# a value

num[0].remove(1)
print(num)

#reversing

num.reverse()

for i in num:
    i.reverse()
print(num)

#we can use without assigning the reverse version to any variable
#as the reverse() modifies the list in place and does not return a new list
# assigning result to any variable will result as null

#sorting
num.sort()

for i in num:
    i.sort()
print(num)

# Slicing
print("slicing")
print(num[1])
#to print from beginning to index 2
print(num[0:2]) 
#to print from beginning to index 3
print(num[:3])
#to print from index 1 to index 4
print(num[1:4])
#to print from index 2 to index 3
print(num[2:3])
#printing all elements using slicing
print(num[:])
#print all values starting from index 1
print(num[1:])