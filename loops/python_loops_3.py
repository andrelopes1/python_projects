sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0


for location in sales_data:
    for scoops in location:  # Use a different variable name here
        scoops_sold += scoops  # Add each scoop value to scoops_sold

print("Total scoops sold:", scoops_sold)
