filename = "cities_and_times.txt"
with open(filename) as infile:
    listoflines = list(infile)
    listoflines.sort()
    for line in listoflines:
        linesepar=line.split("\t")
        print(linesepar)
        
