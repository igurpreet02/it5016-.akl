name=input("enter the name")
age=input("qenter the age")
print("hello,",name,"age",age,"yearsold",sep="")
#fstring
print(f"hello,{name}. you are {age}years old.")

pi=3.141592653589
print(pi)
formatpi=f"value of pi to 2 decimal places:{pi:.2f}"
print(formatpi)

salary=float(input("enter your weekly salary:"))
print(f"your weekly salary is ${salary:.2f}")

#
a=10
b=5
result=f"the result of {a} multiplied by {b} is { a*b }"
print(result)

name="james"
age=28
address="dreadon avenue"
info=f"""
name:{name}
age:{age}
address:{address}
"""
print(info)