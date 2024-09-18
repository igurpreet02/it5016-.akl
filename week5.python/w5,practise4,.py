def collect_user_data(id_counter):
    print("enter user information")
    username=input("name:")
    user_age=input("age:")
    user_email=input("email adress:")

    unique_id=id_counter + 1
    id_counter=unique_id

    print("user information:")
    print(f"name:{username}")
    print(f"age:{user_age}")
    print(f"email:{user_email}")
    print(f"unique_id:{id_counter}")
    return username,user_email,user_age,id_counter

#2
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
    
    #3
def categorize_request(total_amount):

    if total_amount<150:
        category="low"
        recommendation="proceed with potential discount"
    else:
        category="high"
        recommendation="review for potential discount"
    return category,recommendation

#4
def create_details_report(id_counter,username,user_age,useremail,total_amount,category,recommendation):
    print("detailed report")
    print(f"unique id:{id_counter}")
    print(f"username:{username}")
    print(f"age:{user_age}")
    print(f"email: {useremail}")
    print(f"total amount :$ {total_amount:.2f}")
    print(f"category:{category}")
    print(f"recommendation:{recommendation}")

def main():
    id_counter=5000
    id_counter,username,user_age,useremail=collect_user_data(id_counter)
    total_amount,items=caluculate_total_amount()
    category,recommendation=categorize_request(total_amount)
    create_details_report(id_counter,username,user_age,useremail,total_amount,category,recommendation)

main()