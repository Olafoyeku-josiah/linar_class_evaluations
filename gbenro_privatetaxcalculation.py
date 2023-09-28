print("welcome to gbenro's tax calculation session!! ")
user_name=input("enter your name:")
print("Hello "+user_name)

user_salary=float(input("enter your monthly salary: "))
new_const1=10
new_const2=100
user_tax=new_const1/new_const2 * user_salary
month_leftover=user_salary-user_tax
print("Given private tax rate as 10%, your tax for the month will be: "+str(user_tax))
print("Your month leftover after payment of tax is: " +str(month_leftover))

print("thank you for choosing gbenro's tax calculation session "+(user_name))