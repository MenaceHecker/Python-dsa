def bubble_sort(my_list):
    for i in range(len(my_list) -1, 0 , -1):
        for j in range(i):
            if my_list[j] > my_list[j+1]:
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp
    return my_list

testing = bubble_sort([3,2,4,1,7,6])
print(testing)
