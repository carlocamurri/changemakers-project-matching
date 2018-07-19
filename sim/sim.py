from src.matcher import Matcher
from src.entities.student import Student
from src.entities.project import Project

users = {
    "16077909" : "Password1",
    "16977910" : "Password2"
}

def intro():
    print "\n- - - UCL CHANGEMAKERS - - -"
    print "- - Simulation of workflow - -"
    print "------------------------------\n"

def insert_credential():
    username = raw_input('User ID: ')
    password = raw_input("Password: ")
    validate_account(username, password)

def login():
    username = ""
    password = ""
    print "Enter login credentials."
    insert_credential()
    print username

def validate_account(username, password): 
    if username not in users:
        print "Unregistred Account!\n"
        username = raw_input("Re-enter username: ")
        validate_account(username, password)
    else:    
        if users[username] == password:
            print "\nSuccessful login!"
        else: 
            print "Invalid password\n"
            password = raw_input("Re-enter password: ")
            validate_account(username, password)

# def load_data():


intro()
login()
# load_data()

