def receive_tips(tips):
    total_tips = 0
    for tip in tips:
        total_tips += tip
        # if tip amount is less than 5 dollar, do not say thank you.
        # if tip < 5:
        #     continue
        # print("Thank you for tipping me $" + str(tip))
        if tip >= 5:
            print("Thank you for tipping me $" + str(tip))
    return total_tips

receive_tips([10, 5, 2])