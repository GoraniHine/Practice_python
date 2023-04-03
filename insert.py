list = [1, 2, 3, 4]

def my_insert(pos, value):
    list.append(0)
    for i in range(len(list)-1, pos, -1):
        list[i] = list[i-1]
    list[pos] = value

my_insert(0, 5)
print(list)

#def my_delete(lst, pos):
#    for i in range(pos+1, len(list)-1):
#        lst[i] = lst[i+1]
#        lst.pop(-1)
#