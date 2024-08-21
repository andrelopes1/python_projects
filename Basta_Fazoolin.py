class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time
    
    def __repr__(self):
        return f"{self.name} menu available from {self.start_time} to {self.end_time}"
    
    def calculate_bill(self, purchased_items):
        total = sum(self.items[item] for item in purchased_items)
        return total

class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return self.address
    
    def available_menus(self, time):
        available = [menu for menu in self.menus if menu.start_time <= time <= menu.end_time]
        return available

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

# Create Menus
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00,
    'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
brunch = Menu("Brunch", brunch_items, "11am", "4pm")

early_bird_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}
early_bird = Menu("Early Bird", early_bird_items, "3pm", "6pm")

dinner_items = {
    'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00,
    'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50,
    'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00
}
dinner = Menu("Dinner", dinner_items, "5pm", "11pm")

kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00,
    'apple juice': 3.00
}
kids = Menu("Kids", kids_items, "11am", "9pm")

# Create Franchises
menus = [brunch, early_bird, dinner, kids]
flagship_store = Franchise("1232 West End Road", menus)
new_installment = Franchise("12 East Mulberry Street", menus)

# Test
print(flagship_store)  # Expected: "1232 West End Road"
print(new_installment.available_menus("12pm"))  # Expected: [brunch, kids]
print(flagship_store.available_menus("5pm"))  # Expected: [early_bird, dinner, kids]

# Create Arepa Menu and Franchise
arepas_items = {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50,
    'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepas_menu = Menu("Arepas", arepas_items, "10am", "8pm")

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

# Create Business
arepa_business = Business("Take a' Arepa", [arepas_place])
