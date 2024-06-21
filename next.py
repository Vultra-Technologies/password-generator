import string
import random
import os

print("How long do you want your password to be? \n \n 5 characters: Something not so important, like an unpaid newsletter acount. \n 10 letters: Something more important, like a Twitter (Now named X) account. \n 15 characters: A very important account, like an account containing payment information. \n Advanced - Other Length: Input your own number.")

length = int(input("Enter your length:"))

print("Type the corresponding number for Characters. \n You can keep on adding numbers until you press 4 (Finish). ")

print('''Type the corresponding number for Character(s). : 
         1. Digits
         2. Letters
         3. Special characters
         4. Finish''')
 
characterList = ""
 
# Getting character set for password
while(True):
    choice = int(input("Pick a number "))
    if(choice == 1):
         
        # Adding letters to possible characters
        characterList += string.ascii_letters
    elif(choice == 2):
         
        # Adding digits to possible characters
        characterList += string.digits
    elif(choice == 3):
         
        # Adding special characters to possible
        # characters
        characterList += string.punctuation
    elif(choice == 4):
        break
    else:
        print("Please pick a valid option!")
 
password = []
 
for i in range(length):
   
    # Picking a random character from our 
    # character list
    randomchar = random.choice(characterList)
     
    # appending a random character to password
    password.append(randomchar)
 
# printing password as a string
print("The random password is " + "".join(password))

savepwd = input("Do you want to save your password? Yes or No:")
if (savepwd == 'Yes') :
    pwdname = input("What do you want to call the file? (Do not include file extension, eg. '.txt'.)")
    with open(pwdname + ".txt", "w") as file:
        file.write("".join(password))
    print("Saved succesfully to Program Installation Directory. You can find where that is by checking 'Apps and Programs' in System Settings.")
elif(savepwd == 'No'):
    quit
