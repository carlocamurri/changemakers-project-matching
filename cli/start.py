users = {
    "carlocamurri" : "bonfire",
    "francescobenintende" : "UCLove<3",
    "miquel" : "crossfit"
}

def intro():
    print "\n- - - UCL CHANGEMAKERS - - -"
    print "Simulation of workflow"
    print "------------------------------\n"

def insert_credential():
    username = raw_input('username: ')
    password = raw_input("password: ")
    validate_account(username, password)

def login():
    username = ""
    password = ""
    print "Enter login credentials"
    insert_credential()
    print username

def validate_account(username, password): 
    if username not in users:
        print "Unregistred Account!\n"
    else:    
        if users[username] == password:
            print "\nSuccessful login"
        else: 
            print "Invalid password\n"
            password = raw_input("Re-enter password: ")
            validate_account(username, password)


intro()
login()
