itinerary = []

def flight_itinerary():
    global itinerary
    name = input("What is your first name? ")
    origin = input("Where are you flying from? ")
    destination = input("Where are you flying to? ")

    itinerary.append((name,origin,destination))
    print(f"{name}'s was added successfully")

def show_itinerary():
    for index,(name, origin, destination) in enumerate(itinerary):
        print(f"Itinerary {index + 1}: {name} - from {origin} to {destination}")
def menu():
    print("1. Create a new flight")
    print("2. Show Itinerary")
    print("3. Exit")

while True:
    menu()
    choice = input("Chose an option: ")
    if choice == "1":
        flight_itinerary()
    elif choice == "2":
        show_itinerary()
    elif choice =="3":
        print("Exiting the program.")
        break
    else:
        print("That is not a valid option")