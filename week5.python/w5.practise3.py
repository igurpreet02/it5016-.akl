def collect_user_data(id_counter):
    print("enter user information")
    username=input("name:")
    user_id=input("staff id:")
    user_email=input("email adress:")

    unique_id=id_counter + 1
    id_counter=unique_id

    print("user information:")
    print(f"name:{username}")
    print(f"age:{user_id}")
    print(f"email:{user_email}")
    print(f"unique_id:{id_counter}")
    return username,user_email,user_id,id_counter

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

def categorize_request(total_amount):

    if total_amount<500:
        status="approved"
       
    elif total_amount>500:
        status="pending"
    
    else:
        print("enter correct value")
    return status

def main():
    id_counter=5000
    id_counter,username,user_id,user_email=collect_user_data(id_counter)
    total_amount,items = caluculate_total_amount()
    status=categorize_request(total_amount)

    print("request summary")
    print(f"total amount $ {total_amount:.2f}")
    print(f"status:{status}")
    if status=="approved":
        id_counter_str=str(id_counter)
        print(f"Approval refernce number{user_id}{id_counter_str[2:]}")
    else:
        print("")

main()
