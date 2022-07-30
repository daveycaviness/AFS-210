class Stack:
    def __init__(self):
        self.stackList = []
    
    def push(self, letter):
        self.stackList.append(letter) 

    def pop(self):
        self.stackList.pop()

    def size(self):
       return len(self.stackList)

    def isEmpty(self):
        return self.stackList == []

    def peek(self):
        return self.stackList[-1]

        


class Queue:
    def __init__(self):
        self.queueList = []

    def enqueue(self, letter):
        self.queueList.insert(0, letter)

    def dequeue(self):
        self.queueList.pop()

    def size(self):
        return len(self.queueList)

    def isEmpty(self):
        return self.queueList == []

    def peek(self):
        return self.queueList[-1]

def isPalindrome(word):
    stack = Stack()
    queue = Queue()

    for letter in word.upper():
        stack.push(letter)

    for letter in word.upper():
        queue.enqueue(letter)

    if stack.stackList == queue.queueList:
        return True
    else:
        return False

print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))