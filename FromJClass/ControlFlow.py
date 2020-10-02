# Control flow to control the ways to get to another pages depends on the tasks
# EX) Are you 18 or up?
# Y redirect to the website, N do not give the access.

# def website_welcome(name, age):
#     greetings = "Welcom " + name + "!"
#     print(greetings)
#     year_born = 2020 - age
#     print("You were born in " + str(year_born))
#
# website_welcome("Sung", 30)

# refactor, use boolean
def website_welcome(name, age):
    if age >= 18:
        print("Welcome " + name + "!")
    else:
        print("Opps, you are too young to proceed to next level")
        years_left = 18 - age
        print("Wait another " + str(years_left) + " years to become a member")

website_welcome("Sung", 10)