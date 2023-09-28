"""def greetings1(name, dept):
    print(f'Hi {name}, you are welcome to {dept} department!')

greetings1("Ade", "Web")
greetings1(name = input("Whats your name:\n"), dept = input("Whats your department:\n"))
"""
def age_calculator(name,pyear,byear):
    """The functions helps you to calculate your age/
    It takes 3 parameter, 
    name = str, pyear = present year in integer, byear = year of birth in integer"""
    age = int(pyear)  - int(byear)
    print(f'Hi {name} you are {age} years old')

age_calculator('emmag',2023,2006)
age_calculator(name = input("Whats your name:\n"), pyear = input("Whats the present year"), byear = input("Whats your year of birth"))

