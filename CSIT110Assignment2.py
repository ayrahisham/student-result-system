# Assignment 2
# subject code : CSIT110
# name : Nur Suhaira
# student number : 5841549
# date : 14/10/2018

# Develop a Student's result system to
#1. Display modules average scores
#2. Display modules top scorer
# All modules results are stored in the data.csv file. (See Appendix)

systemTitle = "Welcome to Students' Result System"
def menu  () :
    print ("1. Display modules average score")
    print ("2. Display modules top scorer")
    print ("0. Exit")

menu1Title = "Display Modules Average Scores"
menu2Title = "Display Modules Top Scorer"
mod110 = "CSIT110"
mod121 = "CSIT121"
mod135 = "CSIT135"
mod142 = "CSIT142"
max110= 0
max121 = 0
max135 = 0
max142 = 0
mod = "Module"
fname = "First Name"
lname = "Last Name"

def display_modules_average_scores (filepath) :
    sum110= 0
    sum121 = 0
    sum135 = 0
    sum142 = 0
    with open(filePath) as csvfile:
                reader = csv.DictReader(csvfile)
                
                # Iterate 3 times since there are 3 data in file
                for i in range (0, 3) :
                    for row in reader:
                        
                        # Extract values from file columns into variables
                        filemod110= int(row[mod110])
                        filemod121 = int(row[mod121])
                        filemod135 = int(row[mod135])
                        filemod142 = int(row[mod142])
                        
                        # Store every column value into sum variables
                        sum110 += filemod110
                        sum121 += filemod121
                        sum135 += filemod135
                        sum142 += filemod142
                        
    # Calculate average from sum variables
    avg110 = round (sum110 / 3, 2)
    avg121 = round (sum121 / 3, 2)
    avg135 = round (sum135 / 3, 2)
    avg142 = round (sum142 / 3, 2)

    # Display to user 
    print ("{0:^8} | {1:^8} | {2:^8} | {3:^8}".format (mod110, mod121, mod135, mod142))
    print ("{0:^8} | {1:^8} | {2:^8} | {3:^8}".format (avg110, avg121, avg135, avg142))
    print ("=" * 40)

def display_modules_top_scorer(filepath) :
    list110 = []
    list121 = []
    list135 = []
    list142 = []
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
                
        # Display to user 
        print ("{0:<8} | {1:>8} | {2:<8}".format (mod, fname, lname))
        # Iterate 3 times since there are 3 data in file
        for i in range (0, 3) :
            for row in reader:
                
                # Extract values from file columns into variables
                # Compare to check the top score and store in max
                # Extract the first and last name of top scorer
                list110.append (int(row[mod110]))
                list121.append (int(row[mod121]))
                list135.append (int(row[mod135]))
                list142.append (int(row[mod142]))

        # Store the max marks in variables
        max110 = max (list110)
        max121 = max (list121)
        max135 = max (list135)
        max142 = max (list142)

    # Use the max variables to check which student achieve that mark
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for i in range (0, 3) :
            for row in reader :
                if (max110 == int(row[mod110])) :
                    fname110 = (row ['first_name'])
                    lname110 = (row ['last_name'])
                    print ("{0:<8} | {1:>8} | {2:<8}".format (mod110, fname110, lname110))
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for i in range (0, 3) :
            for row in reader :
                if (max121 == int(row[mod121])) :
                    fname121 = (row ['first_name'])
                    lname121 = (row ['last_name'])
                    print ("{0:<8} | {1:>8} | {2:<8}".format (mod121, fname121, lname121))
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for i in range (0, 3) :
            for row in reader :
                if (max135 == int(row[mod135])) :
                    fname135 = (row ['first_name'])
                    lname135 = (row ['last_name'])
                    print ("{0:<8} | {1:>8} | {2:<8}".format (mod135, fname135, lname135))
    with open(filePath) as csvfile:
        reader = csv.DictReader(csvfile)
        for i in range (0, 3) :
            for row in reader :
                if (max142 == int(row[mod142])) :
                    fname142 = (row ['first_name'])
                    lname142 = (row ['last_name'])
                    print ("{0:<8} | {1:>8} | {2:<8}".format (mod142, fname142, lname142))
                
        print ("=" * 40)

def main (filepath) :

    print ("=" * 40)
    print (systemTitle)
    print ("=" * 40)

    ok = True
    while (ok == True) :
        print ()
        menu ()
        try :
            choice = int (input ("Enter choice: "))

            # Choice 1: Display modules average scores
            if (choice == 1) :
                print ("=" * 40)
                print (menu1Title)
                print ("=" * 40)
                print ()
                display_modules_average_scores (filePath)
                    
            # Choice 2 : Display modules top scorer
            elif (choice == 2) :
                print ("=" * 40)
                print (menu2Title)
                print ("=" * 40)
                print ()
                display_modules_top_scorer(filePath) 
                
            # Choice 0: Quit
            elif (choice == 0) :
                ok = False
                print ("=" * 40)
                print ("Thank you for using Students' Result System")
                print ("=" * 40)
                
            # Other choices
            else :
                print ("Invalid choice, please enter again")
            
        except :
            print ("Choice is not numeric, please try again")
        print ()

        

import csv
filePath = "data.csv"

main (filePath)
