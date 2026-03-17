#   Created by Elshad Karimov on 05/04/2020.
#   Copyright © 2020 AppMillers. All rights reserved.


import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

################### Insertion in 2D Array ###################
# Axis = 0 : Insertion in the row
# Axis = 1 : Insertion in the column

newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=1)
print(f"New array: \n{newTwoDArray}")

print(f"Length of the array: {len(twoDArray)}")
#############################################################

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(newTwoDArray))
print(len(newTwoDArray[0]))

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])

accessElements(newTwoDArray, 1, 2)

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


traverseTDArray(twoDArray)


def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element no found'

################### Search in 2D Array ###################
print(searchTDArray(twoDArray, 444))
#############################################################

################### Deletion in 2D Array ###################
# Axis = 0 : Deletion in the row
# Axis = 1 : Deletion in the column
print(f"Existing 2D Array: \n{twoDArray}")
newTDArray = np.delete(twoDArray, 1, axis=1)
print(f"New 2D Array: \n{newTDArray}")
#############################################################