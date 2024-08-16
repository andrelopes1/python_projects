# Dictionary with percentages of women in various occupations
pct_women_in_occupation = {
    "CEO": 28,
    "Engineering Manager": 9,
    "Pharmacist": 58,
    "Physician": 40,
    "Lawyer": 37,
    "Aerospace Engineer": 9
}

# Step 1: Use a for loop to iterate through the items of the dictionary
for occupation, percentage in pct_women_in_occupation.items():
    # Print the required string for each occupation
    print(f"Women make up {percentage} percent of {occupation}s.")
