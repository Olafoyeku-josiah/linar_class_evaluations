def age_categorization(name,p_year,b_year):
    """The functions helps you to calculate your age and it also gives you an age category,
    the function takes 3 parameter, 
    name = str, pyear = current year in integer, byear = user year of birth in integer"""
    user_age = int(p_year)  - int(b_year)
    if user_age>=0 and user_age<=5:
        """the if and elif keyword is used in this function to categorize the user's age whether the user is a baby or a kid or 
         a teenager or a young adult and also an adult. """
        print("{} you are currently {} years old and you are a baby.".format(name,user_age))
    elif user_age>=6 and user_age<=12:
        print("{} you are currently {} years old and you are a kid.".format(name,user_age))
    elif user_age>=13 and user_age<=19:
        print("{} you are currently {} years old and you are a teenager.".format(name,user_age))
    elif user_age>=20 and user_age<=35:
        print("{} you are currently {} years old and you are a young adult.".format(name,user_age))
    elif user_age>=35 and user_age<=float('inf') :
        print("{} you are currently {} years old and you are an adult.".format(name,user_age))
    else:
        print("Dear {}, pls enter the valid corresponding year ".format(name))
age_categorization(name = input("What's your name: "), p_year = input("What's the present year: "), b_year = input("What's your year of birth: "))