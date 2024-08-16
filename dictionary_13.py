# Initial dictionaries
user_ids = {
    "teraCoder": 100019,
    "pythonGuy": 182921,
    "samTheJavaMaam": 123112,
    "lyleLoop": 102931,
    "keysmithKeith": 129384
}

num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# Step 1: Create a variable called users and assign it to be a dict_keys object of all keys in user_ids
users = user_ids.keys()

# Step 2: Create a variable called lessons and assign it to be a dict_keys object of all keys in num_exercises
lessons = num_exercises.keys()

# Step 3: Print users to the console
print(users)

# Step 4: Print lessons to the console
print(lessons)
