from lliststack import SStack

# Extracts a collection of integer values from the user
# and prints them in reverse order.
PROMPT = "Enter an int value (<0 to end):"
myStack = SStack()

# Extract the values and push them onto a stack.
value = int(input( PROMPT ))

while value >= 0 :
    myStack.push( value )
    value = int(input( PROMPT ))

# Pop the values from the stack and print each.
while not myStack.isEmpty() :
    value = myStack.pop()
    print( value )

