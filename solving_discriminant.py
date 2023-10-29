"""This code calculates value of a discriminant after accepting inputs for discriminant value a,b and c from the user"""
#solving discriminant b^2-4ac:
discriminant_value1=int(input("enter the value of first discriminant value b:"))
discriminant_value2=int(input("enter the value of first discriminant value a:"))
discriminant_value3=int(input("enter the value of first discriminant value c:"))

disc_val_x=pow(discriminant_value1,2)
new_constant_y=4

left_hand_calOfDiscriminant=new_constant_y * discriminant_value2 * discriminant_value3
discriminant_total=disc_val_x - left_hand_calOfDiscriminant
print("the discriminant of the formula b^2-4ac is: {}".format(discriminant_total))
