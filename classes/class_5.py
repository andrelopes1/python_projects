class Circle:
    pi = 3.14
    
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        self.radius = diameter / 2  # Set self.radius to half of the diameter
    
    def circumference(self):
        return 2 * self.pi * self.radius  # Calculate and return the circumference

# Define three Circle objects with different diameters
medium_pizza = Circle(12)  # 12 inches across
teaching_table = Circle(36)  # 36 inches across
round_room = Circle(11460)  # 11,460 inches across

# Print out the circumferences
print(f"Medium Pizza circumference: {medium_pizza.circumference():.2f} inches")
print(f"Teaching Table circumference: {teaching_table.circumference():.2f} inches")
print(f"Round Room circumference: {round_room.circumference():.2f} inches")
