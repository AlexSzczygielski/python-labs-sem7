#Task 3 - implement a combination lock - asks for code and checks (few)
import maskpass

def set_pswd():
    pswd = input("Provide password: ")
    try:
        if(input("Verify a password: ") == pswd):
            print("Password set successfully!")
        else:
            raise Exception('Verification failed - repeated password was not identical')
    except Exception as e:
        print(f"Error: {e}")
        return ""
    return pswd

def verify(usr_input,pswd):
    try:
        if(usr_input == pswd):
            print("Logged in!")
        else:
            raise Exception('Wrong password')
    
    except Exception as e:
        print("Error: ",e)

if __name__ == "__main__":
    pswd = set_pswd()

    if(pswd!= ""):
        usr_input = input("Please provide a password to enter: ")
        verify(usr_input,pswd)
    
            