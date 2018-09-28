from arrayStack import Stack
def checkValidity(fileName):
    bracketDict = {"{":"}", "[":"]", "(":")"}
    checkStack = Stack()
    with open(fileName) as file:
        check = file.read()
        for i in check:
            if i in bracketDict.keys():
                checkStack.push(i)
            if i in bracketDict.values():
                if i == bracketDict[checkStack.peek()]:
                    checkStack.pop()
                else:
                    print("Everything with this is wrong.")
                    return False
        print("Everything with this except your brackets is wrong.")
        return True

checkValidity("sampleC.cpp")
