def eat_apples(num_of_apples, on_diet):
    apples_remaining = num_of_apples

    # Loop
    while apples_remaining > 0 and not on_diet:
        print("Remaining apple = " + str(apples_remaining))
        apples_remaining -= 1
        print("Thank you!")

    print("Done")

    return

    # eat an apple
    apples_remaining = apples_remaining - 1

    # say thank you
    # print("Thank you!")



eat_apples(5, False)