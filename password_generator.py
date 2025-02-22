# Imports
import random

# Characters being used
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZaqbcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*?"

# Password Generator Function
while 1:
    pass_len = int(input("How long would you like your passwords to be? : "))
    pass_num = int(input("How many passwords would you like to generate? : "))
    
    if pass_len <= 0:
        print("Invalid password length entered.")
    else:
        True
    
    for x in range(0, pass_num):
        password = ""    
    
        for x in range(0, pass_len):
            password_chars = random.choice(chars)
            password = password + password_chars
        
        print("Here is your password! : ", password) 