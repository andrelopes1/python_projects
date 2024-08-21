# Provided string of authors
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

# Split the string by commas to create a list of full names
author_names = authors.split(",")

# Create a new list to hold only the last names
author_last_names = []

# Iterate through the list of full names
for name in author_names:
    # Split each full name into first and last name
    last_name = name.split(" ")[-1]  # Take the last part as the last name
    author_last_names.append(last_name)

# Print the lists
print(author_names)
print(author_last_names)
