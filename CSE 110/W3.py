import math

num_products = int(input('How many did you sell?'))
price = input = float(input('What was the price of each item? $'))
comission_rate = int(input('Commission rate? (%)'))
total_price = num_products * price
commission = total_price * (comission_rate / 100)

print(f'Comission for {num_products} at {price} each with {comission_rate / 100}\
       comission is ${commission:.2f}')


#Rounding options

# num = 3.126
# rounded_num = round(num, 2)
# rounded_ceil = math.ceil(num)
# rounded_floor = math.floor(num)

# print(num)
# print(rounded_ceil)
# print(rounded_num)
# print(rounded_floor)

# print(f':${rounded_num:.2f}')
# rounded_num = round(3.10, 2)
# print(f':${rounded_num:.2f}')
# print(f"${num:2f}")
# num = 3.126
# print(f"${num:2f}")
# print(f"${num:.1f}")
# print(f"${.0000000000000000345:.2e}") #scientific notation
# print("${:.2f} moneys".format(num))
# print(f"Eye color:{"brown":>15}!")
