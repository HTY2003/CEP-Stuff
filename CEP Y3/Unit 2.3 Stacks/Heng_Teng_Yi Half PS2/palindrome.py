from lliststack import Stack

def palindrome():
    teststack = Stack()
    tempstack = Stack()
    reverseteststack = Stack()
    test = input("Enter a string: ")

    #Loops through the string's characters
    for i in test:
        #Pushes each character into both a test stack and temporary stack
        teststack.push(i)
        tempstack.push(i)

    #Loops through temporary stack and pushes popped value into empty stack, creating reversed version of stack
    while not tempstack.isEmpty():
        reverseteststack.push(tempstack.pop())

    #Loops through test stack and conducts an elementwise comparison between test and reversed stack
    while not teststack.isEmpty():
        #If the elements do not match, the string is not a palindrome.
        if teststack.peek() != reverseteststack.peek():
            print(test + "\nnot a palindrome")
            palindrome()
        #If they do match, the elements are popped from their stacks.
        teststack.pop()
        reverseteststack.pop()

    #If the loop is passed succesfully, the reverse and original are the same, meaning the string is a palindrome.
    print(test + "\npalindrome")
    palindrome()

palindrome()
