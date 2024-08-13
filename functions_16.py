def username_generator(first_name, last_name):
    # Take the first three letters of the first name or the whole name if it's shorter
    first_part = first_name[:3]
    
    # Take the first four letters of the last name or the whole name if it's shorter
    last_part = last_name[:4]
    
    # Combine both parts to form the username
    user_name = first_part + last_part
    
    return user_name

# Example usage:
print(username_generator("Abe", "Simpson"))  # Output will be 'AbeSimp'
print(username_generator("Al", "Smith"))  # Output will be 'AlSmit'


def password_generator(user_name):
    # Initialize an empty string for the password
    password = ""
    
    # Loop through the indices of user_name
    for i in range(len(user_name)):
        # Add the letter at the previous index to the password
        password += user_name[i - 1]
    
    return password

# Example usage:
user_name = username_generator("Abe", "Simpson")
print(password_generator(user_name))  # Output will be 'pAbeSim'
