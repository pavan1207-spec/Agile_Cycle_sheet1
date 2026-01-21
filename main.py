CREDS = {"ADMIN":1234,"SURYA":1003,"PAVAN":1207}

def login(username,password):
    if username in CREDS and CREDS[username] == password:
        return True
    return False

def main():
    print("Login to the system")
    username = input("Enter the username: ")
    password = int(input("Enter the passcode: "))
    print(login(username,password))
main()