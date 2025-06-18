from datetime import datetime #to have a proper dateformat so that we can have input validation for expiration date
from tabulate import tabulate #formatting tables so that we can display our dictionaries in a nice table format in the terminal



# Initial inventory using a list of dictionaries
# Each item contains keys: item_id, item_name, stock_quantity, price, and expiration_date

# === Inventory list ===
# Stores all inventory items as dictionaries
inventory = [
    {"item_id": "SKU001", "item_name": "Yakult 10 pack", "stock_quantity": 20, "price": 25000, "expiration_date": "2025-07-01"},
    {"item_id": "SKU002", "item_name": "Susu Greenfields", "stock_quantity": 15, "price": 18000, "expiration_date": "2025-06-20"},
    {"item_id": "SKU003", "item_name": "Olive Oil Felipo Berio", "stock_quantity": 10, "price": 95000, "expiration_date": "2026-01-01"},
    {"item_id": "SKU004", "item_name": "Rinso Liquid Frontloading Machine", "stock_quantity": 25, "price": 32000, "expiration_date": "2027-05-01"},
    {"item_id": "SKU005", "item_name": "Rapika for Clothes", "stock_quantity": 30, "price": 15000, "expiration_date": "2026-08-15"},
    {"item_id": "SKU006", "item_name": "Bebek Kloset", "stock_quantity": 40, "price": 13000, "expiration_date": "2026-02-10"},
    {"item_id": "SKU007", "item_name": "Wangshan Fuji Apples", "stock_quantity": 12, "price": 30000, "expiration_date": "2025-06-15"},
    {"item_id": "SKU008", "item_name": "Sunpride Bananas", "stock_quantity": 18, "price": 22000, "expiration_date": "2025-06-14"},
    {"item_id": "SKU009", "item_name": "Ready to Go Mix Salad", "stock_quantity": 8, "price": 17000, "expiration_date": "2025-06-13"},
    {"item_id": "SKU010", "item_name": "Sunlight", "stock_quantity": 35, "price": 14000, "expiration_date": "2026-03-30"}
] # item_id, item_name, and expiration_date are all strings using " ", and price and stock_quantity are integers 


# === Recycle bin ===
# Used for delete_item function to be able to restore "deleted" data
recycle_bin = []

# === Pause Function ===
def return_to_main_menu(): 
    """
    A helpful tool to allow the user to pause after output,
    so they can read the result before returning to the main menu.
    """
    input("\nPress Enter to return to the main menu...") #waits for the user to press enter


# === CRUD Function Definitions ===

def create_item():
    """
    Adds a new item to the inventory
    Includes checks for duplicate Item IDs and optional name warnings
    Validates input and also uses proper datetime for expiration date format
    """
    while True:
        print('\n[Add New item]')
        if inventory:
            print("\n Current Inventory (ID | Name):")
            for item in inventory:
                print(f"{item['item_id']} | {item['item_name']}")
        else:
            print("\n Inventory is currently empty.")

        item_id = input('Enter New Item ID (e.g., SKU011): ').strip().upper()
        for item in inventory:
            if item["item_id"] == item_id:
                print(" Item ID already exists. Please use a different ID.\n")
                return

        item_name = input('Enter New Item Name (e.g., Sunlight 750ml):')
        for item in inventory:
            if item["item_name"].lower() == item_name.lower():
                while True:
                    warn = input(f" An item with the name '{item_name}' already exists. Continue anyway? (Y/N): ").strip().upper()
                    if warn == "Y":
                        break
                    elif warn == "N":
                        print(" Canceled. Item not saved.\n")
                        return
                    else:
                        print(" Invalid input. Please type 'Y' or 'N'.")

        while True:
            try:
                stock_quantity = int(input("Enter stock quantity (number, e.g., 20): "))
                break
            except ValueError:
                print(" Invalid input. Please enter a whole number.")

        while True:
            try:
                price = int(input("Enter price (e.g., 15000): "))
                break
            except ValueError:
                print(" Invalid input. Please enter a whole number like 15000 or 125000.")

        while True:
            expiration_date = input('Enter Expiration Date (e.g., 2026-12-25): ').strip()
            try:
                datetime.strptime(expiration_date, "%Y-%m-%d")
                break
            except ValueError:
                print(" Invalid date format. Please use YYYY-MM-DD like 2026-12-25.")

        while True:
            confirm = input("Do you want to save this item? (Y/N): ").strip().upper()
            if confirm == "Y":
                break
            elif confirm == "N":
                print(" Canceled. Item not saved.\n")
                return
            else:
                print(" Invalid input. Please type 'Y' or 'N'.")

        new_item = {
            "item_id": item_id,
            "item_name": item_name,
            "stock_quantity": stock_quantity,
            "price": price,
            "expiration_date": expiration_date
        }
        inventory.append(new_item)
        print("Item added successfully!\n")
        print(" Updated Inventory:")
        print(tabulate(inventory, headers="keys", tablefmt="grid"))

