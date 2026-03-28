def print_all_info(date, my_money, category, payment, price_of_item):
    left = my_money - price_of_item
    print(f"date: {date} , amount: {my_money}$ , category: {category} , payment: {payment}, price: {price_of_item}$, left: {left}$")
    
    with open("summary.txt", "a") as myfile:
        myfile.write(f"[date:{date} , mymoney:{my_money}$ , category:{category} , payment:{payment}, price_of_item:{price_of_item}$, left_of_money:{left}$]\n")

while True:
    print("Hello My Bank")

    date = input("Enter a date (y-m-d): ")
    my_money = float(input("Enter your money: $"))
    price_of_item = float(input("Enter your price: $"))
    category = input("Enter a category: ")
    payment = input("Enter a payment: ")

    print_all_info(date, my_money, category, payment, price_of_item)
    
    cont = input("Do you want to exit? (y/n): ")
    if cont.lower() == "y":
        print("Goodbye!")
        break
