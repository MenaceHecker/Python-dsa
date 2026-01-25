## Given an array of integers nums, find all the duplicates in the array using a hash table (dictionary).
def find_duplicates(nums):
    my_dict = {}
    output = []
    for i in nums:
        if i in my_dict:
            output.append(i)
        else:
            my_dict[i] = True
        
    return output

## Test Cases

print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )