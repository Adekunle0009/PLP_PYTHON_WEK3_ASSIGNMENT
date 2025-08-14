# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate and display the final price
final_price = calculate_discount(original_price, discount_percent)

print(f"Final price: {final_price}")
