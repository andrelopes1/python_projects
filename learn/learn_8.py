import csv  # Step 1: Import the csv module

# Step 2: Open the file books.csv
with open('books.csv') as books_csv:
    # Step 3: Create a DictReader with @ as delimiter
    books_reader = csv.DictReader(books_csv, delimiter='@')
    
    # Step 4: Create a list to hold ISBN numbers
    isbn_list = []
    
    # Iterate through books_reader to get each ISBN
    for row in books_reader:
        isbn_list.append(row['ISBN'])

# Optionally, you could print isbn_list to verify the result
print(isbn_list)
