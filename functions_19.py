highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# Step 2
highlighted_poems_list = highlighted_poems.split(",")

# Step 4
highlighted_poems_stripped = [poem.strip() for poem in highlighted_poems_list]

# Step 6
highlighted_poems_details = [poem.split(":") for poem in highlighted_poems_stripped]

# Step 8
titles = []
poets = []
dates = []

# Step 9
for details in highlighted_poems_details:
    titles.append(details[0])
    poets.append(details[1])
    dates.append(details[2])

# Step 10
for i in range(len(titles)):
    print("The poem {} was published by {} in {}.".format(titles[i], poets[i], dates[i]))

print(highlighted_poems)

print(highlighted_poems_list)

print(highlighted_poems_stripped)

highlighted_poems_details = []



# Create the empty list as per the previous step
highlighted_poems_details = []

# Iterate through the list and split each string at the ':' character
for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(":"))

# Now highlighted_poems_details will be a list of lists with title, author, and date
print(highlighted_poems_details)  # Optional: To check the structure
