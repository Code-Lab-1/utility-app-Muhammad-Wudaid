menu = {
    "Drinks": {
        "01": {"name": "7up", "price": 2.00},
        "02": {"name": "coke", "price": 2.50},
        "03": {"name": "fanta", "price": 2.00},
        "04": {"name": "sprite", "price": 3.00},
        "05": {"name": "pepsi", "price": 2.50},
        "06": {"name": "green tea", "price": 5.00},
        "07": {"name": "hot chocolate", "price": 5.00},
        "08": {"name": "fresh mint tea", "price": 10.00},
        "09": {"name": "hot lemonade", "price": 5.00},
        "10": {"name": "tea", "price": 1.00}
    },
    "Snacks": {
        "11": {"name": "doritos", "price": 2.00},
        "12": {"name": "lays", "price": 2.50},
        "13": {"name": "cheetos", "price": 10.00},
        "14": {"name": "sun chips", "price": 5.00},
        "15": {"name": "pringles", "price": 5.00},
        "16": {"name": "snicker Bar", "price": 3.50},
        "17": {"name": "kitkat", "price": 2.50},
        "18": {"name": "M&Ms", "price": 2.50},
        "19": {"name": "cadbury", "price": 2.00},
        "20": {"name": "toblerone", "price": 2.00}
    }
}

# Display the menu to the user
for category, items in menu.items():
    print("-------")
    print(category)
    for code, item in items.items():
        print(f"{code}: {item['name']} - ${item['price']}")
    print()

total_cost = 0

while True:
    # Take user input
    selected_code = input("Please enter a code to select an item from the menu: ")

    # Check if the selected code is in the menu
    if selected_code in menu["Drinks"]:
        # Get the name and price of the selected item
        name = menu["Drinks"][selected_code]['name']
        price = menu["Drinks"][selected_code]['price']
        
        # Add the price of the item to the total cost
        total_cost += price
    elif selected_code in menu["Snacks"]:
        # Get the name and price of the selected item
        name = menu["Snacks"][selected_code]['name']
        price = menu["Snacks"][selected_code]['price']
        
        # Add the price of the item to the total cost
        total_cost += price
    else:
        print("Sorry, the code you entered is not available in the menu.")
        continue

    # Ask the user if they want to buy more items
    additional_items = input("Do you want to buy any additional items (yes/no)? ")
    if additional_items.lower() == "no":
        break

# Get the amount of money entered by the user
payment = float(input("Please enter the amount of money: $"))

# Check if the entered amount is greater than or equal to the total cost of the items
if payment >= total_cost:
    # Calculate the change
    change = payment - total_cost
    
    # Dispense the items
    print("Your food has been dispensed.")
    
    # Return the change to the user
    print(f"Here is your change: ${change}")
else:
    print("Sorry, you did not enter enough money.") 
