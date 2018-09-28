from chainhash import HashTable

def chainhashclient():
    """Showcase of Separate Chaining hash table and its important functions.
    To use, run the program, scroll to the top, and read from there.
    For closer analysis, look at the code."""

    testfile = open("db.txt").readlines()
#-------------INITIALIZATION-------------------
    """Initialization: Prime numbers recommended for size"""
    a = HashTable(257)
    b = HashTable(127)

    print("~~~~~~~~~~~~~~ANALYSIS FOR IMPORTANT FUNCTIONS~~~~~~~~~~~~~~~\n")
#------------------ADD & PRINT----------------------
    # adds all items into the hash table:
    print("HashTable.add(key, value):\n" + HashTable.add.__doc__)
    for i in range(len(testfile)):
        b.add(i,testfile[i])

    print("\nstr(HashTable):\n" + HashTable.__str__.__doc__)
    print("\nHash Table after all testitems are added: \n")
    # prints organized string of the hash table array
    print(b)

    print("iter(HashTable):\n" + HashTable.__iter__.__doc__)
    print("\nIteration through all values in the hash table: \n")
    # prints all elements in the hash
    for item in b:
        print(item)
#--------------------------------------------------------
#-----------------------GET------------------------------
    print("\nHashTable.get(key):\n" + HashTable.get.__doc__)
    print("\nValues of keys in the hash table: \n")
    # prints indexes of each student in the hash table
    for i in range(len(testfile)):
        print("Value of key (" + str(i).strip("\n") + ") : " + str(b.get(i)))

    print("\nValues of keys NOT in the hash table: \n")
    # prints None when element is not in hash table
    print(("Values of key (101): " + str(b.get(101))))
#---------------------------------------------------------
#---------------------REHASH------------------------------
    print("\nHashTable.rehash(size):\n" + HashTable.rehash.__doc__)
    print("\nLength before rehashing into 257:")
    print(len(b))
    #rehashes table into a size 256 table
    print("\nLength after rehashing into 257:")
    b.rehash(257)
    print(len(b))
#---------------------------------------------------------
#-------------------------REMOVE--------------------------
    print("\nHashTable.remove(key):\n" + HashTable.remove.__doc__)
    #removes all items in the hash table
    for item in range(len(testfile)):
        b.remove(item)
    print("\nNo of spaces used in hash table after removing all key-value pairs:")
    print(b.used())
#---------------------------------------------------------
#----------------------CHECKREHASH------------------------
    print("\nHashTable.checkrehash(min, max, multiplier, divisor):\n" + HashTable.checkrehash.__doc__)
    print("\nOriginal length of hash table, and amount of spaces used:")
    print(len(b), b.used())
    #divides hash table by 2 (can be changed) if less than 20% is used(this can be changed to any percentage)
    print("\nAfter checking and rehashing:")
    b.checkrehash()
    print(len(b), b.used())

    #multiplies by 2 (can be changed) if more than 80% is used(this can be changed to any percentage)
    for i in range(504):
        a.add(i, i)
    print("\nOriginal length of hash table, and amount of spaces used:")
    print(len(a), a.used())

    print("\nAfter checking and rehashing:")
    a.checkrehash()
    print(len(a), a.used())
#-----------------------------------------------------------
    print("~~~~~~END OF ANALYSIS FOR SEPARATE CHAINING HASH TABLE~~~~~~~")

chainhashclient()
print("\n" +chainhashclient.__doc__)
