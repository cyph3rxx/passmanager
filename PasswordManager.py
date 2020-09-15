from Userx import list
from usrentry import blah
from passdecryptor import passdecryptor
print("Are you opening this for the first time?")
useranswer=input()
if useranswer=="yes" or useranswer=="y":
    blah()
elif useranswer=="no" or useranswer=="n":
    f=open("userinformation.py")
    userkey=f.read()
    print("Enter the password")
    userauth=input()
    if userauth==passdecryptor(userkey):
        print("Here are your encrypted passwords: \n")
        list()
    else:
        print("Wrong password!!")
else:
    print("Wrong input!!")