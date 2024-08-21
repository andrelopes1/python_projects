# Provided tarot cards dictionary
tarot = { 
    1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "The Emperor", 
    5: "The Hierophant", 6: "The Lovers", 7: "The Chariot", 8: "Strength", 
    9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 
    13: "Death", 14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 
    18: "The Moon", 19: "The Sun", 20: "Judgement", 21: "The World", 22: "The Fool"
}

# Step 1: Create an empty dictionary called spread
spread = {}

# Step 2: Pop the value assigned to the key 13 out of the tarot dictionary
spread["past"] = tarot.pop(13)

# Step 3: Pop the value assigned to the key 22 out of the tarot dictionary
spread["present"] = tarot.pop(22)

# Step 4: Pop the value assigned to the key 10 out of the tarot dictionary
spread["future"] = tarot.pop(10)

# Step 5: Iterate through the items in the spread dictionary and print the required string
for key, value in spread.items():
    print(f"Your {key} is the {value} card.")
