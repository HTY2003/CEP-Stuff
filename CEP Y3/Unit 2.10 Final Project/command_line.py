import os
import re
import itertools
import datetime as dt
from colorama import Fore, Back, Style
from ds_dyarray import DyArray
from ds_set import Set
from cds_contactbook import ContactBook
from cds_date import Date

class Color:
    def red(msg): print(Fore.RED + Style.BRIGHT + msg + Style.RESET_ALL)
    def blue(msg): print(Fore.BLUE + Style.BRIGHT + msg + Style.RESET_ALL)
    def green(msg): print(Fore.GREEN + Style.BRIGHT + msg + Style.RESET_ALL)
    def bold(msg): print(Style.BRIGHT + msg + Style.RESET_ALL)

def main():
    def help(useless):
        print('''Commands:
    CREATE <book name> - Used to create new books
    OPEN <book name> - Used to open existing books
    CLOSE - Used to close open books
    EXIT - Used to end session
    SAVE - Used to save progress on open books
    RENAME <new book name> - Used to rename the book
    REVERT - Undoes all actions done after last save
    RESET - Clear all friends from existing books
    BURN - Delete book forever

    TODAY - Shows all events that happened on this day of the year

    ADD <username>
    - Used to add new user into open book
    Then, prompts for the user attributes will apppear
    If a username is not provided, the user's first name and last name will be used

    EDIT <username> [<attribute>=value, <attribute>=value]
    - Used to edit an existing user's information
    - Possible Attributes: [username, first name, last name, sex[M/F], phone number, email, birthday[DDMMYYYY]]

    DELETE <username>
    DELETE BY ATTRIBUTE OR [<attribute>=value, <attribute>=value, <attribute>=value ...]
    DELETE BY ATTRIBUTE AND [<attribute>=value, <attribute>=value, <attribute>=value ...]
    - Possible Attributes: [first name, last name, sex[M/F], phone number, email, birthday[DDMMYYYY], date added[DDMMYYYY]]

    SEARCH <username>
    - Used to find out the attributes of a user

    SEARCH BY USERNAME <string>
    - Used to find all users with usernames which contain the specified string

    SEARCH BY ATTRIBUTE OR [<attribute>=value, <attribute>=value, <attribute>=value ...] (-simsearch)
    SEARCH BY ATTRIBUTE AND [<attribute>=value, <attribute>=value, <attribute>=value ...] (-simsearch)
    - Used to find all users which attributes have the following values
    - Use the -simsearch flag to search users with attributes which contain the specified string
    - Possible Attributes: [first name, last name, sex[M/F], phone number, email, birthday[DDMMYYYY], date added[DDMMYYYY]]

    SEARCH MAX ATTRIBUTE <attribute>
    SEARCH MIN ATTRIBUTE <attribute>
    - Possible Attributes: [first name, last name, sex, phone number, email, birthday, date added]

    SEARCH AVG ATTRIBUTE <attribute>
    - Possible Attributes: [sex, phone number]

    LIST - List all usernames in recently accessed order
    LIST BY USERNAME (-reverse)
    - List all usernames in sorted order according to username
    - Use the -reverse flag to list usernames in reverse sorted order

    LIST BY ATTRIBUTE <attribute> (-reverse)
    - List all usernames in sorted order according to specified attribute
    - Use the -reverse flag to list usernames in reverse sorted order
    - Possible Attributes: [first name, last name, sex, phone number, email, birthday, date added]

    LISTALL ~
    - Use LISTALL instead of LIST to show all the user data instead of just listing usernames like in LIST ''')

    def _yesno(msg, bold=False):
        '''Asks users a question, and return True or False based on the reply'''
        if not bold: qn = input(msg)
        else: qn = input(Style.BRIGHT + msg + Style.RESET_ALL)
        #check for Y or N
        if qn.upper() == 'Y': return True
        elif qn.upper() == 'N': return False
        #error msg and loop function
        Color.red('Invalid reply: Reply should be "y" or "n"')
        return _yesno(msg)

    def _checksaved():
        '''Asks users if he wants to save'''
        if _yesno('Would you like to save your work? [y/n]: '):
            main.book.save()
            main.saved = True
            Color.green('Book ' + main.book.filename[:-4] + ' saved')

    def _process(data, mode=None, sim=None, date_added=None):
        '''
        Process string of [<attribute>=value, <attribute>=value, <attribute>=value ...]
        and analyses it to make sure the data is valid for searching or editing
        '''
        #checks format
        if '[' in data[0] and ']' in data[-1]:
            #removes square brackets
            data[0] =  data[0][1:]
            data[-1] = data[-1][:-1]
            #attrdict stores the location and type of reply of each attribute
            attrdict = {'username':(4,0),'first name':(0, 0), 'last name':(0, 1), 'sex':(3,2) ,'phone number':(1, 3), 'email':(3.5, 4), 'birthday':(2, 5)}
            if date_added: attrdict['date added'] = (2, 6)
            #heavily processing the strings into a dict such that {attribute:value}
            datadict = {i[0].lower():i[1] for i in list(x.split('=') for x in ' '.join(data).replace(' =', '=').replace('= ', '=').replace(', ', ',').replace(' ,', ',').split(',')) if len(i) == 2}
            #creates veriables to fill
            newname = None
            newdata = DyArray(7, capacity=7)
            for i in datadict.keys():
                if i in attrdict.keys():
                    #---checks for normal search---
                    if sim is None:
                        type, pos = attrdict[i]
                        #No Check (String)
                        if type == 0:
                            newdata[pos] = datadict[i]
                        #Integer Check
                        elif type == 1:
                            try: newdata[pos] = int(datadict[i])
                            except ValueError:
                                Color.red('Invalid data format: Variable ' + i + ' should be an integer')
                                return
                        #Date Check
                        elif type == 2:
                            if sim: newdata[pos] = datadict[i]
                            elif len(datadict[i]) == 8:
                                try:
                                    if int(datadict[i][-4:]) < 2020:
                                        newdata[pos] = Date(int(datadict[i]))
                                    else:
                                        Color.red('Invalid data format: Date comes from the future!!!')
                                except ValueError:
                                    Color.red('Invalid data format: Variable ' + i + ' must be in numerical form')
                                    return
                            else:
                                Color.red('Invalid data format: Variable ' + i + ' must be in valid date format (DDMMYYYY)')
                                return
                        #Sex Check
                        elif type == 3:
                            if datadict[i].upper() == 'M': newdata[pos] = 0
                            elif datadict[i].upper() == 'F': newdata[pos] = 1
                            else:
                                Color.red('Invalid data format: Variable ' + i +' should be "M" or "F"')
                                return
                        #Email Check
                        elif type == 3.5:
                            if re.match(r'[^@]+@[^@]+\.[^@]+', datadict[i]): newdata[pos] = datadict[i]
                            else:
                                Color.red('Invalid data format: Variable ' + i +' should have a valid email format')
                                return
                        elif mode and type == 4: newname = datadict[i]

                    else:
                        #---checks for similarity search---
                        type, pos = attrdict[i]
                        #Sex Check
                        if type == 3:
                            if datadict[i].upper() in ['M', 'MA', 'MAL', 'MALE']: newdata[pos] = 0
                            elif datadict[i].upper() in ['F','FE','FEM', 'FEMA', 'FEMAL', 'FEMALE']: newdata[pos] = 1
                        #Date Check
                        elif type == 2:
                            if sim: newdata[pos] = datadict[i]
                            elif len(datadict[i]) == 8:
                                try:
                                    if int(datadict[i][-4:]) < 2020:
                                        newdata[pos] = Date(int(datadict[i]))
                                    else:
                                        Color.red('Invalid data format: Date comes from the future!!!')
                                except ValueError:
                                    Color.red('Invalid data format: Variable ' + i + ' must be in numerical form')
                                    return
                            else:
                                Color.red('Invalid data format: Variable ' + i + ' must be in valid date format (DDMMYYYY)')
                                return
                        #Integer Check
                        elif type == 1:
                            try: newdata[pos] = int(datadict[i])
                            except ValueError:
                                Color.red('Invalid data format: Variable ' + i + ' should be an integer')
                                return
                        #No Check (String)
                        else: newdata[pos] = datadict[i]

                #error msg for no attributes
                else:
                    Color.red('Invalid data: Attributes given are invalid')
                    return
            return (newdata, newname) if mode is not None else newdata
        else: Color.red('Invalid data format: List of values not given')

    def create(commandlist):
        filename = ' '.join(commandlist[1:])
        #if file with that name does not exist
        if not os.path.exists(filename + '.txt'):
            #create a new book
            newbook = ContactBook(' '.join(commandlist[1:]))
            newbook.save(True)
            Color.green('Book ' + ' '.join(commandlist[1:]) + ' created')
        else:
            Color.blue('File with name ' + ' '.join(commandlist[1:]) + ' already exists')

    def open(commandlist):
        #if a book is not already open
        if not main.book:
            filename = ' '.join(commandlist[1:])
            #if book exists
            if os.path.exists(filename +'.txt'):
                main.saved, main.book = True, ContactBook(filename)
                reply = main.book.build()
                #if build is successful
                if reply == 1: Color.green('Book ' + filename + ' opened')
                #if build is not successful
                else:
                    Color.red('Book ' + filename + ' corrupted')
                    main.book, main.saved = None, None
            else:
                Color.red('Book ' + filename + ' does not exist')

        #if opening the book already open
        elif main.book.filename[:-4] == ' '.join(commandlist[1:]):
            Color.blue('Book ' + main.book.filename[:-4] + ' already open')

        #if opening a new book (and if user agrees to closing existing book)
        elif _yesno('Book ' + main.book.filename[:-4] + ' still open. Would you like to close it? [y/n] '):
            if not main.saved: _checksaved()
            Color.green('Book ' + main.book.filename[:-4] + ' closed')
            main.saved, main.book = None, None
            open(commandlist)

        #cancels command
        else: Color.blue('Command cancelled')

    def close(useless):
        if main.book:
            #checks if book is saved yet
            if main.saved is False: _checksaved()
            #asks, then does
            if _yesno('Are you sure you want to close this book? [y/n]: '):
                Color.green('Book ' + main.book.filename[:-4] + ' closed')
                main.saved, main.book = None, None
            else: Color.blue('Command cancelled')
        else: Color.red('No book open')

    def exit(useless):
        #checks if book is saved yet
        if main.saved is False: _checksaved()
        #asks, then does
        if _yesno('Are you sure you want to end this session? [y/n] '): main.done = True
        else: Color.blue('Command cancelled')

    def save(useless):
        #asks, then does
        if main.book:
            if _yesno('Would you like to save your work? [y/n]: '):
                #saves book
                main.book.save()
                main.saved = True
                Color.green(main.book.filename[:-4] + ' saved')
            else: Color.blue('Command cancelled')
        else: Color.red('No book open')

    def rename(commandlist):
        if main.book:
            #asks, then does
            if _yesno('Are you sure you want to rename this book? [y/n]'):
                #new name is everything after RENAME
                filename = ' '.join(commandlist[1:])
                #makes sure file doesn't already exist
                if not os.path.exists(filename + '.txt'):
                    #removes old file
                    os.remove(main.book.filename)
                    #makes new setting
                    main.book.filename = filename + '.txt'
                    #saves to new file
                    main.book.save(newfile=True)
                    Color.green('Book renamed to ' + main.book.filename[:-4])
                else: Color.red('File with name ' + ' '.join(commandlist[1:]) + ' already exists')
            else: Color.blue('Command cancelled')
        else: Color.red('No book open')

    def revert(useless):
        #asks, then does
        if _yesno('Do you want to revert all actions to previous save? [y/n]'):
            main.book.build()
            Color.green('Book ' + main.book.filename[:-4] + ' reverted')
        else: Color.blue('Command cancelled')

    def reset(useless):
        if main.book:
            #asks, then does
            if _yesno('Are you sure you want to reset this book? [y/n]', bold=True):
                main.book.reset()
                Color.green('Book ' + main.book.filename[:-4] + ' cleared')
            else: Color.blue('Command cancelled')
        else: Color.red('No book open')

    def burn(useless):
        if main.book:
            if _yesno('Are you sure you want to burn this book? [y/n]: '):
                if _yesno('Are you VERY sure? [y/n]:'):
                    os.remove(main.book.filename)
                    Color.green('Book ' + main.book.filename[:-4] + ' deleted')
                    main.saved, main.book = None, None
                else: Color.blue('Command cancelled')
            else: Color.blue('Command cancelled')
        else: Color.red('No book open')

    def today(useless):
        if main.book:
            bd, d = main.book.today()
            #print birthdays
            if len(bd) != 0:
                Color.green("The following friends have their birthdays today: ")
                for i in bd: print(i[0])
            else: Color.blue("No friends' birthday today")
            print('')
            #print date added
            if len(d) != 0:
                Color.green("You added the following friends today: ")
                for i in d: print(i[0])
            else: Color.blue("No friends were added today")
        else: Color.red('No book open')

    def add(commandlist):
        def ask(type, msg):
            #Asks question
            qn = input(msg)
            #Integer Check
            if type == 1:
                try: return int(qn)
                except ValueError: Color.red('Invalid response: Variable must be an integer')
            #Date Check
            elif type == 2:
                if len(qn) == 8:
                    try:
                        if int(qn[-4:]) < 2020: return Date(int(qn))
                        else: Color.red('Invalid data format: Date comes from the future!!!')
                    except ValueError: Color.red('Invalid response: Variable must be in numerical form')
                else: Color.red('Invalid response: Variable must be in valid date format (DDMMYYYY)')
            #Sex Check
            elif type == 3:
                if qn.upper() == 'M': return 0
                elif qn.upper() == 'F': return 1
                else: Color.red('Invalid response: Variable should be "M" or "F"')
            #Email Check
            elif type == 3.5:
                if re.match(r'[^@]+@[^@]+\.[^@]+', qn): return qn
                else: Color.red('Invalid response: Variable should have a valid email format')
            else: return qn
            return ask(type, msg)

        def aduser(id):
            qndict = {'First Name? ':(0, 0), 'Last Name? ':(0, 1), 'Sex? [M/F] ':(3,2) ,'Phone Number? ':(1, 3), 'Email? ':(3.5, 4), 'Birthday? [DDMMYYYY] ':(2, 5)}
            data = DyArray(7, capacity=7)
            #ask for each attribute to prevent confusion
            for i in qndict.keys(): data[qndict[i][1]] = ask(qndict[i][0], i)
            #creates final attribute (date added)
            now = dt.datetime.now()
            data[6] = Date(str('{0:0=2d}'.format(now.day)) + str('{0:0=2d}'.format(now.month)) + str(now.year))
            #uses fname + lname if username is not provided
            if id is None: id = data[0] + ' ' + data[1]
            #if user with username already exists
            if id in main.book:
                #asks if he wants to delete existing user
                if _yesno('User ' + id + ' already exists. Would you like to delete this user?[y/n]'): main.book.deleteuser(id)
                else:
                    Color.blue('Command cancelled')
                    return
            #otherwise, the new user is added
            main.book.adduser(data,id)
            main.saved = False
            Color.green('User ' + id + ' added')

        if main.book:
            if len(commandlist) > 1:
                id = ' '.join(commandlist[1:])
                aduser(id)
            else: Color.red('No username given')
        else: Color.red('No book open')

    def edit(commandlist):
        if main.book:
            if len(commandlist) > 1:
                for i in range(len(commandlist)):
                    if '[' in commandlist[i]:
                        startpos = i
                        break
                    else: startpos = 1
                if startpos - 1 >= 1:
                    #combine attribute info
                    id = ' '.join(commandlist[1:startpos])
                    #check and process attribute info into attribute data
                    check = _process(commandlist[startpos:], mode=True, date_added=False)
                    if check != None:
                        if id in main.book:
                            #edit user
                            main.book.edituser(id, check[0], username=check[1])
                            main.saved = False
                            Color.green('User ' + id + ' edited')
                        else: Color.red('User ' + id + ' not found')
                else: Color.red('Invalid command: List of values not given')
            else: Color.red('No username given')
        else: Color.red('No book open')

    def delete(commandlist):
        def deluser(id):
            '''Deletion process for many people'''
            #makes sure user exists
            if id in main.book:
                #double confirms with user
                if _yesno('Are you sure to want to delete user '+ id + '? [y/n] '):
                    main.book.deleteuser(id)
                    main.saved = False
                    Color.green('User ' + id + ' deleted')
                else: Color.blue('Command cancelled')
            else:
                Color.blue('User ' + id + ' not found: ignoring this user')

        def deluser2(id):
            '''Deletion process for one person'''
            #makes sure user exists
            if id in main.book:
                #double confirms with user
                if _yesno('Are you sure to want to delete user '+ id + '? [y/n] '):
                    main.book.deleteuser(id)
                    main.saved = False
                    Color.green('User ' + id + ' deleted')
                else: Color.blue('Command cancelled')
            else:
                Color.red('User ' + id + ' not found')

        if main.book:
            if len(commandlist) > 1:
                if len(commandlist) > 3:
                    #if deleting by attribute
                    if commandlist[1].upper() + ' ' + commandlist[2].upper() == 'BY ATTRIBUTE':
                        if len(commandlist) > 4:

                            #AND deletion
                            if commandlist[3].upper() == 'AND':
                                data = _process(commandlist[4:])
                                if data != None:
                                    #deletes each user in search result
                                    for i in main.book.andsearch(data): deluser(i[0])

                            #OR deletion
                            elif commandlist[3].upper() == 'OR':
                                data = _process(commandlist[4:])
                                if data != None:
                                    #deletes each user in search result
                                    for i in main.book.orsearch(data): deluser(i[0])

                            else: Color.red('Invalid command: ' + commandlist[3])
                        else: Color.red('Invalid command: ' + ' '.join(commandlist))

                    #otherwise deletes user(assumed username is everything after DELETE)
                    else: deluser2(' '.join(commandlist[1:]))
                else: deluser2(' '.join(commandlist[1:]))
            else: Color.red('No username given')
        else: Color.red('No book open')

    def search(commandlist):
        def user_info(username, lyst):
            Color.green('User found')
            template = ('Username', 'First Name', 'Last Name', 'Sex', 'Phone Number', 'Email Address', 'Birthday', 'Date Added')
            for i in range(len(template)):
                if i == 0: print(template[i] + ': ' + username)
                elif i == 3: print(template[i] + ': ' + ('Male' if lyst[i-1]==0 else 'Female'))
                else: print(template[i] + ': ' + str(lyst[i-1]))

        def user_list(userset):
            if len(userset) == 0: Color.red('No users found')
            else:
                Color.green('Users found: ')
                for i in userset: print(i[0])

        if main.book:
            if len(commandlist) >= 3:
                command = commandlist[1].upper() + ' ' + commandlist[2].upper()
                id = ' '.join(commandlist[3:])

                #search usernames by string similarity
                if command == 'BY USERNAME':
                    user_list(main.book.usersimsearch(id))

                #search usernames by attribute
                elif command == 'BY ATTRIBUTE':
                    if len(commandlist) > 4:

                        #AND search
                        if commandlist[3].upper() == 'AND':
                            #checks for similarity search flag
                            if commandlist[-1] == '-simsearch': data, sim = _process(commandlist[4:-1], sim=True, date_added=True), True
                            else: data, sim = _process(commandlist[4:],date_added=True), False
                            if data != None:
                                if sim: user_list(main.book.attrsimsearch(data))
                                else: user_list(main.book.andsearch(data))

                        #OR search
                        elif commandlist[3].upper() == 'OR':
                            #checks for similarity search flag
                            if commandlist[-1] == '-simsearch': data, sim = _process(commandlist[4:-1], sim=True, date_added=True), True
                            else: data, sim = _process(commandlist[4:], date_added=True), False
                            if data != None:
                                if sim: user_list(main.book.attrsimsearch(data, True))
                                else: user_list(main.book.orsearch(data))
                        else: Color.red("Invalid command: 'AND' or 'OR' not specified")
                    else: Color.red("Invalid command: 'AND' or 'OR' not specified")

                #maximum attribute
                elif command == 'MAX ATTRIBUTE':
                    attr = id.lower()
                    if attr in attrset:
                        data = main.book.max(id)
                        if data[1] != None:
                            if len(data[1]) != 0:
                                Color.green('Maximum value of attribute (' + id + '): ' + str(data[0]))
                                print('User(s) with maximum attribute:')
                                for i in data[1]: print(i[0])
                            else: Color.blue('No users with attribute found')
                        else: Color.blue('No users with attribute found')
                    else: Color.red('Invalid attribute: ' + attr)

                #minimum attribute
                elif command == 'MIN ATTRIBUTE':
                    attr = id.lower()
                    if attr in attrset:
                        data = main.book.min(id)
                        if data[1] != None:
                            if len(data[1]) != 0:
                                Color.green('Minimum value of attribute (' + id + '): ' + str(data[0]))
                                print('User(s) with minimum attribute:')
                                for i in data[1]: print(i[0])
                            else: Color.blue('No users with attribute found')
                        else: Color.blue('No users with attribute found')
                    else: Color.red('Invalid attribute: ' + attr)

                #average attribute
                elif command == 'AVG ATTRIBUTE':
                    attr = id.lower()
                    if attr == 'phone number':
                        data = main.book.avg(attr)
                        if data != None: Color.green('Average value for attribute (Phone Number): ' + str(data))
                        else: Color.blue('No users with attribute found')
                    elif id == 'sex':
                        data = main.book.avg(attr)
                        if data != None:
                            if data == 0: Color.green('Average value for attribute (Sex): ' + str(data) + ' [All male]')
                            elif data < 0.25: Color.green('Average value for attribute (Sex): ' + str(data) + ' [Mostly male]')
                            elif data < 0.5:Color.green('Average value for attribute (Sex): ' + str(data) + ' [Slightly more males than females]')
                            elif data == 0.5: Color.green('Average value for attribute (Sex): ' + str(data) + ' [Equal number of males and females]')
                            elif data < 0.75: Color.green('Average value for attribute (Sex): ' + str(data) + ' [Slightly more females than males]')
                            elif data < 1: Color.green('Average value for attribute (Sex): ' + str(data) + ' [Mostly female]')
                            elif data == 1: Color.green('Average value for attribute (Sex): ' + str(data) + ' [All female]')
                        else: Color.blue('No users with attribute found')
                    else: Color.red('Invalid attribute: ' + id)

                #defaults to USER INFO search
                else:
                    id = ' '.join(commandlist[1:])
                    searchans = main.book.usersearch(id)
                    if searchans != None: user_info(id, searchans)
                    else: Color.red('User not found: ' + id)
            #defaults to USER INFO search
            else:
                id = ' '.join(commandlist[1:])
                searchans = main.book.usersearch(id)
                if searchans != None: user_info(id, searchans)
                else: Color.red('User not found: ' + id)
        else: Color.red('No book open')

    def lister(commandlist):
        #this function in particular is really messy, the time limitations forced out the primitive coder in me
        def listall(username=None, attribute=None, attrstring='', sorttype=None):
            template2 = ('Username', 'First Name', 'Last Name', 'Sex', 'Phone Number', 'Email Address', 'Birthday', 'Date Added')
            template = DyArray(8, capacity=8)
            for i in range(len(template2)):
                if username != None and i == 0: template[i] = Fore.GREEN + Style.BRIGHT + template2[i] + Style.RESET_ALL
                elif template2[i].lower() == attrstring: template[i] = Fore.GREEN + Style.BRIGHT + template2[i] + Style.RESET_ALL
                else: template[i] = template2[i]

            #list all data for username
            if username != None:
                if len(username) != 0:
                    Color.green('All user data in ' + sorttype + ' order by username:')
                    print(' | '.join(template))
                    for id in username:
                        newdata = DyArray(7, capacity=7)
                        for i in range(7):
                            if i != 2: newdata[i] = id[1][i]
                            elif id[1][2] == 0: newdata[i] = 'Male'
                            elif id[1][2] == 1: newdata[i] = 'Female'
                        print(Fore.GREEN + Style.BRIGHT + id[0] + Style.RESET_ALL + ' | ' + ' | '.join((str(x) for x in newdata)))
                else: Color.blue('No users to list')

            #list all data for attributes
            else:
                if len(attribute) != 0:
                    attribute = list(itertools.chain.from_iterable(x[1].tolist() for x in attribute))
                    Color.green('All user data in ' + sorttype + ' order by ' + attrstr + ':')
                    print(' | '.join(template))
                    for id in attribute:
                        data = main.book.usersearch(id)
                        newdata = DyArray(7, capacity=7)
                        for i in range(7):
                            if i != 2: newdata[i] = data[i]
                            elif data[2] == 0: newdata[i] = 'Male'
                            elif data[2] == 1: newdata[i] = 'Female'
                        string = id
                        for i in range(7):
                            if attrstring.upper() == template2[i+1].upper(): string += ' | ' + Fore.GREEN + Style.BRIGHT + str(data[i]) + Style.RESET_ALL
                            else: string += ' | ' + str(data[i])
                        print(string)
                else: Color.blue('No users to list')

        def attrlist(data, attribute, sorttype):
            if len(data) != 0:
                template2 = ('Username', 'First Name', 'Last Name', 'Sex', 'Phone Number', 'Email Address', 'Birthday', 'Date Added')
                Color.green('Users in ' + sorttype + ' order by ' + attribute + ':')
                for i in template2:
                    if attribute.upper() == i.upper(): print('Username | ' + Fore.GREEN + Style.BRIGHT + i + Style.RESET_ALL)
                for i in data:
                    if i[1] != None:
                        for x in i[1]:
                            if attribute.upper() == 'SEX':
                                if i[0] == 0: print(str(x[0]) + ' | ' + 'Male')
                                else: print(str(x[0]) + ' | ' + 'Female')
                            else: print(str(x[0]) + ' | ' + str(i[0]))
            else: Color.blue('No users to list')

        def userlist(data, sorttype):
            if len(data) != 0:
                Color.green('Users in ' + sorttype + ' order by username:')
                for i in data: print(i[0])
            else: Color.blue('No users to list')

        if main.book:
            if commandlist[0].upper() == 'LISTALL':
                if len(commandlist) >= 3:
                    command = commandlist[1].upper() + ' ' + commandlist[2].upper()

                    #LISTALL BY USERNAME (-reverse)
                    if command == 'BY USERNAME':
                        if commandlist[-1] == '-reverse': listall(main.book.listbyusername(True, True), sorttype='reverse sorted')
                        else: listall(main.book.listbyusername(True, False), sorttype='sorted')

                    #LISTALL BY ATTRIsBUTE <attribute> (-reverse)
                    elif command == 'BY ATTRIBUTE':
                        if len(commandlist) > 3:
                            if commandlist[-1] == '-reverse': attrstr, reverse = ' '.join(commandlist[3:-1]).lower(), True
                            else: attrstr, reverse = ' '.join(commandlist[3:]).lower(), False
                            if attrstr in attrset and attrstr != 'username':
                                listall(attribute=main.book.listbyattribute(attrstr, reverse), attrstring=attrstr, sorttype=('reverse sorted' if reverse else 'sorted'))
                            else: Color.red('Invalid command: Attribute not valid')
                        else: Color.red('Invalid command: Attribute not specified')
                    else: Color.red("Invalid command: 'BY USERNAME' or 'BY ATTRIBUTE' not specified")

                #LISTALL
                else: listall(main.book.listbyusername(False), sorttype='recently accessed')
            else:
                if len(commandlist) >= 3:
                    command = commandlist[1].upper() + ' ' + commandlist[2].upper()

                    #LIST BY USERNAME (-reverse)
                    if command == 'BY USERNAME':
                        if commandlist[-1] == '-reverse': userlist(main.book.listbyusername(True, True), 'reverse sorted')
                        else: userlist(main.book.listbyusername(True, False), 'sorted')

                    #LIST BY ATTRIBUTE <attribute> (-reverse)
                    elif command == 'BY ATTRIBUTE':
                        if len(commandlist) > 3:
                            if commandlist[-1] == '-reverse': attrstr, reverse = ' '.join(commandlist[3:-1]).lower(), True
                            else: attrstr, reverse = ' '.join(commandlist[3:]).lower(), False
                            if attrstr in attrset and attrstr != 'username':
                                attrlist(main.book.listbyattribute(attrstr, reverse), attrstr, ('reverse sorted' if reverse else 'sorted'))
                            else: Color.red('Invalid command: Attribute not valid')
                        else: Color.red('Invalid command: Attribute not specified')
                    else: Color.red("Invalid command: 'BY USERNAME' or 'BY ATTRIBUTE' not specified")

                #LIST
                else: userlist(main.book.listbyusername(False), 'recently accessed')
        else: Color.red('No book open')

    def runcommand():
        command = input('> ')
        if command.replace(' ', ''):
            commandlist = command.split(' ')
            #classifies and run function based on first word
            if commandlist[0].upper() in refdict.keys(): refdict[commandlist[0].upper()](commandlist)
            else: Color.blue(commandlist[0] + ': Command not found')

    main.book, main.saved, main.done = None, None, False
    refdict = {'OPEN': open, 'CREATE':create, 'ADD' : add,'EDIT':edit, 'DELETE':delete, 'SEARCH':search, 'LIST':lister, 'LISTALL':lister, 'SAVE':save, 'CLOSE':close, 'EXIT':exit, 'HELP': help, 'RESET': reset, 'RENAME': rename, 'REVERT':revert, 'TODAY':today, 'BURN':burn}
    attrset = Set(['username', 'first name', 'last name', 'phone number', 'sex', 'email', 'birthday', 'date added'])
    Color.bold('Session started\nType "HELP" to list all possible commands.')
    while not main.done: runcommand()
    Color.bold('Session ended')

main()
