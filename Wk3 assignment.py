# Function calculate_discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

print(calculate_discount(100, 25))
print(calculate_discount(100, 10)) 

# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Calculate and print the final price
    final_price = calculate_discount(price, discount_percent)
    print(f"The final price after applying the discount is: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numerical values.")