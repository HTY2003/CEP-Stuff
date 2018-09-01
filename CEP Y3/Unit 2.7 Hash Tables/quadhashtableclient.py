from quadhash2 import HashTable

def quadhashclient():
    """
    Showcase of Quadratic Probing hash table and its important functions.
    To use, run the program, scroll to the top, and read from there.
    For closer analysis, look at the code."""

    testfile = open("db.txt").readlines()

    #-------------------INITIALIZATION----------------------
    '''Case A: a size 256 table, twice as much as needed.
    #Makes the table sparse for less collisions, for quicker addition, searching and deletion
    #Although it sacrifices space'''
    a = HashTable(len(testfile)*2, autocal=True)

    '''Case B: a size 128 table, calculated to fit the testfile data
    Ensures that no memory is wasted on empty space and no time is wasted resizing the hash table
    Although it makes adding and searching take VERY slightly longer'''
    b = HashTable(len(testfile), autocal=True)

    '''Case C: a size 64 table that eventually gets resized to size 128 to fit the data
    Not optimal in any case, but it works, and that's all that matters'''
    c = HashTable()


    print("~~~~~~~~~~~~~~ANALYSIS FOR IMPORTANT FUNCTIONS~~~~~~~~~~~~~~~\n")
    # adds all items into the hash table:
#-------------------ADD and PRINT----------------------
    print("HashTable.add(key,value):\n" + HashTable.add.__doc__)
    for i in range(len(testfile)):
        b.add(i,testfile[i])

    print("\nstr(HashTable):\n" + HashTable.__str__.__doc__)
    print("\nHash Table after all testitems are added: \n")
    # prints organized string of the hash table array
    print(b)

    print("iter(HashTable):\n" + HashTable.__iter__.__doc__)
    print("\nIteration through all values in the hash table: \n")
    # prints all elements in the hash table
    for item in b:
        print(item)
#--------------------------------------------------
#-----------------------GET-------------------------
    print("\nHashTable.get(key):\n" + HashTable.get.__doc__)
    print("\nValues of keys in the hash table: \n")
    # prints indexes of each student in the hash table
    for i in range(len(testfile)):
        print("Value of key (" + str(i).strip("\n") + ") : " + str(b.get(i)))

    print("\nIndexes of keys NOT in the hash table: \n")
    # prints None when element is not in hash table
    print(("Value of key (" + str(len(testfile)+1)+ "): " + str(b.get(len(testfile)+1))))
#----------------------------------------------
#-----------------REHASH-----------------------
    print("\nHashTable.rehash(size):\n" + HashTable.rehash.__doc__)
    #rehashes table into a size 256 table
    print("\nLength after rehashing into 256:")
    b.rehash(256)
    print(len(b))
    print("\nLength after rehashing into 1000 with autocal enabled:")
    #rehashes table into a size 1024 table (auto-calculated from 1000)
    b.rehash(1000, autocal = 1000)
    print(len(b))
#-----------------------------------------------
#------------------REMOVE-----------------------
    print("\nHashTable.remove(key):\n" + HashTable.remove.__doc__)
    #removes all items in the hash table
    for item in range(len(testfile)):
        b.remove(item)
    print("\nNo of spaces used in hash table after removing all key-value pairs:")
    print(b.used())
#------------------------------------------------
#------------------CHECKREHASH-------------------
    print("\nHashTable.checkrehash(min, max, multiplier, divisor):\n" + HashTable.checkrehash.__doc__)
    print("\nOriginal length of hash table, and amount of spaces used:")
    print(len(b), b.used())
    #halves hash table if less than 20% is used(this can be changed to any percentage)

    print("\nAfter checking and rehashing:")
    b.checkrehash()
    print(len(b), b.used())

    #multiplies if more than 80% is used(this can be changed to any percentage)
    for i in range(254):
        a.add(i, i)
    print("\nOriginal length of hash table, and amount of spaces used:")
    print(len(a), a.used())

    print("\nAfter checking and rehashing:")
    a.checkrehash()
    print(len(a), a.used())
#---------------------------------------------------
    print("\nALSO: automatic rehashing when the table is full")
    #hash table also automatically rehashes when full
    print("\nLength before adding 100 elements to a size 64 table:")
    print(len(c))
    for i in testfile:
        c.add(i, i)
    print("\nAfter hash table gets full and automatically resizes:")
    print(len(c))
    print("~~~~~~END OF ANALYSIS FOR QUADRATIC PROBING HASH TABLE~~~~~~~")

quadhashclient()
print("\n" + quadhashclient.__doc__)
