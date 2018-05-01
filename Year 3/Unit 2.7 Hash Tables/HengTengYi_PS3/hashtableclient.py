from quadhash import QHashTable
from chainhash import CHashTable
import time

def quadhashclient():
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

    #~~~~~~~~~~~~~~~~~~~(IMPORTANT) function showcase ~~~~~~~~~~~~~~~~~~~~~~~~~
    print("~~~~~~~~~~~~~~ANALYSIS FOR IMPORTANT FUNCTIONS~~~~~~~~~~~~~~~")
    # adds all items into the hash table:
    print("QHashTable.add(element):" + QHashTable.add.__doc__)
    for name in testfile:
        b.add(name)

    print("\nstr(QHashTable):" + QHashTable.__str__.__doc__)
    # prints organized string of the hash table array
    print(b)

    print("\niter(QHashTable):" + QHashTable.__iter__.__doc__)
    # prints all elements in the hash table
    for item in b:
        print(item)

    print("\nQHashTable.get(element):" + QHashTable.get.__doc__)
    # prints indexes of each student in the hash table
    for i in testfile:
        print("Index of " + i + " : " + str(b.get(i)))
    # prints None when element is not in hash table
    print(("Index of 1: " + str(b.get(1))))

    print("\nQHashTable.rehash(size):" + QHashTable.rehash.__doc__)
    #rehashes table into a size 256 table
    b.rehash(256)
    print(len(b))
    #rehashes table into a size 1024 table (auto-calculated from 1000)
    b.rehash(1000, autocal = 1000)
    print(len(b))

    print("\nQHashTable.remove(element):" + QHashTable.remove.__doc__)
    #removes all items in the hash table
    for item in testfile:
        b.remove(item)

    print("\nQHashTable.checkrehash(min, max, multiplier, divisor):" + QHashTable.checkrehash.__doc__)
    print(len(b))
    #halves hash table if less than 20% is used(this can be changed to any percentage)
    b.checkrehash()
    print(len(b))

    #multiplies if more than 80% is used(this can be changed to any percentage)
    print(len(a))
    for i in range(254):
        a.add(i)
    a.checkrehash()
    print(len(a))

    #hash table also automatically rehashes when full
    print(len(c))
    for i in testfile:
        c.add(i)
    print(len(c))
    print("~~~~~~END OF ANALYSIS FOR QUADRATIC PROBING HASH TABLE~~~~~~~")

def chainhashclient():
    """Testing code for the chaining hash table, and showcase of multiple scenarios and functions
    Read source code comments for closer analysis of hash table initialization
    Run the program for analysis of functions"""

    """Case: Any size allowed! But prime numbers recommended"""
    a = CHashTable(107)
    print(a)
    #~~~~~~~~~~~~~~~~~~~(IMPORTANT) function showcase ~~~~~~~~~~~~~~~~~~~~~~~~~
    #add
    print("1) CHashTable.add(element):")
    print(CHashTable.add.__doc__)
    for i in testfile:
        a.add(i)
        b.add(i)
        c.add(i)
    z = input("Press ENTER to continue: ")
    print("Hash table after adding db.txt:")
    time.sleep(2)
    print(b)
    z = input("Press ENTER to continue:")

    #get
    print("\n2) QHashTable.get(element):")
    print(QHashTable.get.__doc__)
    z = input("Press ENTER to continue:")
    print("Indexes of each student in db.txt: ")
    time.sleep(2)
    for i in testfile:
        print("Index of " + i[:-3] + " : " + str(b.get(i)))
    z = input("Press ENTER to continue: ")

    #remove
    print("\n3) QHashTable.remove(element):")
    print(QHashTable.remove.__doc__)
    z = input("Press ENTER to continue: ")
    print("\nBefore removing: ")
    d = QHashTable(4)
    d.add("Tom")
    print(d)
    z = input("Press ENTER to continue: ")
    print("\nAfter removing with QHashTable.remove('Tom'): ")
    d.remove("Tom")
    print(d)
    print("Note: The empty strings also represent empty slots.")
    z = input("Press ENTER to continue: ")

    #rehash
    print("\n4) QHashTable.rehash(size)")
    print(QHashTable.rehash.__doc__)
    z = input("Press ENTER to continue: ")
    print("Original table: ")
    e = QHashTable(2)
    print(e)
    z = input("Press ENTER to continue: ")
    print("\nAfter rehashing with QHashTable.rehash(4): ")
    e.rehash(4)
    print(e)
    z = input("Press ENTER to continue: ")
    print("\nAfter rehashing with QHashTable.rehash(5, autocal=True): ")
    e.rehash(5, autocal=True)
    print(e)
    print("~~~~~~END OF ANALYSIS FOR QUADRATIC PROBING HASH TABLE~~~~~~~")

quadhashclient()
