def caluculate_total_amount():
    items=[]
    itemprice=0
    while True:
        item=input("enter the name of item(or type end to finish)")
        if item.lower()=="done":
           break
        try:
            price=input(f"enter the price of {item}")
            items.append((item,price))
            itemprice+=price
        except ValueError:
            print("welcome to shopping list program")
            return items,itemprice
def main():
    items,itemprice=caluculate_total_amount()
    if not items:
        print("no items were enrter")
    else:
        print("items:")
        for item,price in items:
          print(f"{item},${price:.2f}")
        print(f" total price:${itemprice:.2f}")
main()





