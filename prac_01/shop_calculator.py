"""
Shop Calculator
"""

DISCOUNT_RATE = 0.1
PRICE_FOR_DISCOUNT = 100
total_price = 0

items = int(input("Number of items: "))
while items < 0:
    print("Invalid number of items: ")
    items = int(input("Number of items: "))

for item in range(1, items + 1):
    item_price = float(input("Price of item: "))
    total_price += item_price

if total_price >= PRICE_FOR_DISCOUNT:
    total_price *= DISCOUNT_RATE
print(f"Total price for {items} items is $ {total_price:.2f}")

