import csv  # Step 1: Import the csv module

# Step 2: Open the file cool_csv.csv
with open('cool_csv.csv') as cool_csv_file:
    # Step 3: Read the contents into cool_csv_dict using csv.DictReader
    cool_csv_dict = csv.DictReader(cool_csv_file)

    # Step 4: Print out each row's "Cool Fact"
    for row in cool_csv_dict:
        print(row["Cool Fact"])
