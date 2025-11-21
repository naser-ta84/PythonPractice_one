#Needed variables
from getpass import getpass
from operator import index

rate = 9
length = 8
advantages =[]
disadvantages =[]

print("Welcome tp our checking system")

#Checking null inputs
while True:
    username = input("Please enter your username: ")
    if username == "":
        print("⚠️ Username cannot be empty. Please try again.")
    else:
        break

while True:

    #You should run this app in terminal since pycharm has problem with getpass
    password = getpass("Please enter your password: ")
    if password == "":
        print("⚠️ Password cannot be empty. Please try again.")
    else:
        break

while True:
    yearOfBirth = input("Please enter your year of birth: ")
    if yearOfBirth == "":
        print("⚠️ Year of birth cannot be empty. Please try again.")
    else:
        break

#Showing inputs
print("Username : ", username)
print("Password : ", '*' * (len(password)))

#Start checking
print("✅ Filter checks:")

# First Condition : Checking password length
FirstConditionOutput = ""
if len(password) < length:
    FirstConditionOutput += "❌ Password is shorter than 8 characters. "
    disadvantages.append(FirstConditionOutput)
    print(FirstConditionOutput)
    rate = rate - 1
else:
    FirstConditionOutput+= "✅ Password length is sufficient. "
    advantages.append(FirstConditionOutput)
    print(FirstConditionOutput)

#Second Condition: Password should include at least one letter

SecondConditionOutput = ""
def letter_checking(input_string):
    for ch in input_string:
        if 'a' <= ch.lower() <= 'z':
            return True
    return False
if letter_checking(password):
    SecondConditionOutput +="✅ Contains at least one English letter"
    advantages.append(SecondConditionOutput)
    print(SecondConditionOutput)
else:
    SecondConditionOutput += "❌ Password does not contain any English letters. "
    disadvantages.append(SecondConditionOutput)
    print(SecondConditionOutput)
    rate = rate - 1

#Third Condition: Password should include at least special charactor ($,@,!)
ThirdConditionOutput = ""
if "@" in password or "$" in password or "!" in password:
    ThirdConditionOutput += "✅ Contains at least one special character. "
    advantages.append(ThirdConditionOutput)
    print(ThirdConditionOutput)
else:
    ThirdConditionOutput += "❌ Password does not contain any special characters. "
    disadvantages.append(ThirdConditionOutput)
    print(ThirdConditionOutput)
    rate = rate - 1

#Forth Condition: Password should include at least one uppercase letter
FourthConditionOutput = ""
def letter_checking_uppercase(input_string):
    for ch in input_string:
        if 'A' <= ch <= 'Z':
            return True

    return False

if letter_checking_uppercase(password):
    FourthConditionOutput+= "✅ Contains at least one uppercase letter. "
    advantages.append(FourthConditionOutput)
    print(FourthConditionOutput)
else:
    FourthConditionOutput += "❌ Password does not contain any uppercase letters."
    disadvantages.append(FourthConditionOutput)
    print(FourthConditionOutput)
    rate = rate - 1

#Fifth Condition: Username and password should not be same
FifthConditionOutput = ""
if username == password:
    FifthConditionOutput += "❌ Password is identical to the username. "
    disadvantages.append(FifthConditionOutput)
    print(FifthConditionOutput)
    rate = rate - 1

else:
    FifthConditionOutput += "✅ Password is not identical to the username. "
    advantages.append(FifthConditionOutput)
    print(FifthConditionOutput)

#Sixth Condition : Password should not be the swapcase version of username
SixthConditionOutput = ""
if password.swapcase() == username:
    SixthConditionOutput += "❌ Password is the swapcase version of the username. "
    disadvantages.append(SixthConditionOutput)
    print(SixthConditionOutput)
    rate = rate - 1

else:
    SixthConditionOutput += "✅ Password is not the swapcase version of the username. "
    advantages.append(SixthConditionOutput)
    print(SixthConditionOutput)

#Seventh Condition : Password should not be a special-charactor version of the username
SeventhConditionOutput = ""

tmp =""
for char in password:
    if char == "@":
        tmp = tmp + "a"
    elif char == "$":
        tmp = tmp + "s"
    elif char == "!":
        tmp = tmp + "i"
    elif char == "0":
        tmp = tmp + "o"
    else:
        tmp = tmp + char
if tmp == username:
    SeventhConditionOutput += "❌ Is a special-character version of the username. "
    disadvantages.append(SeventhConditionOutput)
    print(SeventhConditionOutput)
    rate =rate - 1

else:
    SeventhConditionOutput += "✅ Password is not a special-character version of the username. "
    advantages.append(SeventhConditionOutput)
    print(SeventhConditionOutput)

#Eighth Condition : Password should not be a common password
EighthConditionOutput = ""

def checkcommonpassword(input_string):
    commonPasswords = ["123456", "12345678", "12345", "111111", "123456789",
                       "qwerty", "asdfgh", "zxcvbnm", "password", "admin",
                       "P@s$w0rd"]
    for commonPassword in commonPasswords:
        if input_string == commonPassword:
            return True
    return False
if checkcommonpassword(password):
    EighthConditionOutput += "❌ Password is one of the most common passwords. "
    disadvantages.append(EighthConditionOutput)
    print(EighthConditionOutput)
    rate = rate - 1

else:
    EighthConditionOutput += "✅ Password is not one of the most common passwords. "
    advantages.append(EighthConditionOutput)
    print(EighthConditionOutput)

#Ninth condition : Password should not include user year of birth
NinthConditionOutput = ""
if yearOfBirth in password:
    NinthConditionOutput += "❌ Password has year of birth. "
    disadvantages.append(NinthConditionOutput)
    print(NinthConditionOutput)
    rate = rate - 1

else:
    NinthConditionOutput += "✅ Password dose not have year of birth. "
    advantages.append(NinthConditionOutput)
    print(NinthConditionOutput)

#Result

#Showing rate
print(f"🔐 Final Score: {rate} out of 9  ")

#Showing level
securityLevel = ""
tip = ""

if rate == 9 :
    securityLevel += "Strong"
    tip += "🎉 Your password is highly secure and passed all checks!"

elif  5 < rate < 9 :
    securityLevel += "Medium"
    tip +="Your password is fairly secure, but try to add more variety — e.g., more symbols or longer length."

elif 3 < rate < 6 :
    securityLevel += "Weak"
    tip += "Your password is weak. Try adding uppercase letters, special characters,or more length."

elif 0 <= rate < 4 :
    securityLevel += "Very Weak"
    tip += "Your password is too simple and easy to guess. Avoid using common words or personal info like your name or birth year."

print(f"🔒 Security Level: {securityLevel} ")

print(f"📌 Tip: {tip}")
