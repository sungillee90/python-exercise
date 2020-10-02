def can_watch_movie(age, with_parents):
    if age >= 17:
        print("Welcome! Enjoy the show!")
        return True
    else:
        if with_parents:
            print("Yes, you can watch it!")
            return True
        else:
            print("Sorry, you MUST to have your parents")
            return False


can_watch_movie(18, False)