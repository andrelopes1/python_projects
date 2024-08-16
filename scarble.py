# Provided lists of letters and their corresponding point values
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 
          4, 8, 4, 10]

# Step 1: Create the dictionary letter_to_points
letter_to_points = {letter: point for letter, point in zip(letters, points)}

# Add the blank tile with a point value of 0
letter_to_points[" "] = 0

# Step 2: Define the score_word function
def score_word(word):
    # Initialize the point total to 0
    point_total = 0
    # Loop through each letter in the word
    for letter in word:
        # Add the point value of the letter to point_total
        point_total += letter_to_points.get(letter.upper(), 0)  # .get() handles missing letters
    return point_total

# Test the function with the word "BROWNIE"
brownie_points = score_word("BROWNIE")
print(f"BROWNIE points: {brownie_points}")  # Should print 15

# Step 3: Create the player_to_words dictionary
player_to_words = {
    "player1": ["BLUE", "TENNIS", "EXIT"],
    "wordNerd": ["EARTH", "EYES", "MACHINE"],
    "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
    "Prof Reader": ["ZAP", "COMA", "PERIOD"]
}

# Initialize the player_to_points dictionary
player_to_points = {}

# Loop through each player and their words
for player, words in player_to_words.items():
    # Initialize player_points for the current player
    player_points = 0
    # Loop through each word the player has played
    for word in words:
        # Add the score of the word to player_points
        player_points += score_word(word)
    # Update the player_to_points dictionary
    player_to_points[player] = player_points

# Print the player_to_points dictionary to see the standings
print(player_to_points)  # This will show the total points for each player
