import random
import time

# Implement the username rules - u1 and u2 are the first and last names, respectively
def get_username(u1,u2):
    u1 = u1[0]
    u2 = u2[-3:]
    user = u1 + u2
    return user

# Helper function for the password generator function
# There are a few ways to do this - you could use the ASCII codes alternatively
def get_random_letter():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    length = len(alphabet)
    randomIndex = random.randint(0,length-1)

    letter = alphabet[randomIndex]

    # The code below randomly selects if the letter is capital or not (50/50)
    capsSelector = random.randint(0,1)

    if capsSelector == 0:
        return letter
    else:
        return letter.upper()

# Another helper function for the password generator function
def get_random_symbol():
    
    # Some symbols (you could add more)
    symbols = "/*?£$()@<>^"

    length = len(symbols)

    randomIndex = random.randint(0,length-1)

    return symbols[randomIndex]

# Check to see if the character can be added
def check_char(pw,i,char):

    # If this is the first character, you need to add it
    if i == 0:
        pw += char
        return (True,pw)

    # For additional characters, check these are different to the previous
    # If they are not, then the while loop needs to loop again
    elif char != pw[i-1]:
        pw += char
        return (True,pw)

    else:
        return(False,"")
    

# Implement the password rules
def get_password():


    # Initialise an empty password (for now)
    pw = ""

    # Loop as many times as the generated length
    for i in range(10):

        # Random choice between letters and numbers/symbols
        likelihood = random.randint(1,3)

        # Letters are twice as likely as numbers or symbols
        if likelihood == 2 or likelihood == 3:

            """ Each generated character has the code below - it keeps generating
            a new character until the check_char function returns True (meaning
            it was different to the previous character)."""
            while True:
                char = get_random_letter()

                check = check_char(pw,i,char)

                if check[0] == True:
                    pw = check[1]
                    break

        # This is when a letter has NOT been selected - so either a number or a symbol
        elif likelihood == 1:

            # Random choice for either numbers or symbols. They are as likely to occur as each other.
            # To choose, perform another random generation.
            likelihood = random.randint(1,2)

            # For a symbol...
            if likelihood == 1:

                while True:
                    char = get_random_symbol()

                    check = check_char(pw,i,char)

                    if check[0] == True:
                        pw = check[1]
                        break

            # For a number...
            elif likelihood == 2:

                # For numbers it's a simple generation so doesn't benefit from a helper function

                while True:
                    char = str(random.randint(0,9))

                    check = check_char(pw,i,char)

                    if check[0] == True:
                        pw = check[1]
                        break                    

    # When the for loop ends, the password has been created
    return pw

# Main program
print("Welcome")
firstName = input("Please enter your first name: ")
lastName = input("Please enter your last name: ")

# Gives an illusion of thinking time
time.sleep(2)

# Holds and then prints the results of the two key functions
username = get_username(firstName, lastName)
password = get_password()

print("Your username is: ",username)
print("Your password is: ",password)
