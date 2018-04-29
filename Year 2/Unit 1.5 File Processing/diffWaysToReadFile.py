'''
It is good practice to use the with keyword when dealing with file objects. This has the advantage that the file is properly closed after its suite finishes, even if an exception is raised on the way. It is also much shorter than writing equivalent try-finally blocks:

>>>
>>> with open('workfile', 'r') as f:
...     read_data = f.read()
>>> f.closed
True

'''


### Read whole file as a string
print("Read whole file as a string")
print("="*50)
filename = "cities_and_times.txt"
with open(filename) as infile:
    wholeFileAsString = infile.read();
    print(wholeFileAsString)

### Read whole file as a list of strings #1
print("Read whole file as a string #1")
print("="*50)
filename = "cities_and_times.txt"
with open(filename) as infile:
    listoflines = infile.readlines()
    print(listoflines)


## Iterate over each line of the file
print("Read whole file as a string #3")
print("="*50)
filename = "cities_and_times.txt"
with open(filename) as infile:
    listoflines = list(infile)
    listoflines.sort()
    for line in listoflines:
        print(line.split("\t"))
