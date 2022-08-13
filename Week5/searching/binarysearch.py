def binary_search(list, item):
    total_size = len(list)
    mid_index = (total_size / 2)
    if (list[0] > item or list[int(total_size - 1)] < item):
        return False
    else:
        if list[int(mid_index)] == item:
            return True
        elif list[int(mid_index)] > item:
            cut_list = list[:int(mid_index)]
            return binary_search(cut_list, item)
        elif list[int(mid_index)] < item:
            cut_list = list[int(mid_index):]
            return binary_search(cut_list, item)


usr_lst = input('Input Ordered List: ')
stringified_lst = usr_lst.strip('][').split(', ')
my_list = []


def parse(list):
    if len(list) > 0:
        my_list.append(int(list[0]))
        list.pop(0)
        return parse(list)
    return
parse(stringified_lst)

target = int(input('Enter expected target: '))

print(binary_search(my_list, target))