while True:
    print("Please create your account, What's your nickname?")
    nickname = input()
    print("Now please create your password")
    passreg = input()
    print("Please repeat your password")
    password2 = input()
    if passreg != password2:
        print("Your password is not the same, please try again")
        continue    
    else:
        print("Nice, Welcome to this App")
        break

while True:
    print("Plase Login, What's your nickname?")
    nicknamelog = input()
    if nicknamelog != nickname:
        print("Your nickname doesn't exist, please try again")
        continue
    print("What's your password?")
    passlog = input()
    if passlog != passreg:
        print("Wrong password, Try again")
    else:
        print("Please come back")
    break



print('www')


