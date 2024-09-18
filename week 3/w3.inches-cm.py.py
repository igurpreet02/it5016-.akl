def function1(inches):
    inches_to_cm=inches*2.54
    return inches_to_cm

def function2(cm):
    cm_to_inches=cm/2.54
    return cm_to_inches

inches=float(input("enter the no. of inches"))
cm=float(input("enter the no. of cm"))
print("inches to cm",(function1(inches)))
print("cm to inches",(function2(cm)))