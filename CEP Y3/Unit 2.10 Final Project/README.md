# CEP Final Project

The purpose of this file is to provide an overview and analysis of the data structures and their unique attributes and how they are used within the Contact Book class.

I also suggest reading this in a Markdown Viewer (Ctrl + Shift + M in Atom) or it gets really ugly.

## Data Structures

* Dynamic ctypes Array (DyArray: **ds_dyarray.py**)

* AVL Tree (AVLBST: **ds_avltree.py**)

* Splay Tree (SplayBST: **ds_splaytree.py**)

* Set (Set: **ds_set.py**)
  * Hash Table (HashTable: **ds_hashtable.py**)

### Dynamic Array
```
Indexing/ Slicing
- Time complexity: O(1)

Append
- Time complexity: O(1)

Insert
- Time complexity (Average): O(log n)
- Time complexity (Worst case): O(n)

Pop
- Time complexity: O(1)

Remove
- Time complexity (Average): O(log n)
- Time complexity (Worst case): O(n)

Note: Resizes only when completely full
```

This class is just a basic implementation of a dynamically resizing ctypes array, and was used as the container for the list of atributes in the Contact Book ADT and a general helper class.

Since you can set the array not to resize, it can also function as a static array (which is useful since the number of attributes in the contact book is fixed so there is no need to resize).

### Splay Tree
```
Add
- Time complexity (Average): O(log n)
- Time complexity (Worst case): O(n)

Search
- Time complexity (Average): O(log n)
- Time complexity (Worst case): O(n)

Remove
- Time complexity (Average): O(log n)
- Time complexity (Worst case): O(n)

Sort
- Time complexity: O(n)

Note: O(1) time when accessing recently accessed attributes
```
The splay tree suffers from pretty bad O(n) worst case performance, but it makes up for it with speedy recently accessed searches and the ability to sort in recently accessed order (level order), letting the user list friends in the order of those most recently added/edited.

In the Contact Book class, there is one instance of this class as a User Tree:

Key: Username
Value: DyArray of [first name, last name, sex, phone, email, birthday, date added]

The O(n) sorting that trees can perform also allows the 'Sorting' requirment to be carried out quickly.

### AVL Tree
```
Add
- Time complexity: O(log n)

Search
- Time complexity: O(log n)

Remove
- Time complexity: O(log n)

Sort
- Time complexity: O(n)
```

The splay tree was used for its recent access, but most people don't display users by 'recently accessed attribute'. Hence, it's important to ensure that each attribute of all values can be searched quickly, which is why searching by attribute is done through AVL trees. Their constant O(log n) add/search/delete time makes them very efficient to search with and to remove values from.

There are 7 instances of this class in the Contact Book class, for each of the 7 attributes:

Key: attribute value
Value: Set of usernames of all users with that attribute value

The O(n) sorting trees provide once again let us list out all the users quickly. Since we mentioned sets, let's move on to them.

### Set
```
Add
- Time complexity (Average): O(log n)
- Time complexity (Worst case): O(n)

Search (Lookup)
- Time complexity: O(1)

Remove
- Time complexity: O(1)
```
This set implementation, like the standard Python set is a hash table with keys and dummy values(None in my case), using the O(1) lookup time to quickly perform comparisons between sets to do unions and intersections.

The use of this class was to perform unions and intersections for AND and OR searches quickly, rather than the inefficient process of scanning through an entire array for example.

However, one area in which this implementation is better than the standard Python set is in the lookup time: **constant** O(1)

This is thanks to using cuckoo hashing in my hash table, so we'll go into that next.

### Hash Table
```
Time complexity: same as Sets
```
So as we mentioned, sets are just hash tables with dummy values, so the speed of operations in sets lies in this class. Previously with quadratic probing, O(1) lookup time was not guaranteed. In a completely full hash table (since my probe of i*i+i went through every slot), the search time for an element not in the table was O(n) GUARANTEED, searching through every slot before determining that the element was not in the table.

