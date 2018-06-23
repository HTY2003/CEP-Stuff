#Reference:
# * https://developers.google.com/edu/python/dict-files
# * https://jeffknupp.com/blog/2015/08/30/python-dictionaries/

'''
Python's efficient key/value hash table structure is called a "dict".
The contents of a dict can be written as a series of key:value pairs within braces { },
e.g. dict = {key1:value1, key2:value2, ... }.
The "empty dict" is just an empty pair of curly braces {}.

Looking up or setting a value in a dict uses square brackets,
e.g. dict['foo'] looks up the value under the key 'foo'.
Strings, numbers, and tuples work as keys, and any type can be a value.
Other types may or may not work correctly as keys (strings and tuples work cleanly since they are immutable).
Looking up a value which is not in the dict throws a KeyError
-- use "in" to check if the key is in the dict,
or use dict.get(key) which returns the value or None
if the key is not present (or get(key, not-found) allows you to specify what value to return in the not-found case).
'''

## Can build up a dict by starting with the the empty dict {}
## and storing key/value pairs into the dict like this:
## dict[key] = value-for-that-key
mdict = {} #Constructs an empty dictionary
mdict['a'] = 'alpha'
mdict['g'] = 'gamma'
mdict['o'] = 'omega'

print(mdict)  ## {'a': 'alpha', 'o': 'omega', 'g': 'gamma'}

print(mdict['a'])     ## Simple lookup, returns 'alpha'
mdict['a'] = 6       ## Put new key/value into dict
print(mdict['a'])
print(mdict)
##
'a' in mdict         ## True
#print (mydict['z'])                  ## Throws KeyError
if 'z' in mdict: print(mdict['z'])     ## Avoid KeyError


#wyr = {'prank': ['baotou', 'lookatgirls'], 'dreamgirl': {'prank':['sendsms', 'sendemoji']}}

print(mdict.get('z'))  ## None (instead of KeyError)
##
##
#### Other ways to construct a dictionary
##
###comma-separated list of the form key: value enclosed by braces
a = {1:2, 3:4}
##
###using dict() with two iterables of equal length; the first contains a list of keys and the second contains their associated values.
b = dict(zip([1, 3], [2, 4])) #{1: 2, 3: 4}
##
###using dict() with keyword arguments mapping keys to values (where one and two are valid identifiers)
c = dict(one=2, three=4) #{'one': 2, 'three': 4}
##
###using dict() with an iterable containing iterables with exactly two objects, the key and value
d = dict([(1, 2), (3, 4)]) #{1: 2, 3: 4}
##
##
##'''
##Iterating over dictionary
##A for loop on a dictionary iterates over its keys by default. The keys will appear in an arbitrary order.
##The methods dict.keys() and dict.values() return lists of the keys or values explicitly.
##There's also an items() which returns a list of (key, value) tuples,
##which is the most efficient way to examine all the key value data in the dictionary.
##All of these lists can be passed to the sorted() function.
##'''
##
postoffice = dict(zip(['Sembawang','Woodlands', 'Yishun','Ang Mo Kio','Hougang','Punggol', 'Sengkang', 'Serangoon','Bedok', 'Pasir Ris', 'Tampines','Bukit Batok','Bukit Panjang','Clementi','Jurong', 'Toa Payoh'],
                      [757632, 730900,768794,560727,538766,828815,545025,[550261,550261],460218,518457,529508,658713,689379,[129588,120727],[608532,648886,640492],[310520,310203]]))
print(postoffice)

##
###Printing key:value pair in a dictionary.
##print("Printing key:value pair in dictionary")
##print("="*50)
##print(postoffice)
##
###Printing all the keys - note: this is a dict_key object, not a normal list.
print("Printing all keys")
print("="*50)
print(postoffice.keys())
##
##
###Printing 3rd key in dictionary, first by converting dict_key object into a list before indexing the 3rd element
print("Printing third key")
print("="*50)
print(list(postoffice.keys())[2])
##
###Printing all values in dictionary
print("Printing all values")
print("="*50)
print(postoffice.values())
##
###.items() is the dict expressed as (key, value) tuples
print("Printing all (key,value) pair in dictionary")
print("="*50)
print(postoffice.items())
##
#### By default, iterating over a dict iterates over its keys.
#### Note that the keys are in a random order.
print("Iterating over a dictionary")
print("="*50)
for key in postoffice:
    print(key, postoffice[key])


###Printing the key value pairs
print("Printing key-value pairs")
print("="*50)
for (k,v) in postoffice.items():
    print("Town", k, "Postcodes" ,v)
##
#### Common case -- loop over the keys in sorted order,
#### accessing each key/value
print("Iterating over a dictionary sorted by key")
print("="*50)
for key in sorted(postoffice.keys()):
    print(key, postoffice[key])
##
postoffice2 = dict(zip(['Sembawang','Woodlands', 'Yishun','Ang Mo Kio','Hougang','Punggol', 'Sengkang', 'Serangoon','Bedok', 'Pasir Ris', 'Tampines','Bukit Batok','Bukit Panjang','Clementi','Jurong', 'Toa Payoh'],
                      [757632, 730900,768794,560727,538766,828815,545025,550261,460218,518457,529508,658713,689379,129588,608532,310520]))
##
print(postoffice2)
##
##
###Looking up whether a key exists in a dictionary, postoffice
##if 'Sembawang' in postoffice.keys():
##    print("Postal code: ", postoffice['Sembawang'])
##else:
##    print("Not Found")
##

##    
###Printing the key value pairs sorted by key
##print("Printing key-value pairs sorted by key")
##print("="*50)
##for key in sorted(postoffice.keys()):
##    print(key, postoffice[key])
##
#Printing the key value pairs sorted by value
print("Printing key-value pairs sorted by value")
print("="*50)
for specificpostalcode in sorted(postoffice2.values()):
    print(specificpostalcode, [town for town,postcode in postoffice2.items() if postcode == specificpostalcode])
    '''
    ##Equivalent to the list comprehension above .... by way yan
    l = []
    for town,postcode in postoffice2.items():
        if postcode == specificpostalcode:
            l += town
    '''





            
