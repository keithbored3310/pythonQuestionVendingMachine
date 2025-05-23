class Drinks:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Global list of available banknotes for the machine
AVAILABLE_BANKNOTES = [100, 50, 20, 10, 5, 1]

productA = Drinks("Boba", 5)
productB = Drinks("Tea", 6)
productC = Drinks("Cola", 7)

products = [productA, productB, productC]

def choose_product():
    print("Drinks Vending Machine")
    print("Available Products:")
    for i, product_item in enumerate(products):
        print(f"{i+1}. Name: {product_item.name}, Price: ${product_item.price}")

    while True:
        try:
            choice = input("Choose a product by number (or type 'exit' to cancel): ")
            if choice.lower() == 'exit':
                return None
            choice_idx = int(choice) - 1
            if 0 <= choice_idx < len(products):
                return products[choice_idx]
            else:
                print("Invalid choice. Please select a valid number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_quantity():
    while True:
        try:
            quantity_val = int(input("Enter quantity: "))
            if quantity_val <= 0:
                print("The product quantity must be more than 0.")
            else:
                return quantity_val
        except ValueError:
            print("Invalid input. Please enter a whole number for the quantity.")

def calculate_final_price(product, quantity_val):
    return product.price * quantity_val

def process_payment(total_price):
    print(f"The total price is ${total_price}.")
    while True:
        try:
            amount_inserted_str = input(f"Insert notes (total amount, at least ${total_price}): ")
            amount_inserted = int(amount_inserted_str)
            if amount_inserted < total_price:
                print(f"Amount inserted (${amount_inserted}) is less than the total price (${total_price}). Please insert enough money.")
            else:
                change = amount_inserted - total_price
                print(f"Amount paid: ${amount_inserted}")
                if change > 0:
                    print(f"Your change is: ${change}")
                    return_change(change)
                else:
                    print("Exact amount paid. No change.")
                return True # Payment successful
        except ValueError:
            print("Invalid input. Please enter a whole number for the amount inserted.")

def return_change(amount_to_return):
    print("Returning change denominations:")
    original_amount_to_return = amount_to_return # Keep a copy for final check
    returned_notes_summary = {}

    for note in AVAILABLE_BANKNOTES:
        count = 0
        while amount_to_return >= note:
            amount_to_return -= note
            count += 1
        if count > 0:
            returned_notes_summary[note] = count
            print(f"Returning {count} x ${note}")

    # This check is a safeguard, ideally the logic ensures full change is calculated
    if amount_to_return > 0:
        print(f"Warning: Unable to return full change. Remaining unreturned: ${amount_to_return}")


# Main execution logic
def run_vending_machine():
    print("Welcome to the Vending Machine!")

    while True: # Loop for multiple transactions
        selected_product = choose_product()

        if selected_product is None:
            print("Transaction cancelled.")
        else:
            print(f"You selected: {selected_product.name}")
            quantity_ordered = get_quantity()
            final_price = calculate_final_price(selected_product, quantity_ordered)

            if process_payment(final_price):
                print(f"Thank you for your purchase of {quantity_ordered} {selected_product.name}(s)!")
            else:
                # This else might not be reachable if process_payment always loops until success or user exits (not implemented)
                print("Payment failed or was cancelled.")

        another_purchase = input("Would you like to make another purchase? (yes/no): ").lower()
        if another_purchase != 'yes':
            break

    print("Exiting vending machine. Goodbye!")

if __name__ == "__main__":
    run_vending_machine()
