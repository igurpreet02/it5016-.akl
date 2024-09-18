'''
task 2
program to caluculate the total amount of item with name of items
Author = Gurpreet Singh'''
def requistions_total():
    item=[]
    price=0

    print("enter the item(type 'end' to finsh)")
    while True:
        nameofitem=input("enter the item name and cost (e.g ,table $250)")
        if nameofitem.lower()=="end":
            break
    try:
        requistionsitem,itemprice=nameofitem.rsplit('',1)
        itemprice=float(input("enter the price of the item"))
        item.append((requistionsitem,itemprice))
        price += itemprice
    except ValueError:
        print(f"total_value:{price:.2f}")
        return item,price
requistions_total()
