import random

def generate_password(length):
    """
    Generates a password for the given length.
  
    Parameters:
    length (int): Length of the password.
  
    Returns:
    str: Password string.
  
    """
    string = ''
    for i in range(0, length):
        string += chr(random.randint(33, 126))
    return string

password_length = int(input("Enter length of the required password: "))
password = generate_password(password_length)
print("The randomly generated password is: " + password)
