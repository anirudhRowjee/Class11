# bubble sort

x = int(input("please give number of elements in list >>> "))


# accept integer number of list elements

init_list = []

# made an empty list to input values taken from the user

for i in range(1, x+1):     # start counter from 1 to max index of list
    z = int(input("Give element number "+ str(i) + " for list >>> "))  # ask for nth element of list
    init_list.append(z)     # append the element to the list

working_list = init_list       # create a working list to maintain data integrity

print("\nunsorted list is", working_list)         # print the unsorted list

for i in range(0, len(working_list)):       # start range counter to help us define the limit of our sort per row
    # print("Current I is  ", i)
    for j in range(0, len(working_list)-i-1):  # start range counter to fix limit at n-1th element of list
        # print("Current J is ", j)
        # print("Before ", working_list)
        if working_list[j] > working_list[j + 1]:           # if the current element is greater than the previous
            working_list[j] , working_list[j + 1] = working_list[j + 1], working_list[j]    # swap the two
            # print("After  ", working_list)

print("\nsorted list is ", working_list)
