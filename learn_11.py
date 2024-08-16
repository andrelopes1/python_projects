import json  # Step 1: Import the json module

# Correct data_payload as provided in your instructions
data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]

# Step 2: Open the file data.json in write-mode
with open('data.json', 'w') as data_json:
    # Step 3: Write the list of dictionaries to the JSON file
    json.dump(data_payload, data_json)
