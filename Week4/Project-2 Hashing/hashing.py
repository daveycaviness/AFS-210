class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        keyStr = str(key)
        hashValue = 0
        for ch in str(keyStr):
            hashValue += ord(ch)
        return(hashValue % self.size)
    
    def rehash(self,key):
        # Insert your secondary hashing function code
        keyStr = str(key)
        hashValue = 0
        count = 0
        for ch in str(keyStr):
            count += 1
            hashValue += ord(ch) + count
        return (hashValue % self.size)
    
    def put(self,key,data):
        # Insert your code here to store key and data 
        newSlot = self.hashfunction(key)
        while self.slots[newSlot] and self.data[newSlot]:
            newSlot = self.rehash(key)
            break

        self.data[newSlot] = data
        self.slots[newSlot] = key

    def get(self,key):
        # Insert your code here to get data by key
        return self.data[self.hashfunction(key)]

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


H = HashTable()
H[69] = 'A'

# Store remaining input data
H.put(66, "B")
H.put(80, "C")
H.put(35, "D")
H.put(18, "E")
H.put(52, "F")
H.put(89, "G")
H.put(70, "H")
H.put(12, "I")

# print the slot values
print(H.slots)

# print the data values
print(H.data)

# print the value for key 52
print(H.get(52))