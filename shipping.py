# Get user input for the weight of the package
weight = float(input("Enter the weight of the package (in pounds): "))

# Ground Shipping
# Rates and flat charge for ground shipping
if weight <= 2:
    ground_shipping_cost = weight * 1.50 + 20.00
elif weight <= 6:
    ground_shipping_cost = weight * 3.00 + 20.00
elif weight <= 10:
    ground_shipping_cost = weight * 4.00 + 20.00
else:
    ground_shipping_cost = weight * 4.75 + 20.00

print(f"Ground Shipping Cost: ${ground_shipping_cost:.2f}")

# Ground Shipping Premium
# Flat charge for ground shipping premium
ground_shipping_premium_cost = 125.00

print(f"Ground Shipping Premium Cost: ${ground_shipping_premium_cost:.2f}")

# Drone Shipping
# Rates for drone shipping
if weight <= 2:
    drone_shipping_cost = weight * 4.50
elif weight <= 6:
    drone_shipping_cost = weight * 9.00
elif weight <= 10:
    drone_shipping_cost = weight * 12.00
else:
    drone_shipping_cost = weight * 14.25

print(f"Drone Shipping Cost: ${drone_shipping_cost:.2f}")

# Determine the cheapest shipping method
if ground_shipping_cost < ground_shipping_premium_cost and ground_shipping_cost < drone_shipping_cost:
    cheapest_method = "Ground Shipping"
    cheapest_cost = ground_shipping_cost
elif ground_shipping_premium_cost < drone_shipping_cost:
    cheapest_method = "Ground Shipping Premium"
    cheapest_cost = ground_shipping_premium_cost
else:
    cheapest_method = "Drone Shipping"
    cheapest_cost = drone_shipping_cost

print(f"The cheapest method is {cheapest_method} with a cost of ${cheapest_cost:.2f}")
