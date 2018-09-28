import datetime

class Date:
    '''
    A class to display dates in the correct format(DD/MM/YYYY) but compare them in the logical format (YYYYMMDD)
    It can also tell if a date is today!

    Note: Apparently the datetime library already has a class like this, but I didn't know so let's just call me HARDWORKING
    '''

    __slots__ = ('val', 'year', 'month', 'day')
    def __init__(self,val):
        '''Converts DDMMYYYY into this class's attributes'''
        #a lot of string processing to convert a value (DDMMYYYY) into all the needed info
        self.val, self.year, self.month, self.day = int(str(val)[-4:] + str(val)[-6:-4] + str(val)[0:2]), int(str(val)[-4:]), int(str(val)[-6:-4]), int(str(val)[0:2])

    def __str__(self):
        '''Returns a string of date format DD/MM/YYYY'''
        return str(self.day) + '/' + str(self.month) + '/' + str(self.year)

    __repr__ = __str__

    def treestr(self):
        '''Returns a string of format DDMMYYYY for tree building'''
        return str("{0:0=2d}".format(self.day)) + str("{0:0=2d}".format(self.month)) + str(self.year)

    def isToday(self):
        '''Returns whether this date is today'''
        now = datetime.datetime.now()
        return (now.day == self.day and now.month == self.month)

    #---COMPARISON FUNCTIONS---
    # Used for sorting when adding class into a tree
    def __eq__(self, other):
        return self.val == other.val if other != None else False

    def __ne__(self, other):
        return self.val != other.val if other != None else True

    def __gt__(self, other): return self.val < other.val
    def __lt__(self, other): return self.val > other.val
    def __le__(self, other): return self.val <= other.val
    def __ge__(self, other): return self.val >= other.val
