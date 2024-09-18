'''
task 3
program which intended to make decisions
Author= Gurpreet Singh
'''
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
def responding_to_requests(price):
    if price<=500:
        status="Approved"
       
    else:
        status="pending"
        return status
def main():
    item,price=requistions_total()
    status=responding_to_requests(price)

    print(f"total:{price:.2F}")
    print(f"status:{status}")
    print("approval reffernce number:FN19001")
main()
