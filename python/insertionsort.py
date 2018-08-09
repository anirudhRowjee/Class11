#insertion sort

o_list = []

x = int(input("Please give the number of elements in unsorted list"))
for i in range(1, x+1):
    y = input("please give element " + str(i) + " >>> ")
    o_list.append(y)

print("Unsorted list is ", o_list)
w_list = o_list

for i in range(0, len(w_list)):
    # print("i ", i)
    for j in range(0, i+1):
        # print("j ", j)
        if w_list[i] < w_list[j]:
            w_list.insert(j, w_list[i])
            w_list.pop(i+1)
            break

print("Sorted List is ", w_list)
