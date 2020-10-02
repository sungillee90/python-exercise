def can_watch_movie(age, with_parents):
    if age >= 17 or with_parents:
        print("Welcome! Enjoy the show!")
        return True
    # else:
    #     if with_parents:
    #         print("Yes, you can watch it!")
    #         return True
    #     else:
    #         print("Sorry, you MUST to have your parents")
    #         return False

        # else if for python
        # elif age < 17 and with_parents:
        #     print("Yes, you can watch it!")
        #     return True

    else:
        print("Sorry, you MUST to have your parents")
        return False

can_watch_movie(8, False)