from random import choice, randint
import datetime
print("1:MAKE YOUR OWN PASSWORD\n2:LET COMPUTER MAKE IT FOR YOU")
choose = int(input("Choose : "))
f = open("PASSWORD.txt","a")
if(choose == 1):
    purpose = input("Enter purpose : ")
    created_on = str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().year) + " at " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)
    password = input("Enter password : ")
    f.write(purpose + " : " + password + "\t" + created_on + "\n")
    f.close()
    print("Password Saved!")
elif(choose == 2):
    char = list("abcdefghijklmnopqrstuvwxyz")
    CHAR = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    num = list("1234567890")
    spl_char = list("*/?<>\:;{}[]+=-_&^%$#@!")
    length = int(input("Enter desired password length : "))
    purpose = input("Enter purpose : ")
    password = ""
    for i in range(length):
        random_choice = randint(1,4)
        if(random_choice == 1):
            password = password + choice(char)
        elif(random_choice == 2):
            password = password + choice(CHAR)
        elif(random_choice == 3):
            password = password + choice(num)
        elif(random_choice == 4):
            password = password + choice(spl_char)
    created_on = str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().year) + " at " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute)
    f.write(purpose + " : " + password + "\t" + created_on + "\n")
    f.close()
    print("Password Saved!")