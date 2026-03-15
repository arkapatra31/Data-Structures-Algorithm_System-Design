import array
import numpy


################### Create 1D Array ###################
def create_array():
    arr = array.array('i', [1, 2, 3, 4, 5])
    print(arr)


def create_arr_num_py():
    arr = numpy.array([6,7,8,9,10], dtype=int)
    print(arr)

########################################################

arr = array.array('i', [1, 2, 3, 4, 5])
################### Insertion in 1D Array ###################

def insert_element(index, element):
    arr.insert(index, element)
    print(arr)

#############################################################


#################### Traversal in 1D Array ###################

def traverse_array():
    for i in arr:
        print(i)

#############################################################


#################### Accessing in 1D Array ###################
def access_element(index):
    print(arr[index])

#############################################################


################### Searching element in 1D Array ###################

def search_element(element):
    print(element in arr)

#####################################################################


################## Remove element from 1D Array ###################

def remove_element(element):
    arr.remove(element)
    print(arr)

def remove_by_index(index):
    arr.pop(index)
    print(arr)

#####################################################################




if __name__ == "__main__":
    create_array()
    create_arr_num_py()
    insert_element(2, 10)
    traverse_array()
    access_element(3)
    search_element(2)
    remove_element(2)
    remove_by_index(2)