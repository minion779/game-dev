new_set = set()

#how to create a set

num = {1,2,3,4,5,2,1,4,6}
print(num)

#type casting list to set

data = [3,4,56,2,6,87,5,4]
set_data = set(data)
print(set_data)

#iterating through the set

for i in set_data:
    print(i)

#print(set_data[1])
#indexing is not possible as the elements are not in order

#if indexing is needed we can typecast set to list first
list_data = list(set_data)
print(list_data)
print(list_data[1])

#modifying a set
#add elements
new_set.add("jkl")
new_set.add(2)
new_set.add(2)
new_set.add(3)
print(new_set)

#to add multiple elements use update

new_set.update([4,5,6,7])
print(new_set)

#deleting the element

new_set.remove(2)
#new_set.remove(0)

print(new_set)

new_set.discard(3)
new_set.discard(0)

#print(new_set)

#remove() throws an error if the element is not found. However discard() does not throw any error if the element is not found.
#when using pop() random elements get deleted as the set is unordered 

popped = new_set.pop()
print(popped)
print(new_set)

set1 = {1,2,3,4,5,2,3,4,8}
set2 = {6,7,8,9,7,8,9,5,4}
#union
#method 1
sets = set1.union(set2)
#method 2
sets1 =  set1 | set2
print(sets1)

#intersection
#method 1
sets = set1.intersection(set2)
#method 2
sets1 = set1 & set2

print(sets)

#difference
#method 1
sets = set1.difference(set2)

#method 2
sets1 = set1 - set2
print(sets)

#symmetric difference

#method 1
sets = set1.symmetric_difference(set2)

#method 2
sets1 = set1 ^ set2

print(sets)

