from cds_attributetree import Attribute_AVL
from cds_date import Date
from ds_set import Set
from ds_dyarray import DyArray
from ds_splaytree import SplayBST
import itertools

class ContactBook:
    __slots__ = ('fname','lname','sex','phone','email','birthday','date','users')
    def __init__(self):
        self.users, self.fname, self.lname, self.email, self.sex, self.phone, self.birthday, self.date =  \
        SplayBST(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL(),Attribute_AVL()

    def __str__(self): return str(self.users)

    def adduser(self, fname, lname, sex, phone, email, birthday, date):
        user = fname + ' ' + lname
        data = DyArray(0, capacity = 8)
        refdict = {self.fname: fname, self.lname:lname, self.sex:sex, self.phone:phone, self.email:email, self.birthday:birthday, self.date:date}
        for i in refdict.values(): data.append(i)
        self.users.add(user, data)
        for i in refdict.keys(): i.add(refdict[i], Set([user]))

    def edituser(self, user, fname=None, lname=None, sex=None, phone=None, email=None, birthday=None, date=None):
        refdict = {sex:(self.sex,2), phone:(self.phone, 3), email:(self.email,4), birthday:(self.birthday,5), date:(self.date,6)}
        newdata = self.users[user]
        if fname or lname:
            self.deleteuser(user)
            if fname: newdata[0] = fname
            if lname: newdata[1] = lname
            for i in refdict.keys():
                if i: newdata[refdict[i][1]] = i
            self.adduser(newdata[0], newdata[1],newdata[2],newdata[3],newdata[4],newdata[5],newdata[6])
            return
        for i in refdict.keys():
            if i is not None:
                tmp = newdata[refdict[i][1]]
                newdata[refdict[i][1]] = i
                refdict[i][0][tmp].delete(user)
                refdict[i][0].add(sex, Set([user]))

    def deleteuser(self, user):
        refdict = {self.fname: 0, self.lname:1, self.sex:2, self.phone:3, self.email:4, self.birthday:5, self.date:6}
        data = self.users[user]
        self.users.delete(user)
        for i in refdict.keys(): i[data[refdict[i]]].delete(user)

    def orsearch(self, fname=None, lname=None, sex=None, phone=None, email=None, birthday=None, date=None):
        refdict = {fname: self.fname, lname:self.lname, sex:self.sex, phone:self.phone, email:self.email, birthday:self.birthday, date:self.date}
        baseset = Set()
        for i in refdict.keys():
            if i is not None:
                attributeset = refdict[i][i]
                if attributeset is not None: baseset = baseset.union(attributeset)
        return baseset

    def andsearch(self, fname=None, lname=None, sex=None, phone=None, email=None, birthday=None, date=None):
        refdict = {fname: self.fname, lname:self.lname, sex:self.sex, phone:self.phone, email:self.email, birthday:self.birthday, date:self.date}
        for i in refdict.keys():
            if i is not None:
                attributeset = refdict[i][i]
                if attributeset is not None:
                    try: baseset = baseset.intersect(attributeset)
                    except UnboundLocalError: baseset = attributeset.copy()
        return baseset

    def simsearch(self, fname=None, lname=None, sex=None, phone=None, email=None, birthday=None, date=None):
        refdict = {fname: self.fname, lname:self.lname, sex:self.sex, phone:self.phone, email:self.email, birthday:self.birthday, date:self.date}
        baseset = Set()
        for i in refdict.keys():
            if i is not None: baseset = baseset.union(Set(list(itertools.chain.from_iterable(x.tolist() for x in refdict[i].simsearch(i)))))
        return baseset

    def usersearch(self, user): return self.users[user]

    def listbyattribute(self,attribute, reverse=False):
        refdict = {'fname': self.fname, 'lname':self.lname, 'sex':self.sex, 'phone':self.phone, 'email':self.email, 'birthday':self.birthday, 'date':self.date}
        return list(itertools.chain.from_iterable(i[1].tolist() for i in refdict[attribute]._inOrderReverseGen(refdict[attribute].root))) if reverse else list(itertools.chain.from_iterable(i[1].tolist() for i in refdict[attribute]._inOrderGen(refdict[attribute].root)))

    def listbyrecentlyaccessed(self, reverse=False):
        return list(i[0] for i in self.users._levelOrderGen(self.users.root))
        #lists sorted user tree

    def min(self, attribute, value):
        refdict = {'phone':self.phone, 'birthday':self.birthday, 'date':self.date}
        if attribute in refdict.keys(): return refdict[attribute].min().tolist()

    def max(self, attribute, value):
        refdict = {'phone':self.phone, 'birthday':self.birthday, 'date':self.date}
        if attribute in refdict.keys(): return refdict[attribute].max().tolist()

    '''def build(self, data):
        #builds data structures from data'''

a = ContactBook()
a.adduser('a', 'a', 0, 83386672, 'randumbperson2003@gmail.com', 22112003, 22112003)
print(a)
a.adduser('b', 'a', 0, 82386672, 'randomperson2003@gmail.com', 23112003, 23112003)
print(a)
a.edituser('a a', sex=1)
print(a)
print(a.listbyrecentlyaccessed())
