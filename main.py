creds = {"SURYAR":1003,"PAVANK":2107,"MADHU":3009}

def login(username,password):
    if username in creds and creds[username] == password:
        return True
    return False

def main():
    print("Login to the system")
    username = input("Enter the username: ")
    password = int(input("Enter the passcode: "))
    print(login(username,password))


main()