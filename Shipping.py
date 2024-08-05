
# Ground Shipping
#Write any number to check the total price for ground shipping and drone shipping
weight = 1.5

Ground_Shipping_Premium = 125

if weight <= 2:
  ground_cost = 1.50 * weight + 20.00
elif weight <= 6:
  ground_cost = 3.00 * weight + 20.00
elif weight <= 10:
  ground_cost = 4.00 * weight + 20.00
else:
  ground_cost = 4.25 * weight + 20.00


print("The gound shipping cost for a package with " + str(weight) + " kg is " + str(ground_cost) + "€")

# Drone Shipping

if weight <= 2:
  drone_cost = 4.50 * weight
elif weight <= 6:
  drone_cost = 9.00 * weight
elif weight <= 10:
  drone_cost = 12.00 * weight
else:
  drone_cost = 14.25 * weight

print("The drone shipping cost for a package with " + str(weight) + " kg is " + str(drone_cost) + "€")