import csv
import json

# Step 1: Reading In The Passwords
compromised_users = []

# Open the passwords.csv file and read the data
with open('passwords.csv') as password_file:
    password_csv = csv.DictReader(password_file)
    
    # Iterate through each row in the CSV
    for password_row in password_csv:
        # Append each username to the compromised_users list
        compromised_users.append(password_row['Username'])

# Step 2: Write compromised usernames to a text file
with open('compromised_users.txt', 'w') as compromised_user_file:
    for user in compromised_users:
        compromised_user_file.write(user + '\n')

# Step 3: Notifying the Boss
# Create a dictionary with the boss's message
boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
}

# Write the boss_message_dict to a JSON file
with open('boss_message.json', 'w') as boss_message:
    json.dump(boss_message_dict, boss_message)

# Step 4: Scrambling the Password
# Signature of Slash Null
slash_null_sig = """ 
 _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
"""

# Write the Slash Null signature to a new passwords file
with open('new_passwords.csv', 'w') as new_passwords_obj:
    new_passwords_obj.write(slash_null_sig)
