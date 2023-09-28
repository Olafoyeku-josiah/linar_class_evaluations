"""name1="level"
length1=len(name1)
i=0
for n in range(-1,(-length1-1),-1):
    print(name1[i],"\t",name1[n])
    i=i+1"""

sentence="linar python class"
school_name=sentence[0:5]
print("the name of the school i'm attending is: {}".format(school_name))
course=sentence[6:12]
print("the course i'm studying is {} ".format(course))
batch=sentence[13:19]
print("and currently studying with {} of 2022/2024".format(batch))

x="python"
y=x[::-1]
print(y)