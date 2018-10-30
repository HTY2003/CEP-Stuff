from cds_attributetrees import Attribute_AVL, Attribute_Date_AVL, User_BST
from cds_date import Date
from ds_set import Set
from ds_dyarray import DyArray
from stat import S_IREAD, S_IRGRP, S_IROTH, S_IWUSR
import itertools
import os

class ContactBook:
    '''
    Contact Book ADT for CEP Final Project
    --------------------------------------
    This is the culmination of all the data structures, consisting of 8 trees

    1st tree (User Tree): SplayBST(key=username, value=DyArray([attributes]))
    2nd to 8th tree (Attribute Trees): AVLBST(key=attribute-value, value=Set([users with value]))
    For Attribute Trees, if the attribute is a date, the Date class is used as the key.

    No time complexities will be listed for the functions, although the time complexities for each
    type of tree and data structures can be found in their individual files

    This class supports adding users with the following attributes:
    * Username
    * First Name
    * Last Name
    * Sex
    * Phone
    * Email
    * Birthday
    * Date Added

    The class can search(similarity, AND, OR), delete, list sorted,
    and find the minimum, maximum, and average of all users by all the above attributes

    In addition, the tree supports saving to write-protected plaintext files,
    and building all user and attribute trees from said plaintext files

    The front-end command line interface can be found in command_line.py
    '''
    __slots__ = ('filename','fname','lname','sex','phone','email','birthday','date','users')

    def __init__(self, filename=None):
        '''Initializes all trees and filename'''
        self.filename, self.users, self.fname, self.lname, self.email, self.sex, self.phone, self.birthday, self.date =  \
        str(filename) + '.txt', User_BST(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_Date_AVL(),Attribute_Date_AVL()

    def __str__(self):
        '''Returns string of user tree'''
        return str(self.users)

    def __contains__(self,key):
        '''Returns whether username is in the user tree'''
        return key in self.users

    def adduser(self, data, username):
        '''Adds username and attribute data into all user and attribute trees'''
        refdict = {0:self.fname, 1:self.lname, 2:self.sex, 3:self.phone, 4:self.email, 5:self.birthday, 6:self.date}
        #USER TREE ADDITION
        self.users.add(username, data)
        #ATTRIBUTE TREE ADDITION
        for i in refdict.keys():
            if data[i] != None: refdict[i].add(data[i], Set([username]))
        del refdict

    def edituser(self, olduser, data, username=None):
        '''Edits any user's 8 attributes' values'''
        #collects old user data
        newdata = self.users[olduser]
        #if username is changing
        if username:
            #old username removed entirely
            self.deleteuser(olduser)
            #updates data on any other changes
            for i in range(len(data)):
                if data[i] != None: newdata[i] = data[i]
            #adds new user with newdata
            self.adduser(newdata, username)
        else:
            #if username is not changing
            refdict2 = {0:self.fname, 1:self.lname, 2:self.sex, 3:self.phone, 4:self.email, 5:self.birthday}
            for i in range(len(data)):
                #only data that has changed will be updated
                if data[i] != None:
                    tmp = newdata[i]
                    #updates entry in user tree
                    newdata[i] = data[i]
                    #removes old entry in attribute tree
                    refdict2[i][tmp].delete(olduser)
                    #adds new entry in attribute tree
                    refdict2[i].add(data[i], Set([olduser]))
            del refdict2

    def deleteuser(self, user):
        '''Removes all instance of user from all trees'''
        refdict = {0:self.fname, 1:self.lname, 2:self.sex, 3:self.phone, 4:self.email, 5:self.birthday, 6:self.date}
        #store attribute data
        data = self.users[user]
        #delete from user tree
        self.users.delete(user)
        for i in refdict.keys():
            #delete from attribute tree
            refdict[i][data[i]].delete(user)
            #remove any empty sets
            if len(refdict[i][data[i]]) == 0: refdict[i].delete(data[i])
        del refdict

    def orsearch(self, data):
        '''OR search: Search for username sets based on given attribute data and finds the union'''
        refdict = {0:self.fname, 1:self.lname, 2:self.sex, 3:self.phone, 4:self.email, 5:self.birthday, 6:self.date}
        baseset = Set()
        for i in refdict.keys():
            #if data for that attribute is provided
            if data[i] != None:
                #search for the corresponding username set
                attributeset = refdict[i][data[i]]
                #union if there is a result
                if attributeset != None: baseset = baseset.union(attributeset)
        del refdict
        return baseset

    def andsearch(self, data):
        '''AND search: Search for username sets based on given attribute data and finds the intersection'''
        refdict = {0:self.fname, 1:self.lname, 2:self.sex, 3:self.phone, 4:self.email, 5:self.birthday, 6:self.date}
        for i in refdict.keys():
            #if data for that attribute is provided
            if data[i] != None:
                #search for the corresponding username set
                attributeset = refdict[i][data[i]]
                #intersect if there is a result
                if attributeset != None:
                    try: baseset = baseset.intersect(attributeset)
                    except UnboundLocalError: baseset = attributeset.copy()
        del refdict
        try: return baseset
        except NameError: return []

    def attrsimsearch(self, data, ors=None):
        '''
        Similarity OR search (if ors is enabled): Search for all username sets based on string similarity to given data and finds the union
        Similarity AND search: Search for username sets based on given attribute data and finds the intersection
        '''
        refdict = {0:self.fname, 1:self.lname, 2:self.sex, 3:self.phone, 4:self.email, 5:self.birthday, 6:self.date}
        if ors: baseset = Set()
        for i in refdict.keys():
            if data[i] != None:
                #union if OR search
                if ors: baseset = baseset.union(Set(list(itertools.chain.from_iterable(x.tolist() for x in refdict[i].simsearch(data[i])))))
                else:
                    #intersect if AND search
                    try: baseset = baseset.intersect(Set(list(itertools.chain.from_iterable(x.tolist() for x in refdict[i].simsearch(data[i])))))
                    except UnboundLocalError: baseset = Set(list(itertools.chain.from_iterable(x.tolist() for x in refdict[i].simsearch(data[i]))))
        del refdict
        try: return baseset
        except NameError: return []

    def usersimsearch(self, user):
        '''Similarity username search: Search for all users with given string in their usernames'''
        return list(self.users.simsearch(user))

    def usersearch(self, user):
        '''User Info search: Return all attribute info of a user based on username and user tree'''
        return self.users[user]

    def listbyattribute(self, attribute, reverse=False):
        '''Lists all users by any of the specified attributes'''
        refdict3 = {'first name': self.fname, 'last name':self.lname, 'sex':self.sex, 'phone number':self.phone, 'email':self.email, 'birthday':self.birthday, 'date added':self.date}
        users = list(refdict3[attribute]._inOrderReverseGen(refdict3[attribute].root)) if reverse else list(refdict3[attribute]._inOrderGen(refdict3[attribute].root))
        del refdict3
        return users

    def listbyusername(self, sorted=False, reverse=False):
        '''Lists all users by username (recently accessed by default)'''
        if sorted: return list(self.users._inOrderReverseGen(self.users.root)) if reverse else list(self.users._inOrderGen(self.users.root))
        else: return list(self.users._levelOrderGen(self.users.root))

    def min(self, attribute):
        '''Returns minimum value and corresponding user(s)'''
        refdict3 = {'first name': self.fname, 'last name':self.lname, 'sex':self.sex, 'phone number':self.phone, 'email':self.email, 'birthday':self.birthday, 'date added':self.date}
        if attribute in refdict3.keys(): min = refdict3[attribute].min()
        else: min = None, None
        del refdict3
        return (min.key, min.val)

    def max(self, attribute):
        '''Returns maximum value and corresponding user(s)'''
        refdict3 = {'first name': self.fname, 'last name':self.lname, 'sex':self.sex, 'phone number':self.phone, 'email':self.email, 'birthday':self.birthday, 'date added':self.date}
        if attribute in refdict3.keys(): max = refdict3[attribute].max()
        else: max = None, None
        del refdict3
        return (max.key, max.val)

    def avg(self, attribute):
        '''Returns average value'''
        #the phone number compatibility is just a dumb joke
        refdict4 = {'sex':self.sex, 'phone number':self.phone}
        if attribute in refdict4.keys():
            value = refdict4[attribute].avg()
            del refdict4
            return value
        return None

    def today(self):
        dateset = Set()
        for i in self.date:
            if i[0].isToday(): dateset = dateset.union(i[1])
        birthdayset = Set()
        for i in self.birthday:
            if i[0].isToday(): birthdayset = birthdayset.union(i[1])
        return (birthdayset, dateset)


    def build(self):
        '''Builds all trees from plaintext in file (this does use eval() but its uses are justified below)'''
        with open(self.filename, 'r') as file:
            data = file.read()
            file.close()
        refdict = {1: self.users, 2:self.fname, 3:self.lname, 4:self.email, 5:self.sex, 6:self.phone, 7:self.birthday, 8:self.date}
        builddata = data.split('\n')
        if len(builddata) == 9:
            if builddata[0] == self.filename:
                for i in range(len(builddata)):
                    if i != 0:
                        if '__' in builddata:
                            self.reset()
                            return 0
                        #eval can be dangerous when user input is accidentally executed
                        #however, this is controlled and formatted data being run
                        #checks have also been made to make sure packages cannot be imported
                        #hence, eval is safe to use
                        refdict[i].treebuild(builddata[i])
                return 1
        return 0

    def save(self, newfile=False):
        '''Gathers the treestr of each tree, and saves it along with the filename in a write-protected file'''
        #creates string
        string = self.filename + '\n' + \
                self.users.treestr() + '\n' + \
                self.fname.treestr() + '\n' + \
                self.lname.treestr() + '\n' + \
                self.email.treestr() + '\n' + \
                self.sex.treestr() + '\n' + \
                self.phone.treestr() + '\n' + \
                self.birthday.treestr() + '\n' + \
                self.date.treestr()
        #set file to write mode temporarily
        if not newfile: os.chmod(self.filename, S_IWUSR|S_IREAD)
        #writes string to file
        with open(self.filename, 'w') as file:
            file.write(string)
            file.close()
        #sets file back to read only
        os.chmod(self.filename, S_IREAD|S_IRGRP|S_IROTH)

    def reset(self):
        '''Empties out all users, and saves'''
        #makes new trees
        self.users, self.fname, self.lname, self.email, self.sex, self.phone, self.birthday, self.date =  \
        User_BST(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_Date_AVL(),Attribute_Date_AVL()
        #and save
        self.save()