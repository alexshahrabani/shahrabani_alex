name = input("What is your name?")

lastname = input("What is your last name?")

title = input("What is your school title?")


school = input("What is the name of your school?")

year = input("What years at school are you here for?")

subject = input("What is your favorite school subject?")
           
print("*" * 34)

def printLine(left, right): #Prints each individual line in the card
    print("* {:^15}{:^15} *".format(left, right))

printLine(school, year)
printLine(name, lastname)
printLine(title, subject)
print("*" * 34)


                 
            
             