def read_data():
    """
    Reads and displays inventory data.
    Offers options to view all items or search by item ID (partial match supported).
    Includes sample format hint for ID search.
    """
    while True:
        print("\n--- READ INVENTORY MENU ---")
        print("1. View All Items")
        print("2. Search Item by ID (Exact Match)")
        print("3. Search Item by Name (Partial Match)")
        print("4. Return to Main Menu")
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            if not inventory:
                print("Inventory is empty.")
            else:
                print(f"\nTotal items in inventory: {len(inventory)}")
                print("\n--- INVENTORY LIST ---")
                print(tabulate(inventory, headers="keys", tablefmt="grid"))

        elif choice == "2":
            if not inventory:
                print("Inventory is empty.")
            else:
                search_id = input("Enter Item ID to search (e.g., SKU001): ").strip().upper()
                found = False
                for item in inventory:
                    if "item_id" in item and item["item_id"].upper() == search_id:
                        print("\n=== ITEM FOUND ===")
                        print(tabulate([item], headers="keys", tablefmt="grid"))
                        found = True
                        break
                if not found:
                    print(f"No item found with ID: {search_id}. Make sure it matches exactly (e.g., SKU001).")

        
        elif choice == "3":
            if not inventory:
                print("Inventory is empty.")
            else:
                partial_item_name = input("Enter part of the item name to search: ").strip().lower()
                matches = []
                for item in inventory:
                    if "item_name" in item and partial_item_name in item["item_name"].lower():
                     matches.append(item)
                if matches:
                    print(f"\n=== MATCHING ITEMS FOR '{partial_item_name}' ===")
                    print(tabulate(matches, headers="keys", tablefmt="grid"))
                else:
                    print(f"No item found containing name: {partial_item_name}")

        elif choice == "4":
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

def update_item():
    """"
    Allows user to update an existing item's detail (name, stock, price, expiry).
    Includes input validation and confirmation.
    Loops to allow multiple updates before returning to the main menu.
    """

    while True:
        print("\n=== UPDATE ITEM MENU ===")
        if not inventory:
            print("Inventory is empty. Nothing to update.")
            return

        print("\nAvailable items in inventory:")
        for item in inventory:
            print(f"ID: {item['item_id']}, Name: {item['item_name']}, Stock: {item['stock_quantity']}, Price: Rp{item['price']}, Expiry: {item['expiration_date']}")

        item_id = input("Enter the Item ID to update: ").strip().upper()
        item = None
        for i in inventory:
             if i['item_id'] == item_id:
                item = i
                break
        if not item:
            print("Item not found in the inventory.")
            continue

        print("Item found:")
        for key, value in item.items():
            print(f"{key.capitalize()}: {value}")

        while True:
            confirm = input("Do you want to update this item? (Y/N): ").strip().upper()
            if confirm == 'Y':
                break
            elif confirm == 'N':
                print("Update cancelled.")
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")
        if confirm != 'Y':
            continue

        print("\nWhich item detail would you like to update?")
        print("1. Name")
        print("2. Stock")
        print("3. Price")
        print("4. Expiration Date")

        detail_choice = input("Enter your choice (1-4): ").strip()
        detail_map = {
            "1": "item_name",
            "2": "stock_quantity",
            "3": "price",
            "4": "expiration_date"
        }
        detail_labels = {
            "item_name": "Item Name",
            "stock_quantity": "Stock",
            "price": "Price",
            "expiration_date": "Expiration Date"
        }

        if detail_choice not in detail_map:
            print("Invalid choice. Returning to update menu.")
            continue

        detail_to_update = detail_map[detail_choice]

        if detail_to_update in ["stock_quantity", "price"]:
            while True:
                try:
                    new_value = int(input(f"Enter new {detail_labels[detail_to_update]}: "))
                    if new_value < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a non-negative integer.")
        elif detail_to_update == "expiration_date":
            while True:
                new_value = input(f"Enter new {detail_labels[detail_to_update]} (YYYY-MM-DD): ").strip()
                try:
                    datetime.datetime.strptime(new_value, "%Y-%m-%d")
                    break
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
        else:
            new_value = input(f"Enter new {detail_labels[detail_to_update]}: ").strip()

        while True:
            confirm_final = input(
                f"Are you sure you want to update the item detail '{detail_labels[detail_to_update]}' to '{new_value}'? (Y/N): "
            ).strip().upper()
            if confirm_final == 'Y':
                item[detail_to_update] = new_value
                print("Item updated successfully.")
                break
            elif confirm_final == 'N':
                print("Update cancelled.")
                break
            else:
                print("Invalid input. Please enter 'Y' or 'N'.")

        repeat = input("\nDo you want to update another item? (Y/N): ").strip().upper()
        if repeat != 'Y':
            break

