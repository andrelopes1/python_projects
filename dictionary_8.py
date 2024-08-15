# Provided lists of songs and playcounts
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Step 1: Create the plays dictionary using dict comprehension
plays = {song: playcount for song, playcount in zip(songs, playcounts)}

# Step 2: Print the plays dictionary
print("Plays dictionary:", plays)

# Step 3: Add a new entry for "Purple Haze"
plays["Purple Haze"] = 1

# Step 4: Update the playcount for "Respect"
plays["Respect"] = 94

# Step 5: Create the library dictionary
library = {
    "The Best Songs": plays,
    "Sunday Feelings": {}
}

# Step 6: Print the library dictionary
print("Library dictionary:", library)
