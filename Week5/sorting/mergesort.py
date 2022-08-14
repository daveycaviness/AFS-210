def mergeSort(nlist):
    print("Splitting ",nlist)
    # insert your code to complete the mergeSort function
    list_size = len(nlist)
    mid_index = (list_size / 2)
    if len(nlist) > 1:
        left = nlist[:int(mid_index)]
        right = nlist[int(mid_index):]
        mergeSort(left)
        mergeSort(right)
        merge(nlist, left, right) 
    
    print("Merging ",nlist)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

user_input = input('Please input your list of numbers: ')
string_data = user_input.strip('][').split(', ')
parsed_data = []

def parse(list):
    if len(list) > 0:
        parsed_data.append(int(list[0]))
        list.pop(0)
        return parse(list)
    return

parse(string_data)
mergeSort(parsed_data)
