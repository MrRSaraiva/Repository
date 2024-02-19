#   This is a program to check the stock, price and value of items sold in a cafe

#   Menu, stock and price lists
menu = ["Coffee", "Tea", "Cocoa", "Pastry"]
stock_list = [254, 312, 96, 52]
price_list = [2.50, 1.90, 3.10, 2.20]

#   Stock - Displays the amount of items in stock
stock = dict(zip(menu, stock_list))

print("Items in stock:\n")

for item, stock in stock.items():
    print(item,"\t", stock)

print("\n\n")

#   Price - Displays item prices
price = dict(zip(menu, price_list))

print("Item prices:\n")

for item, prices in price.items():
    print(item,"\t", prices)

print("\n\n")

#   Stock worth
stock_worth = dict(zip(stock_list, price_list))
item_values = []
total_stock = 0

#   Stock worth - Calculates the stock worth (per item and total)
for price, stock in stock_worth.items():
    item_values.append(price * stock)
    total_stock += (price * stock)

#   Stock worth - Displays the stock worth (per item and total)
menu_item_values = dict(zip(menu, item_values))

print("Stock value (per item and total): \n")

for item, values in menu_item_values.items():
    print(item,"\t", values)

print("\nTotal\t",round(total_stock,2))