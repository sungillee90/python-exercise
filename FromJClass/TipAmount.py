# def tip_amount(tip_percentage, total):
#     print("The total is: " + str(total))
#     print("The tip percentage is: " + str(tip_percentage * 100) + "%")
#     print("The tip amount will be : " + str(total * tip_percentage) + " dollars")
#
# tip_amount(.10,100)

def tip_amount(tip_percentage, total):
    # print("The total is: " + str(total))
    # print("The tip percentage is: " + str(tip_percentage) + "%")
    # print("The tip amount will be : " + str(total * tip_percentage * 0.01) + " dollars")
    return (total * tip_percentage * 0.01)

# tip_amount(10,100)

def buy_Produce(num_tomatoes, num_bananas):
    total_Price = num_tomatoes * 2.00 + num_bananas * 1.50
    print("Welcome to Trader Joe's!")
    print("Number of tomatoes you purchased: " + str(num_tomatoes))
    print("Number of bananas you purchased: " + str(num_bananas))
    print("Total price is : " + str(total_Price) + " dollars")

    tips = tip_amount(15, total_Price)
    print("Total tip amount is = " + str(tips))

buy_Produce(2,3)