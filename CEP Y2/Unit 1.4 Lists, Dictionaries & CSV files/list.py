#https://developers.google.com/edu/python/mylists
'''
Python has a great built-in mylist type named "mylist".
mylist literals are written within square brackets [ ].
mylists work similarly to strings -- use the len() function
and square brackets [ ] to access data, with the first element at index 0. 
'''
colors = ['red', 'blue', 'green']
jumbledlist = [1, 3.14, "hello"] #heterogenous 

print(jumbledlist[-1])

print(colors[0])    ## red
print(colors[2])    ## green
print(len(colors))  ## 3

emptymylist = [] ## Empty mylist
amylist = [1,2]
bmylist = [3,4]
print(amylist+bmylist)


t = [1,2, [3,4]]
print(t)

t[2] = "world"
print(t)

del t[-1]
print(t)
##
##'''
##Python's *for* and *in* constructs are extremely useful,
##and the first use of them we'll see is with mylists.
##The *for* construct -- for var in mylist -- is an easy way to look
##at each element in a mylist (or other collection).
##Do not add or remove from the mylist during iteration.
##'''
squares = [1, 4, 9, 16]
ssum = 0
for num in squares:
    ssum += num
print(ssum)  ## 30
##
##'''
##The *in* construct on its own is an easy way to test
##if an element appears in a mylist (or other collection)
##-- value in collection -- tests if the value is in the collection,
##returning True/False.
##'''
mylist = ['larry', 'curly', 'moe']
if 'curly' in mylist:
    print('yay')

##'''
##The for/in constructs are very commonly used in Python code
##and work on data types other than mylist, so you should just
##memorize their syntax. You may have habits from other languages
##where you start manually iterating over a collection,
##where in Python you should just use for/in.
##'''
##
##
##'''
##mylist Methods
##'''
##
##mylist.append(elem) -- adds a single element to the end of the mylist.
##Common error: does not return the new mylist, just modifies the original.
mylist = ['larry', 'curly', 'moe']
#mylist[3] = 'shemp' #invalid, must use .append()
mylist.append('shemp')         ## append elem at end
##
##mylist.insert(index, elem) -- inserts the element at the given index,
##shifting elements to the right.
mylist.insert(0, 'xxx')        ## insert elem at index 0
print(mylist)

##
##mylist.extend(mylist2) adds the elements in mylist2 to the end of the mylist.
##Using + or += on a mylist is similar to using extend().
mylist.extend(['yyy', 'zzz'])  ## add mylist of elems at end
print(mylist)  ## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']

###Difference between extend and append
lista = [1,2,3]
listb = [5,6]
lista.append(listb)
print(lista) #[1, 2, 3, [5, 6]]
lista = [1,2,3]
listb = [5,6]
lista.extend(listb)
print(lista) #[1, 2, 3, 5, 6]

##mylist.index(elem) -- searches for the given element from
##the start of the mylist and returns its index. Throws a ValueError
##if the element does not appear (use "in" to check without a ValueError).
print(mylist.index('curly'))    ## 2

if 'raffles' in mylist:
    mylist.index('raffles')

#print(mylist.index("raffles")) #ValueError
##
##mylist.remove(elem) -- searches for the first instance of the given element
##and removes it (throws ValueError if not present)
mylist.remove('curly')         ## search and remove that element
##
##mylist.pop(index) -- removes and returns the element at the given index.
##Returns the rightmost element (last) if index is omitted
##(roughly the opposite of append()).
mylist.pop(1)                  ## removes and returns 'larry'
##print(mylist)  ## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']
##
##
##'''
##Sorting list
##The sorted() function shown below is preferred.
##'''
####Returns a new list ['moe', 'shemp', 'xxx', 'yyy', 'zzz'],
####original mylist is unchanged
print(mylist)
print(sorted(mylist))
print(mylist)
##
####Returns a new list sorted in reverse order ['zzz', 'yyy', 'xxx', 'shemp', 'moe']
####original mylist is unchanged
print(sorted(mylist, reverse=True, key=len))
print(mylist)
##
####Sorts list in place. The original position of the items are not preserved
##print(mylist)
##mylist.sort()
##print(mylist)
##
####Reverse sort the list in place. The original position of the items are not preserved
##mylist.sort(reverse=True)
##print(mylist) 
##
##'''
##   List Slices work on lists just as with strings,
##   and can also be used to change sub-parts of the list.
##'''
mylist2 = ['a', 'b', 'c', 'd']
print(mylist2[1:-1])   ## ['b', 'c']
mylist2[0:2] = 'z'    ## replace ['a', 'b'] with ['z']
print(mylist2)         ## ['z', 'c', 'd']

print(mylist2[-1:]) #last element onwards
print(mylist2[-2:]) #last 2 elements onwards
