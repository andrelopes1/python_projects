# Initial setup
available_items = {
    "health potion": 10,
    "cake of the cure": 5,
    "green elixir": 20,
    "strength sandwich": 25,
    "stamina grains": 15,
    "power stew": 30
}
health_points = 20

# Step 1: Add "stamina grains" value to health_points and remove the item
health_points += available_items.pop("stamina grains", 0)

# Step 2: Add "power stew" value to health_points and remove the item
health_points += available_items.pop("power stew", 0)

# Step 3: Add "mystic bread" value to health_points and remove the item
health_points += available_items.pop("mystic bread", 0)

# Step 4: Print the updated available_items and health_points
print(available_items, health_points)