Obviously, I could not allow for that, so I decided to find some better collision resolution and found cuckoo hashing.

Essentially, there are only two possible index a value can be placed in:
1 is the value hashed using FNV1(used before) and 2 using CRC32(another hashig algo with even less collisions)

This means that when adding, if both slots 1 and 2 are taken, the new value to add pushes out an existing value in slot 1/2 like a cuckoo and the existing value that was pushed out now tries to occupy its other possible index(2/1) and so on and so forth until all values are in the table.

While this clearly means potentially long addition times, searching and deletion are a constant O(1) since there are only 2 possible positions and not the entire table, making the worst case O(n) addition time worth it. Furthermore, the table resizes at 50% to prevent addition from being too sluggish. With 3 algorithm this resize point could reach 91%, but I was pressed for time.

## Contact Book ADT
So, with all the data structures assembled, we can now form a MONSTER class called ContactBook, combining everything together in **cds_contactbook.py**, and we end up with this (using edited trees from **cds_attributetrees.py**):

1 x **User_BST** - An edited SplayBST to use as User Tree

Key: Username

Value: **DyArray** of [first name, last name, sex, phone, email, birthday, date added]

7x **Attribute_AVL** - An edited AVLBST for Attribute Trees

Key: Attribute Value

Value: **Set** of usernames of all users with that attribute value

To search by username, only the User Tree is used to search, and to search by attribute with AND or OR functionality, the attribute values are searching using the Attribute Trees, and the resultant sets are merged/intersected together depending on AND or OR.

String similarity just uses re.match(), and listing is done using the built-in sorting ability of the trees.

And with these trees come their functionalities, which involve:
* **Addition** of users (username + all attributes)
* **AND search** of users by attribute (with or without **string similarity**)
* **OR search** of users by attribute (with or without **string similarity**)
* **Search** of username by username using **string similarity**

NOTE: for these search functions, only the username of the user will be given. The program user can then search the full info of a user by his username using the feature below

