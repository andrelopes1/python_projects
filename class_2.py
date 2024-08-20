class Circle:
    pi = 3.14
    
    # Add constructor here
    def __init__(self, diameter):
        self.diameter = diameter
        print(f"New circle with diameter: {diameter}")

# Create an instance with diameter 36
teaching_table = Circle(36)
