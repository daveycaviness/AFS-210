import random

user_list = input("Input your list of numbers: ")
string_list = user_list.strip("][").split(", ")
parsed_list = []
shuffled_list = []

def parse(list):
    if len(list) > 0:
        parsed_list.append(int(list[0]))
        list.pop(0)
        return parse(list)
    return 
parse(string_list)
    

def shuffle(list):
    temp = list.copy()
    if len(temp) > 0:
        e= temp.pop(random.randint(0, len(temp)-1))
        shuffled_list.append(e)
        return shuffle(temp)
    else:
        print(shuffled_list)
        shuffled_list.clear()

print("Original List by User: ")
print(f'{parsed_list}')

print("Shuffled: ")
shuffle(parsed_list)
shuffle(parsed_list)
shuffle(parsed_list)
shuffle(parsed_list)
shuffle(parsed_list)
shuffle(parsed_list)