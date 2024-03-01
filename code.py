class Drinks:
	def __init__(self, name, price, banknotes):
		self.name = name
		self.price = price
		self.banknotes = [100,50,20,10,5,1]

productA = Drinks("Boba", 5)
productB = Drinks("Tea", 6)
productC = Drinks("Cola", 7)

products = [productA, productB, productC]

def choose_product(self):
	print("Drinks Vending Machine")
	for product in products:
	print(f"Name: {product.name}, Price: ${product.price}")

	product = input("Amount to buy: ")
	for product in products:
        if product.name == product:
            return product
    print("No such product available.")
    return None

def quantity():
	while True:
	try:
		quantity = int(input("Enter quantity: "))
		if quantity <= 0:
			print("The product must be more than 0.")
		else:
			return quantity
	except ValueError:
		print("Invalid input")

def final_price(product, quantity):
	return product.price * quantity

def insert_note(product, price):
	print("The total price is ${price}.")
	amount = int(input("Insert notes: "))
	change = amount - price
	print ("Here is your balance: ${change}")
	return_note(change)

def return_note(amount):
	print("Returning change: ")
	for note in [100, 50, 20, 10, 5, 1]:
		while amount >= note:
			print(f"Returning ${note}")
			amount -= note

