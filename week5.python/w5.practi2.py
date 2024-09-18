def caluculate_total_amount():
    items=[]
    total_amount=0.0

    print("enter item details(type 'finish' to end)")
    
    while True:
        item_input=input("item name and price (e.g., cables $200)")
        if item_input.lower()=="finish":
            break
        try:
            item_name,price=item_input.rsplit(' ',1)
            item_price=float(price.strip('$'))
            items.append((item_name,item_price))
            total_amount+=item_price

        except ValueError:
            print("Invalid Value")

    print(f"total amount: ${total_amount:.2f}")
    return total_amount,items

def main():
    total_amount, items = caluculate_total_amount()

main()