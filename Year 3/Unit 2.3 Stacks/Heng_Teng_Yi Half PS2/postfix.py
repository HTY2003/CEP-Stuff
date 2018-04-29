from lliststack import Stack
import operator

def postfix():
    #Input delimited by blank space
    exp = input("Enter a postfix expression: ").split(" ")
    stack = Stack()
    operdict = {"+": operator.add,
                "-": operator.sub,
                "*": operator.mul,
                "/": operator.truediv,
                "%": operator.mod}

    #Loops through the string's characters
    for i in exp:
        #If the character is an operator, it is applied to two popped values from the stack, the result being pushed back into the stack.
        if i in operdict:
            try:
                operand2, operand1 = stack.pop(),stack.pop()
                stack.push(operdict[i](operand1, operand2))
            #If the stack does not have two operands to pop, an error is printed.
            except AssertionError:
                print(" ".join(exp) + " $$$\nError: insufficient number of operands.")
                postfix()
        #Since the expression is assumed to be valid, non-operands are pushed to the stack as integers.
        else:
            stack.push(int(i))

    #If one number is left in the stack, it is printed as the solution.
    if len(stack) == 1:
        print(stack.peek())
    #If not, there are too many operands, so an error is printed.
    else:
        print(" ".join(exp) + " $$$\nError: insufficient number of operators.")
    postfix()

postfix()
