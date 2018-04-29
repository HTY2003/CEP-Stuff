from chainhash import CHashTable

def chainhashclient():
    """Showcase of Separate Chaining hash table and its important functions.
    To use, run the program, scroll to the top, and read from there.
    For closer analysis, look at the code."""

    testfile = open("db.txt").readlines()

    """Initialization: Prime numbers recommended for size"""
    a = CHashTable(257)
    b = CHashTable(127)

    print("~~~~~~~~~~~~~~ANALYSIS FOR IMPORTANT FUNCTIONS~~~~~~~~~~~~~~~\n")
    # adds all items into the hash table:
    print("CHashTable.add(element):\n" + CHashTable.add.__doc__)
    for name in testfile:
        b.add(name)

    print("\nstr(CHashTable):\n" + CHashTable.__str__.__doc__)
    print("\nHash Table after all testitems are added: \n")
    # prints organized string of the hash table array
    print(b)

    print("iter(CHashTable):\n" + CHashTable.__iter__.__doc__)
    print("\nIteration through all items in the hash table: \n")
    # prints all elements in the hash table
    for item in b:
        print(item)

    print("\nCHashTable.get(element):\n" + CHashTable.get.__doc__)
    print("\nIndexes of elements in the hash table: \n")
    # prints indexes of each student in the hash table
    for i in testfile:
        print("Index of " + i[:-3] + " : " + str(b.get(i)))

    print("\nIndexes of elements NOT in the hash table: \n")
    # prints None when element is not in hash table
    print(("Index of 1: " + str(b.get(1))))

    print("\nCHashTable.rehash(size):\n" + CHashTable.rehash.__doc__)
    print("\nLength after rehashing into 256:")
    print(len(b))
    #rehashes table into a size 256 table
    print("\nLength after rehashing into 256:")
    b.rehash(256)
    print(len(b))

    print("\nCHashTable.remove(element):\n" + CHashTable.remove.__doc__)
    #removes all items in the hash table
    for item in testfile:
        b.remove(item)
    print("\nNo of spaces used in hash table after removing all elements:")
    print(b.used())

    print("\nCHashTable.checkrehash(min, max, multiplier, divisor):\n" + CHashTable.checkrehash.__doc__)
    print("\nOriginal length of hash table, and amount of spaces used:")
    print(len(b), b.used())
    #divides hash table by 2 (can be changed) if less than 20% is used(this can be changed to any percentage)
    print("\nAfter checking and rehashing:")
    b.checkrehash()
    print(len(b), b.used())

    #multiplies by 2 (can be changed) if more than 80% is used(this can be changed to any percentage)
    for i in range(504):
        a.add(i)
    print("\nOriginal length of hash table, and amount of spaces used:")
    print(len(a), a.used())

    print("\nAfter checking and rehashing:")
    a.checkrehash()
    print(len(a), a.used())

    print("~~~~~~END OF ANALYSIS FOR SEPARATE CHAINING HASH TABLE~~~~~~~")

chainhashclient()
print(chainhashclient.__doc__)
