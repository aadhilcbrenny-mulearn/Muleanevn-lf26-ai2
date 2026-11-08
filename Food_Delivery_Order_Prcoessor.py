import sys

menu = [
    {"name": "Chicken Biriyani", "price": 150},
    {"name": "Fried Rice", "price": 120},
    {"name": "Chicken Burger", "price": 100},
    {"name": "Masala Dosa", "price": 60},
    {"name": "Veg Pizza", "price": 200}
]
orders = [
    {
        "customer_name": "Arjun",
        "mobile_no": "9876543210",
        "items": {
            "Chicken Biriyani": 2,
            "Chicken Burger": 1
        },
        "total_price" : 400
    },
    {
        "customer_name": "Rahul",
        "mobile_no": "9876543211",
        "items": {
            "Fried Rice": 1,
            "Masala Dosa": 2
        },
        "total_price" : 240
    },
    {
        "customer_name": "Anjali",
        "mobile_no": "9876543212",
        "items": {
            "Chicken Biriyani": 1,
            "Veg Pizza": 1
        },
        "total_price" : 350
    },
    {
        "customer_name": "Adithya",
        "mobile_no": "9876543213",
        "items": {
            "Chicken Burger": 2,
            "Masala Dosa": 1
        },
        "total_price" : 260
    },
    {
        "customer_name": "Meera",
        "mobile_no": "9876543214",
        "items": {
            "Fried Rice": 2,
            "Veg Pizza": 1
        },
        "total_price" : 440
    },
    {
        "customer_name": "Vishnu",
        "mobile_no": "9876543215",
        "items": {
            "Chicken Biriyani": 1,
            "Fried Rice": 1,
            "Chicken Burger": 1
        },
        "total_price" : 370
    },
    {
        "customer_name": "Sneha",
        "mobile_no": "9876543216",
        "items": {
            "Masala Dosa": 3
        },
        "total_price" : 80
    },
    {
        "customer_name": "Akash",
        "mobile_no": "9876543217",
        "items": {
            "Veg Pizza": 2,
            "Chicken Biriyani": 1
        },
        "total_price" : 500
    },
    {
        "customer_name": "Diya",
        "mobile_no": "9876543218",
        "items": {
            "Fried Rice": 1,
            "Chicken Burger": 2
        },
        "total_price" : 320
    },
    {
        "customer_name": "Nikhil",
        "mobile_no": "9876543219",
        "items": {
            "Chicken Biriyani": 2,
            "Masala Dosa": 2,
            "Veg Pizza": 1
        },
        "total_price" : 620
    }
]

food_items = []
for menu_item in menu:
    food_items.append(menu_item["name"])

def calculateTotal(items, distance):
    totalPrice = 0
    for i,j in items.items():
        for item in menu:
            if item["name"] == i:
                totalPrice += j * item["price"]
    subtotal = calculateDiscount(items,totalPrice)
    deliveryCharges = calculateDeliveryCharges(subtotal,distance)
    totalPrice = subtotal + deliveryCharges
    return totalPrice

def calculateDiscount(items, price):  
    for i,j in items.items():
        if j >= 3:
            return price * 0.1      #Applying 10% discount if quantity ordered >= 3
        else :
            return price
        
def calculateDeliveryCharges(subtotal,distance):
    if subtotal > 500:
        return 0
    elif distance > 0 and distance <= 3 :
        return 30
    elif distance > 3 and distance <=7 :
        return 50
    elif distance > 7:
        return 50 + distance * 10

def highestValueOrder() :
    highest_order = orders[0]
    highest_price = orders[0]["total_price"]
    for order in orders:
        if order["total_price"] > highest_price:
            highest_order = order
            highest_price = order["total_price"]
    print("Highest Value Order:\n")
    for key,value in highest_order.items():
        print(f"{key} : {value}")
        
def orderSummary() :
    with open("order-summary.txt", "w") as file:
        for order in orders:
            for key,value in order.items():
                file.write(f"{key} -> {value}\n")
            file.write("\n")
    file.close()

def displayOrderSummary() :
    with open("order-summary.txt", "r") as file:
        content = file.read()
        print(content)
    file.close()


def calculateOrder(name, phNo, count, distance):
    items = {}
    flag = 0
    print("Enter item name and quantity (item:quantity):\n")
    for i in range(count):
        item, quantity = tuple(input((f"Item{i+1}-> ")).split(":",1))
        if item == " " or quantity == " ":
            print("Please Enter an input")
            return 0
        elif item.strip() in food_items:
            for menuItem in menu:
                    flag = 1
                    items[item.strip()] = int(quantity)
                    break
            if flag == 0:
                print("Error: Item not in menu\n")
                return 0
    orders.append({"customer_name" : name, "mobile_no" : phNo, "items" : items, "total_price" : calculateTotal(items, distance)})
    print("Order placed successfully\n")
    return 1

print("\n------WELCOME TO FOOD ORDER MANAGEMENT SYSTEM------\n")
try:
    while(True) :
        print("\n1.Place an order\n2.Display Highest Value Order\n3.View Order Summary\n4.Exit\n ")
        choice = int(input("Enter choice: "))
        if choice == 1:
            name = input("Enter name of customer")
            phNo = input("Enter mobile number")
            count = int(input("enter total number of items:"))
            distance = int(input("How much distance to travel (in km) ?:"))
            if(not calculateOrder(name, phNo, count, distance)):
                continue
            orderSummary()

        elif choice == 2:
            highestValueOrder()

        elif choice == 3:
            displayOrderSummary()
        else:
            break
except KeyboardInterrupt :
    sys.exit(0)

except Exception as e:
    print(e)




        

    


