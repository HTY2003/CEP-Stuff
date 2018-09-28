
inputfile = "rpoh.txt"
outputfile = "enumrpoh.txt"
with open(inputfile, "r") as infile:
    allstrings = list(infile)
    with open(outputfile, "w") as outfile:
        i = 1
        for items in allstrings:
            outfile.write("Line "+str(i)+" "+items)
            i = i + 1

            
choices = ['pizza', 'pasta', 'salad', 'nachos']
print(list(enumerate(choices, start = 5))) #[(5, 'pizza'), (6, 'pasta'), (7, 'salad'), (8, 'nachos')]
            
inputfile = "rpoh.txt"
outputfile = "enumrpoh.txt"
with open(inputfile, "r") as infile:
    allstrings = list(infile)
    with open(outputfile, "w") as outfile:
        for lineno, items in enumerate(allstrings, start = 1):
            outfile.write("Line "+str(lineno)+" "+items)


inputfile = "rpoh.txt"
outputfile = "enumrpoh_appendmode.txt"
with open(inputfile, "r") as infile:
    allstrings = list(infile)
    with open(outputfile, "a") as outfile:
        for lineno, items in enumerate(allstrings, start = 1):
            outfile.write("Line "+str(lineno)+" "+items)
            
            
            
