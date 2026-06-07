def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    swap_index = pivot_index

    for i in range(pivot_index+1, end_index+1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index

## Helper function for quick sort, which takes in the list and the left and right indices. It checks if the left index is less than the right index, which means there are at least two elements to sort. It then calls the pivot function to partition the list and get the pivot index. After that, it recursively calls itself on the left and right sublists defined by the pivot index. Finally, it returns the sorted list
def quick_sort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quick_sort_helper(my_list, left, pivot_index-1)  
        quick_sort_helper(my_list, pivot_index+1, right)       
    return my_list
    

def quick_sort(my_list):
    quick_sort_helper(my_list, 0, len(my_list)-1)

 
 


my_list = [4,6,1,7,3,2,5]

quick_sort(my_list)

print(my_list)