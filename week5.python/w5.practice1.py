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

def main():
     id_counter=5000
     id_counter,username,user_age,user_email=collect_user_data(id_counter)
     
main()