#for value in range(1,100,1):
#       print(value)

"""sum=0
for value in range(1,51):
       sum+=value
print(sum)"""
'''
for i in range(1,10):
    for j in range(1,i+1):
       print(i, end="") 
    print("")
'''

"""for i in range(1,10):
   for j in range(1,i+1):
       print("*"*i,end="")
   print("")"""
#i=10
"""for i in range(1,5):
   for j in range(1,i+1):
      print(i,end="")
   print("")"""
#s+=1"""
#example of an infinite loop
"""count=0
while True:
    print("count:",count)
    count+=1
    if count>=10:
        break"""
#another example of an infiinite loop
"""while 1:
    print("this loop will run forever!!",end="")"""
"""for i in range(1,6):
    for j in range(5,i-1,-1):
        print("*")
    print()"""

"""def sum(n):
   s=0
   for i in range(1,n+1):
        for j in range(i,i+1):
            s+=j
   return s"""
"""print(f'even number from 1000 to 0')
even_number=1000
print(f'the first value is {even_number}')
while even_number>0:
    print(f'another even number is {even_number-2}')
    even_number-=2
print(f'thats all for even number evaluation')"""

print(f'this shows even number from 2 to 1000')
even_number=2
print(f'the first even value is {even_number}')
while even_number<100:
    print(f'another even number is {even_number+2}')
    even_number+=2
print(f'thats all for even number evaluation')