* **Search of user info** by EXACT username
* **Editing** user info (all attributes except date added, and username)
* **Deletion** of users by username
* **AND deletion** of users by attribute
* **OR deletion** of users by attribute
* **Save** to a write-protected text file
* **Load** from the same file between uses
* **Search maximum attribute** and its corresponding user(s)
* **Search minimum attribute** and its corresponding user(s)
* **Search average attribute** (phone. no and sex only)
* **Listing** of all users by attribute in **sorted** or **reverse sorted** order
* **Listing** of all users by username in **sorted** or **reverse sorted** order
* **Listing** of all users in **recently accessed** order
* The use of **dates** as attributes in birthday/date added
* Showing the events that happened on a day (show who's birthday it is or show who you added to the book on this day)
* **Resetting** or **reverting** books to their last-saved state

## Command Line Interface

Next up will be a short tutorial covering the program's front-end commands and its capabilities.

The CLI commands were inspired by database languages in their terminology and order, although much more primitive and limited. This might be less user-friendly in terms of number-based paths (which I saw many others doing), but it makes up in terms of speed. With the exception of add which uses prompts to prevent confusion, all the commands can be carried out in one line, much faster than looking at the screen, keying in a number, looking at the screen, keying in another number, and finally following the inflexible options to run the command.

And following my PS2 the code can display **colors** for easy readability of errors and commands, but only when run in a shell or terminal, and the Python package **colorama** has to be installed too to ensure compatibility across all 3 main OSes. I mainly followed this scheme in coloring my messages (although I may have made one or two errors in judgement):

RED: Failure to execute command, most likely due to unopened books or invalid inputs
BLUE: Command was not executed (because it was cancelled) or had unexpected output (e.g. listing users and finding no users)
GREEN: Command was successfully executed with proper output

These were the only colors used to prevent eye damage and also keep everything minimal instead of being rainbow vomit.

### Tutorial

The command line interface can be started by running **command_line.py**, so you should do that, and see `Session started` and a HELP message

So let's start by listing all possible commands by entering `HELP`.
A list of commands should show up, but to be clear we'll go through each command.

1. Create a book called ri by running the command `CREATE ri`. A success message should appear.


2. Open the empty book by running the command `OPEN ri`. Another success message should appear (unless the file has been deleted or tampered with).


3. Now, let's add our own user called ABC (for demonstration purposes). Start with `ADD ABC` and a series of prompts will appear. Answer them as such:
  ```
  First Name? a
  Last Name? z
  Sex? [M/F] M
  Phone Number? 90000000
  Email? fake1@gmail.com
  Birthday? [DDMMYYYY] 11051996
  ```
  After you've added ABC, let's make another user called XYZ with these attributes:
  ```
  ADD XYZ
  First Name? a
  Last Name? a
  Sex? [M/F] M
  Phone Number? 10000000
  Email? fake2@gmail.com
  Birthday? [DDMMYYYY] <use today's date>
  ```

  Finally, you can try adding yourself now! Just follow the same format and prompts as the previous 2.

  You can try doing something wrong like entering in letter for a phone number or a date, but the prompt will reprompt you after an error message.

  **Note**: there is no character limit for phone number to maintain useability worldwide, and there is no time range for dates to maintain useability throughout all of time.


4. Now, let's save our users with `SAVE`, and a `y` to confirm.


5. Moving on, we'll start with editing users. The `EDIT` command is carried out in this format: `EDIT <username> [<attribute>=value, <attribute>=value]`

  So if we want to change XYZ's sex to female and his first name to z, a valid command would be `EDIT XYZ [sex=F, first name = z]`, so run this command, and we'll see the results later.


6. Then we'll delete the user you made as yourself. You can delete by username:
 `DELETE <your username>`

 Or delete by attribute:  `DELETE BY ATTRIBUTE OR [phone no=<your phone number>]` or `DELETE BY ATTRIBUTE AND [first name = <your first name>, last name = <your last name>]`. The `AND` and `OR` determine the criteria by which you delete (use `AND` if all the attributes must match, and `OR` if you only need one attribute to match).


7. Now save again with `SAVE`.


8. Finally, we go into searching. There are many ways to search, but let's assume that you want to find a friend who is male and has a first name 'a'. Then we can use similar syntax to search like this: `SEARCH BY ATTRIBUTE AND [sex=M, first name=a]`
You can use `OR` and any other attributes to accomplish any attribute search you need.
 To search by string similarity, put the `-simsearch` flag at the end of the command.

  However, these commands will only show you usernames. What if you want all the data of a friend?

  To do that, you need to use the command `SEARCH <username>`. Since the above search gives us 'ABC', we can find out his data by running `SEARCH ABC`.


9. Finally, we go into listing. You can list all usernames with `LIST`. Just `LIST` will list in recently accessed order, while `LIST BY USERNAME` will list them sorted by username, and `LIST BY ATTRIBUTE <attribute>` will list them sorted by your specified attribute.

  If you need to see the data sorted in reverse, just put the `-reverse` flag at the end of your command. However, this does not work for the default `LIST`.

  A problem with the usual `LIST` function is that it only states the attribute value and the username instead of all the user data.
  To show all the user data, simply use `LISTALL` instead of `LIST`.


10. You can try `SEARCH MAX ATTRIBUTE <attribute>`,  `SEARCH MIN ATTRIBUTE <attribute>`, or  `SEARCH AVG ATTRIBUTE <attribute>` to find the minimum, maximum, or average values of each attribute. Keep in mind that averages can only be found for the attributes phone number and sex.


11. `TODAY` shows whether today was the date of any events such as birthdays or the date you added one of your current friends.


12. `RESET` empties out all the friends in your book, `RENAME` lets you rename your book, while `REVERT` undoes any changes you made after your last save, and `BURN` deletes your book.


12. To close your book, use `CLOSE`. To exit the program, use `EXIT`. Thank you!
