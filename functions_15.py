def common_letters(string_one, string_two):
    # Convert strings to sets to get unique letters
    set_one = set(string_one)
    set_two = set(string_two)
    
    # Find the common letters using intersection
    common = set_one.intersection(set_two)
    
    # Convert the set to a list
    return list(common)

# Example usage
print(common_letters("banana", "cream"))  # Output will be ['a']
