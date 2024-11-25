def calculate_discount(price,discount_percent):
    if discount_percent >=20:
        discounted_price = price - (price * (discount_percent / 100))
        return discounted_price
    else:
        return price
    
print("Enter the original price \n")
original_price = int(input())
print("Enter the percentage discount allowed \n")
discount = int(input())

new_price = calculate_discount(original_price,discount)


print(f"You will pay ${new_price} for the product")
    