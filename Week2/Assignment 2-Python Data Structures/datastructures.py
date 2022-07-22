from re import I


data1 = (7, False, "Apple", True, 7, 98.6)

data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

data3 = ["A", 7, -1, 3.14, True, 7]

data4 = {
    "name": "Joe",
    "age": 26,   
    "active": True,
    "hourly_wage": 14.75
}


# Data1 - Count the number of items
print(len(data1))

# Data1 - Find the value of the fourth item stored in the data set
print(data1[3])
# Data1 - Count the number of times 7 appears
count = 0
for x in data1:
    if x == 7:
        count += 1
print(count)

# Data2 - Remove a random element from the data set
data2.pop()

# Data2 - Add "Alpha" to the data set
data2.add("Alpha")
# Data2 - Print data set
print(data2)

# Data3 - Print the data set in reverse order
data3.reverse()

# Data3 - Change the second value in the data set to ‘B’
data3[1] = "B"

# Data3 - Remove the last item and print the data set
data3.pop(len(data3)-1)
print(data3)

# Data4 - Change "active" to False
data4["active"] = False

# Data4 - Add "address" with a value of "123 West Main Street"
data4["address"] = "123 West Main Street"

# Data4 - Print the weekly salary for Joe if he worked a full 40 hour week.
print(data4["hourly_wage"] * 40)
# Data4 - Print the data set
print(data4)