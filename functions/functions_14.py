def letter_check(word, letter):
    for char in word:  # Iterate through each character in the word
        if char == letter:  # Check if the current character matches the letter
            return True  # Return True if the letter is found
    return False  # Return False if the loop completes without finding the letter

# Example usage
print(letter_check("banana", "a"))  # Output will be True
print(letter_check("banana", "z"))  # Output will be False

