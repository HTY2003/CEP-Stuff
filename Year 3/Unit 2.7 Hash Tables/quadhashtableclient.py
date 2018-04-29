from quadhash import QHashTable

def quadhashclient():
    """Showcase of Quadratic Probing hash table and its important functions.
    To use, run the program, scroll to the top, and read from there.
    For closer analysis, look at the code."""

    testfile = open("db.txt").readlines()

    """Testing code for the quadratic probing hash table, and showcase of multiple scenarios and functions
    Read source code comments for closer analysis of hash table initialization
    Run the program for analysis of functions"""

    '''Case A: a size 256 table, twice as much as needed.
    #Makes the table sparse for less collisions, for quicker addition, searching and deletion
    #Although it sacrifices space'''
    a = QHashTable(len(testfile)*2, autocal=True)

    '''Case B: a size 128 table, calculated to fit the testfile data
    Ensures that no memory is wasted on empty space and no time is wasted resizing the hash table
    Although it makes adding and searching take slightly longer'''
    b = QHashTable(len(testfile), autocal=True)

    '''Case C: a size 64 table that eventually gets resized to size 128 to fit the data
    Not optimal in any case, but it works, and that's all that matters'''
    c = QHashTable()

    print("~~~~~~~~~~~~~~ANALYSIS FOR IMPORTANT FUNCTIONS~~~~~~~~~~~~~~~\n")
    # adds all items into the hash table:
    print("QHashTable.add(element):\n" + QHashTable.add.__doc__)
    for name in testfile:
        b.add(name)

    print("\nstr(QHashTable):\n" + QHashTable.__str__.__doc__)
    print("\nHash Table after all testitems are added: \n")
    # prints organized string of the hash table array
    print(b)

    print("iter(QHashTable):\n" + QHashTable.__iter__.__doc__)
    print("\nIteration through all items in the hash table: \n")
    # prints all elements in the hash table
    for item in b:
        print(item)

    print("\nQHashTable.get(element):\n" + QHashTable.get.__doc__)
    print("\nIndexes of elements in the hash table: \n")
    # prints indexes of each student in the hash table
    for i in testfile:
        print("Index of " + i[:-3] + " : " + str(b.get(i)))

    print("\nIndexes of elements NOT in the hash table: \n")
    # prints None when element is not in hash table
    print(("Index of 1: " + str(b.get(1))))

    print("\nQHashTable.rehash(size)\n:" + QHashTable.rehash.__doc__)
    #rehashes table into a size 256 table
    print("\nLength after rehashing into 256:")
    b.rehash(256)
    print(len(b))
    print("\nLength after rehashing into 1000 with autocal:")
    #rehashes table into a size 1024 table (auto-calculated from 1000)
    b.rehash(1000, autocal = 1000)
    print(len(b))

    print("\nQHashTable.remove(element):\n" + QHashTable.remove.__doc__)
    #removes all items in the hash table
    for item in testfile:
        b.remove(item)
    print("\nNo of spaces used in hash table after removing all elements: \n")
    print(b.used())

    print("\nQHashTable.checkrehash(min, max, multiplier, divisor):\n" + QHashTable.checkrehash.__doc__)
    print("\nOriginal length of hash table, and amount of spaces used:")
    print(len(b), b.used())
    #halves hash table if less than 20% is used(this can be changed to any percentage)

    print("\nAfter checking and rehashing:")
    b.checkrehash()
    print(len(b), b.used())

    #multiplies if more than 80% is used(this can be changed to any percentage)
    for i in range(254):
        a.add(i)
    print("\nOriginal length of hash table, and amount of spaces used:")
    print(len(a), a.used())

    print("\nAfter checking and rehashing:")
    a.checkrehash()
    print(len(a), a.used())

    #hash table also automatically rehashes when full
    print("\nLength before adding 100 elements to a size 64 table:")
    print(len(c))
    for i in testfile:
        c.add(i)
    print("\nAfter hash table gets full and automatically resizes:")
    print(len(c))
    print("~~~~~~END OF ANALYSIS FOR QUADRATIC PROBING HASH TABLE~~~~~~~")

quadhashclient()
print("\n" + quadhashclient.__doc__)
