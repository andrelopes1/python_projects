# Step 1: Create a variable called total_exercises and set it equal to 0
total_exercises = 0

# The dictionary with the number of exercises per topic
num_exercises = {
    "functions": 10,
    "syntax": 13,
    "control flow": 15,
    "loops": 22,
    "lists": 19,
    "classes": 18,
    "dictionaries": 18
}

# Step 2: Iterate through the values in the num_exercises dictionary
# and add each value to the total_exercises variable
for exercises in num_exercises.values():
    total_exercises += exercises

# Step 3: Print the total_exercises variable to the console
print(total_exercises)
