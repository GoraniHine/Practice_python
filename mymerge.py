list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

def my_merge(list1, list2):
    for i in range(len(list2)):
        for j in range(len(list1)):
            if list2[i] <= list1[j]:
                my_insert(list1, j, list2[i])
                break
        else:
            list1.append(list2[i])
    return list1

def my_insert(lst, index, value):
    lst.append(0)
    for i in range(len(lst) - 1, index, -1):
        lst[i] = lst[i-1]
    lst[index] = value

merged_list = my_merge(list1, list2)

print(merged_list)
