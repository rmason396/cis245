#*******************************
# Assignment10_Mason
# File operations
# Nov. 2, 2019
#*******************************
import os
def ChangeDirectory():
    print("The current directory is " + str(os.getcwd()))
    changeDir = input("Do you want to change to a new directory? 'y' or 'n'")
    if changeDir.lower() == 'y':
        path = input("Enter the path of the new directory: ")
        try:
            os.chdir(path)
        except:
            print("The directory could not be opened")

    print("The current directory is " + str(os.getcwd()))
    GetUserInfo()

def ModifyFile(fileName,contactInfo):   
    try:
        file = open(fileName, "at")
    except:
        print("The file could not be opened")
    file.write(contactInfo + "\n")
    file.seek(0)
    with open (fileName, 'rt') as file:
        for line in file:
            print(line)

def GetUserInfo():
    filename = input("Enter the file name: ")
    name = input("Enter your name: ")
    address = input("Enter your street address: ")
    phone = input("Enter your phone number: ")
    info = name + "," + address + "," + phone
    ModifyFile(filename,info)


def main():
    ChangeDirectory()

main()