def delete_item():
    """
    Allows user to delete items from inventory by ID or delete all.
    Includes confirmation prompts, and input validation. 
    Also includes a recycle bin feature to store deleted items, view deleted items, restore items and permanently empty the recycle bin.
    """

    while True:
        print("\n=== Delete Menu ===")
        if not inventory:
            print("Inventory is empty.")
        else:
            print("\nCurrent Inventory:")
            print(tabulate(inventory, headers="keys", tablefmt="grid"))

        print("\nOptions:")
        print("1. Delete an item by ID")
        print("2. Delete ALL items")
        print("3. View Recycle Bin")
        print("4. Restore item from Recycle Bin")
        print("5. Empty Recycle Bin Permanently")
        print("6. Return to Main Menu")
        
        choice = input("Choose an option (1-6): ").strip()


        if choice == '1':
            item_id = input("Enter the ID of the item to delete: ").strip().upper()
            found_item = None
            for i in inventory:
                if i["item_id"] == item_id:
                    found_item = i
                    break

            if found_item:
                print("\nItem found:")
                print(tabulate([found_item], headers="keys", tablefmt="grid"))
                while True:
                    confirm = input(f"Are you sure you want to delete item '{found_item['item_name']}' (Y/N)? ").strip().upper()
                    if confirm == 'Y':
                        recycle_bin.append(found_item.copy())
                        inventory.remove(found_item)
                        print(f"Item '{found_item['item_name']}' with ID {item_id} has been removed and moved to the recycle bin.")
                        break
                    elif confirm == 'N':
                        print("Deletion canceled.")
                        break
                    else:
                        print("Invalid input. Please enter Y or N.")
            else:
                print("Item ID not found. Please try again.")

        elif choice == '2':
            if not inventory:
                print("Inventory is already empty.")
                continue
            confirm = input("Are you sure you want to delete ALL items in the inventory? (Y/N): ").strip().upper()
            if confirm == 'Y':
                for item in inventory:
                    recycle_bin.append(item.copy())
                inventory.clear()
                print("All items have been deleted and moved to the recycle bin.")
            elif confirm == 'N':
                print("Bulk deletion canceled.")
            else:
                print("Invalid input. Please enter Y or N.")

        elif choice == '3':
            if not recycle_bin:
                print("Recycle bin is empty.")
            else:
                print("\nRecycle Bin Contents:")
                print(tabulate(recycle_bin, headers="keys", tablefmt="grid"))

        elif choice == '4':
            if not recycle_bin:
                print("Recycle bin is empty. Nothing to restore.")
                continue
            item_id = input("Enter the ID of the item to restore: ").strip().upper()
            found_item = None
            for i in recycle_bin:
                if i["item_id"] == item_id:
                    found_item = i
                    break
            if found_item:
                inventory.append(found_item)
                recycle_bin.remove(found_item)
                print(f"Item '{found_item['item_name']}' has been restored to the inventory.")
            else:
                print("Item not found in the recycle bin.")

        elif choice == '5':
            if not recycle_bin:
                print("Recycle bin is already empty.")
                continue
            confirm = input("Are you sure you want to permanently delete all items in the recycle bin? (Y/N): ").strip().upper()
            if confirm == 'Y':
                recycle_bin.clear()
                print("Recycle bin has been emptied.")
            elif confirm == 'N':
                print("Action canceled.")
            else:
                print("Invalid input. Please enter Y or N.")

        elif choice == '6':
            print("Returning to Main Menu...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


# === Wrapper Functions ===

def create_item_menu():
    """
    Wrapper for create_item(). Adds a pause after execution.
    """
    create_item()
    return_to_main_menu()


def read_data_menu():
    """
    Wrapper for read_data(). Adds a pause after execution.
    """
    read_data()
    return_to_main_menu()


def update_item_menu():
    """
    Wrapper for update_item(). Adds a pause after execution.
    """
    update_item()
    return_to_main_menu()


def delete_item_menu():
    """
    Wrapper for delete_item(). Adds a pause after execution.
    """
    delete_item()
    return_to_main_menu()


# === Main Menu ===


def show_main_menu():
    """
    Displays the main menu and routes user to selected CRUD operations.
    Loops until user chooses to exit.
    """
    while True:
        print("\n=== INDOMARET WAREHOUSE INVENTORY SYSTEM ===")
        print("Please select an option:")
        print("1. View Inventory")
        print("2. Add New Item")
        print("3. Update Existing Item")
        print("4. Delete Item from Inventory")
        print("5. Exit Program")
        
        # User input and choosing menu
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            read_data_menu()
        elif choice == '2':
            create_item_menu()
        elif choice == '3':
            update_item_menu()
        elif choice == '4':
            delete_item_menu()
        elif choice == '5':
            print("Thank you! Exiting the program.")
            break
        else:
            print("Invalid input. Please enter a number between 1 and 5.")

# === Start the program ===
show_main_menu()
