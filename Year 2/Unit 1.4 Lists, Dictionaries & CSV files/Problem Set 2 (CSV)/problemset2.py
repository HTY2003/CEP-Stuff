import csv
choiceFile= open('newchoices.csv') #accesses choices
choiceReader= csv.reader(choiceFile)
choiceData=list(choiceReader)
venueFile= open('venues.csv') #accesses venues
venueReader= csv.reader(venueFile)
venueData=list(venueReader)
alloFile=open('allocations.csv','w', newline='')
alloWriter=csv.writer(alloFile)

choiceslist=[]
usedlist=[]
eventlist=[]
eventdict={}
venuesdict={}
allolist=[]
allorow=[]

def venueandeventdictionary():
    global venuesdict
    global eventdict
    global eventlist
    for row in venueData:
        venuesdict[row[0]]=int(row[1])
        eventlist.append(row[0])
    for row in enumerate(eventlist,start=1):
        eventdict[row[0]]=row[1]
def dateandrepeatssort():
        global choiceslist
        for row in choiceData: #process raw choices data
                if row[0] == 'Timestamp':
                        continue #skips that column
                if row[1] in usedlist: #means an NRIC that has been used before
                        # update existing with new time
                        choiceslist[choiceslist.index([j for j in choiceslist if j[1] == row[1]][0])] = row
                else: #means this is the first submission
                        choiceslist.append(row)
                        usedlist.append(row[1]) #submission is recorded as used
        choiceslist.sort() #sort according to date
def alloWrite():
    global allolist
    global allorow
    def allocating(a,i,row,noofchoices): #sorts all students into their groups
        if i <= noofchoices:
            allocatedvenue=eventdict[int(row[i+3])]
            if venuesdict[eventdict[int(row[i+3])]] > 0:
                allorow=[row[1],row[2],row[3],allocatedvenue,i]
                allolist.append(allorow)
                venuesdict[eventdict[int(row[i+3])]]=venuesdict[eventdict[int(row[i+3])]]-1
            elif venuesdict[eventdict[int(row[i+3])]] == 0:
                allocating(a,i+1,row,13)
        elif i > noofchoices:
            if  a <= noofchoices:
                allocatedvenue=eventdict[a]
                if venuesdict[eventdict[a]] > 0:
                    allorow=[row[1],row[2],row[3],allocatedvenue,1] #they got their first choice...*cough cough*
                    allolist.append(allorow)
                    venuesdict[eventdict[int(a)]]=venuesdict[eventdict[a]]-1
                elif venuesdict[eventdict[a]] == 0:
                    allocating(a+1,i,row,13)
    allorow=['NRIC','Name','Class','Venue Allocated','Choice Allocated']
    allolist.append(allorow)
    for row in choiceslist:
        allocating(1,1,row,13)#insert the number of choices(13) as 4th number
    for row in allolist:
        alloWriter.writerow(row)#transfers data into csv file
def basic():
   venueandeventdictionary()
   dateandrepeatssort()
   alloWrite()

basic()
