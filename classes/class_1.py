class Circle:
    pi = 3.14
    
    def area(self, radius):
        return self.pi * (radius ** 2)

# Create an instance of Circle
circle = Circle()

# Calculate areas
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

print("Pizza area:", pizza_area)
print("Teaching table area:", teaching_table_area)
print("Round Room auditorium area:", round_room_area)
