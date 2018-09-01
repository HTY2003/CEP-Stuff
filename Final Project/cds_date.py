import datetime

class Date:
    __slots__ = ('val', 'year', 'month', 'day')
    def __init__(self,val): self.val, self.year, self.month, self.day = int(str(val)[-4:] + str(val)[-6:-4] + str(val)[0:2]), int(str(val)[-4:]), int(str(val)[-6:-4]), int(str(val)[0:2])
    def __str__(self):
        return str(self.day) + '/' + str(self.month) + '/' + str(self.year)
    def isToday(self):
        now = datetime.datetime.now()
        return True if now.day == self.day and now.month == self.month else False
