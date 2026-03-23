def find_missing_number(myList, n):
    actual_sum = int(n*(n+1)/2)
    sum_of_array = sum(myList)
    return actual_sum - sum_of_array

a = [1,2,3,4,6]
n = 6  # The last number in the sequence
print(find_missing_number(a, n))