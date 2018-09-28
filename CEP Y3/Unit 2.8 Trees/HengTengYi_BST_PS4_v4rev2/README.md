Splay Tree ADT in Python
============================

This notebook contains a Python Implementation of a Splay Tree.

The difference between such a tree and a normal binary search tree is that after adding or searching a node, the node is splayed to the top of the tree, and after deleting a node, its parent is splayed to the top of the tree. This characteristic of recently-accessed nodes being near the top of the tree means that frequently accessed nodes can be searched very quickly, making it superior to normal search trees when used with non-random datasets.

## Time Complexity
Unlike binary search trees, which have a worst-case time complexity of O(log n) for access, insertion, and deletion, splay trees have worst-case operations of O(n), although these operations are infrequent, so its amortized time complexity is still O(log n).

However, the tradeoff that this provides is extremely fast access to more frequently accessed nodes. With movie datasets, where the movie with the higher scores and popularity will get searched much more than the others, Tasks 7 and 8 might be finished in O(1) time.

Furthermore, the splaying operations performed typically give the tree self-balancing properties, allowing for faster average search times than normal search trees.

## Space Complexity
This implementation uses linked nodes, making it more memory intensive than single arrays. However, some measures have been taken to prevent memory usage from being too much.

Firstly, the class attributes for nodes and trees were stored in static amounts of memory allocated for the fixed number of attributes instead of the dynamic dictionary that Python defaults to using. This simple one-line setting can reduce RAM usage by up to 40%.

Secondly, deleted nodes are freed from memory, ensuring there is no unnecessarily wasted memory when nodes are deleted.

With these measures, the tree and nodes will use up much less memory, so it will not be a huge problem.

##ADTs, Client Code and Testing
The linked list node implementation can be found in *splaynode.py*, the dynamic array ADT holding values of duplicate keys in *dyarray.py* while the main splay tree ADT can be found in  *splaytree.py*. For testing (and completion of this problem set), a dataset of 140 movies (in *movies.txt*) will be used in the splay tree, with the goal of completing 8 tasks:

* Addition of movie records
* Deletion of movie records
* Search by movie title (full title)
* Count number of titles with less than y million dollars in box office
* Displays all titles with box office within range [a, b]
* Printing the movie that has the highest box office
* Printing of movie titles sorted by ascending score
* Displays all titles with more than x score

To accomplish these tasks, some extra specialized functions were needed, so more specialized trees were made to handle
different values as their keys (movie titles, review scores, and box office earnings), found in *movietrees.py*.

Finally, the client code to do this tasks is in *client.py*, with task 1 being done as an initialization of variables, and task 2-8 separated into functions before running. You can run the program and look at the print to make sure it works.
