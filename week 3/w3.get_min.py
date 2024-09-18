def get_minutes(hours, minuteas):
    total = hours*60+minuteas
    return total

hours=float(input("enter the number of hours"))
minutes=float(input("enter the numbe of minutes"))
total_minutes=get_minutes(hours,minutes)
print(total_minutes)








