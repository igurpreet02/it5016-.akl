def total_user_nubmer():
    total=0
    number=int(input("enter a number (0 to end):"))
    while number !=0:
        total+=number
        number=int(input("enter a number(0 to end):"))
    print("total:",total)

def main():
        total_user_nubmer()
main()