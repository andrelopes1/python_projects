import json  # Step 1: Import the json module

# Step 2: Open the file message.json
with open('message.json') as message_json:
    # Step 3: Parse the JSON file into a Python dictionary
    message = json.load(message_json)
    
    # Step 4: Print the value associated with the 'text' key
    print(message['text'])
