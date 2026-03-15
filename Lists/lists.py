#   Created by Elshad Karimov on 10/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

# Accessing/Traversing the list

shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i]+"+"
    # print(shoppingList[i])
empty = []
for i in empty:
    print("I am empty")


# Update/Insert - List 

myList = [1,2,3,4,5,6,7]
print(myList)
myList.insert(4,15)

myList.append(55)

newList = [11,12,13,14]
myList.extend(newList)
print(myList)


#  Searching for an element in the List
myList =  [10,20,30,40,50,60,70,80,90]

def searchinList(list, value):
    for i in list:
        if i == value:
            return list.index(value)
    return 'The value does not exist in the list'

print(searchinList(myList, 100))

# Delete element from the list
print(f"Original List: {myList}")
myList.remove(10)
print(f"List after removal: {myList}")
myList.pop(2)
print(f"List after pop: {myList}")
print(f"Count of 10: {myList.count(10)}")
del myList[0]
print(f"List after deletion: {myList}")
del myList[1:3]
print(f"List after deletion of slice: {myList}")
myList.clear()
print(f"List after clear: {myList}")


# #  List operations / functions
# total = 0 
# count = 0
# while (True):
#     inp = input('Enter a number: ') 
#     if inp == 'done': break
#     value = float(inp)
#     total = total + value
#     count = count + 1 
#     average = total / count
					
# print('Average:', average)



# numlist = list() 
# while (True):
#     inp = input('Enter a number: ') 
#     if inp == 'done': break
#     value = float(inp)
#     numlist.append(value)
					
# average = sum(numlist) / len(numlist) 
# print('Average:', average)



a = [3,7,1,4,9,2,5]
a.sort()
print(a)