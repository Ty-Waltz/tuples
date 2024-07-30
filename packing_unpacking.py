orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
]

def add_orders():
    global orders
    try:
        name = input("What is your first name? ")
        device = input("What deice are you ordering? ")
        amount = int(input("How many would you like? "))
    except ValueError:
        print("Please enter the correct characters")

    orders.append((name,device,amount))
    print(f"{name}'s was added successfully")

def unpack():
    order_name = input("What is the name for you order?: ").strip().lower()
    found = False
    
    for name, device, amount in orders:
        if name.lower() == order_name:
            print(f"{name} ordered {amount} {device}")
            found = True
            break
    if not found:
        print("That name in not on our order list")
def menu():
    print("1. Add an order")
    print("2. Find an order")
    print("3. Exit program")
while True:
    menu()
    choice = input("What would you like to do?(1,2,3): ")
    if choice == "1":
        add_orders()
    elif choice == "2":
        unpack()
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("that is not a valid option")
    
