from cryptography.fernet import Fernet 

def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

def load_key():
    file =  open("key.key","rb")
    key = file.read()
    file.close()
    return key

write_key()
key = load_key()
fer =Fernet(key)
masterPassword = input("Enter the master password: ")
def view():
    with open("passwordManager.txt","r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user,password = data.split("|")
            print("username: ",user," password: ",fer.decrypt(password.encode()),"\n")

def add():
    username = input("Enter your new username: ")
    password = input("Enter the password for the corresponding password: ")

    with open("passwordManager.txt","a") as f:
        f.write(username+"|"+fer.encrypt(password.encode()).decode()+"\n")
    
     


while True:
    mode = input("Would you like to add a new password or view existing ones(view,add),or type q to quit: ").lower()

    if mode=="q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid input")


print("Exiting the passwordManager")
