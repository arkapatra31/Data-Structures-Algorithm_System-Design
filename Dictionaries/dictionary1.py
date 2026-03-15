#   Created by Elshad Karimov on 20/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

#  Update / add an element to the dictionary

myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
print(myDict)

#  Traverse through a dictionary

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

#  Searching a dictionary


def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 27))


## Access both key and value at same time
for key, value in myDict.items():
    print(f"Key: {key}, Value: {value}")

#  Delete or remove a dictionary

myDict.pop('name')
print("myDict after pop: ", myDict)
print(myDict.popitem())
print("myDict after popitem: ", myDict)

# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}

print(sorted(myDict, key=len))

print("#"*50)
# Create manual collision
class ColidingKeys:
    def __init__(self, value):
        self.value = value
    # This method is used to hash the object
    def __hash__(self):
        return 42
    # This method is used to compare two objects
    def __eq__(self, other):
        return self.value == other.value

col_dict = {
    ColidingKeys("a"): 1,
    ColidingKeys("b"): 2,
    ColidingKeys("c"): 3,
    ColidingKeys("a"): 4
}
print(col_dict)
print(ColidingKeys("a").__hash__())
print(ColidingKeys("a").__eq__(ColidingKeys("a")))