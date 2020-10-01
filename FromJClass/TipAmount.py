def tip_amount(tip_percentage, total):
    print("The total is: " + str(total))
    print("The tip percentage is: " + str(tip_percentage * 100) + "%")
    print("The tip amount will be : " + str(total * tip_percentage) + " dollars")

tip_amount(.10,100)

