def get_shoppinglist():
    shoppinglist=[]
    totalprice=0
    while True:
        item=input("enter the name of the item (or type 'done' to finish):")
        if item.lower() =="done":
          break
        try:
           price=float(input(f"enterthe price of '{item}:"))
           shoppinglist.append((item,price))
           totalprice+=price
        except ValueError:
           print("welcome to the shopping list program")
    return shoppinglist,totalprice
def main():
        print("welcome to the shopping list program")
        shoppinglist,totalprice=get_shoppinglist() 
        if not shoppinglist:
            print("no items were entered")
        else:
            print(" shoppinglist:")
            for item,price in shoppinglist:
                print(f"{item},${price:.2f}")
            print(f" total price:${totalprice:.2f}")
main()