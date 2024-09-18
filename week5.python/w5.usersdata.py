def collect_user_data():
    id_counter=5000
    return id_counter+1

users_name=str(input("enter the users name"))
users_age=int(input("enter the users age"))
users_email=str(input("enter the users email"))
uniqueid=collect_user_data()
print("User Information:")
print(F"Name:{users_name}")
print(F"Age:{users_age}")
print(F"Email:{users_email}")
print(f"Unique ID:{uniqueid}")




