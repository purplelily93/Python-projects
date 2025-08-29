hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# task 1
total_price = 0

# Task 2
for price in prices:
  total_price += price
  print(total_price)

  # task 3
  average_price = total_price / len(prices)

# Task 4
print("Average Haircut Price: ", average_price)

# Task 5
new_prices = [price - 5 for price in prices]
 
# Task 6
print(new_prices)
