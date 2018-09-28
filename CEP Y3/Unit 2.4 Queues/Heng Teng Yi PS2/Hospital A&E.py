from PriorityQ import *

class color:
   GREEN = '\033[92m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

def HospitalAandE():
    """Allows hospitals to quickly queue patients based on their condition and timing

Features:
1) Priority Queue
Uses the PriorityQueue class to enqueue or dequeue patients, heap sorting firstly on
the severity of their condition, followed by when they were entered into the queue

2) Coloured Interface
Illustrates the input lines in the program as \033[91mred\033[0m, and important actions as \033[92mgreen\033[0m
Allows user to efficiently differentiate between important actions, so they can
read and utilize the program more quickly, as well as double-check inputs more easily

3) Uncrashable
Any wrong inputs cannot crash the system, ensuring mistakes don't end the program and
prematurely erase the data of patients in the system
"""
    def mainmenu():
        def mmchecker():
            try:
                reply = int(input(color.RED + "\nEnter option [1-4]: " + color.END))
                if 0 < reply < 5:
                    optionmap[reply]()
                else:
                    print("\nThe following option is not supported. Please enter another one.")
                    mmchecker()
            except ValueError:
                print("\nThe following option is not supported. Please enter another one.")
                mmchecker()

        print(color.BOLD + "\nMain Menu Options:\n"
            "\n1) Schedule patient\n"
            "\n2) Treat next patient\n"
            "\n3) Treat all patients\n"
            "\n4) Exit program" + color.END)

        mmchecker()

    def option1():
        def op1checker():
            try:
                reply = int(input(color.RED + "\nEnter patient's condition [1-3]: " + color.END))
                if 0 < reply < 4:
                    print(color.GREEN + "\n" + name + " is added to the " + conditionmap[reply] + " list." + color.END)
                    patientqueue.push((name, reply))
                    mainmenu()
                else:
                    print("\nThis option is not supported. Please choose another one.")
                    op1checker()
            except ValueError:
                print("\nThis option is not supported. Please choose another one.")
                op1checker()

        name = input(color.RED + "\nEnter patient's name: " + color.END)

        print(color.BOLD + "\nPatient's condition:\n"
        "\n1) Critical\n"
        "\n2) Serious\n"
        "\n3) Fair \n" + color.END)

        op1checker()

    def option2():
        if not patientqueue.isEmpty():
            patient = patientqueue.pop()
            print(color.GREEN + "\n" + str(patient[1]) + "("+ conditionmap[patient[0]] + ")" + " is being treated." + color.END)
        else:
            print(color.GREEN + "\nThere are no patients left to treat." + color.END)

        mainmenu()

    def option3():
        while not patientqueue.isEmpty():
            patient = patientqueue.pop()
            print(color.GREEN + "\n" + str(patient[1]) + "("+ conditionmap[patient[0]] + ")" + " is being treated." + color.END)

        print(color.GREEN + "\nThere are no patients left to treat." + color.END)
        mainmenu()

    def option4():
        print("Program closed.")
        exit()

    patientqueue = PriorityQueue()
    print(color.UNDERLINE + "Welcome to the Binner Hospital A&E program." + color.END)
    optionmap = {1:option1, 2:option2, 3:option3, 4:option4}
    conditionmap = {1: "Critical", 2: "Serious", 3: "Fair"}

    mainmenu()

HospitalAandE()
