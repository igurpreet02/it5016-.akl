""""
task 1: staff info
author =Gurpreet  Singh
"""

def staff_info(unique_id):
    print("printing staff information") 
    dates=input("enter the date")
    id=input("enter the staff id")
    name=input("enter the name of staff")

    requisition_id = unique_id + 1
    unique_id = requisition_id

    print("printing staff information:")
    print(f"Date:{dates}")
    print(f"Staff ID:{id}")
    print(f"Staff Name:{name}")
    print(f"Requisition ID:{requisition_id}")
    return dates,id,name,requisition_id

def main():
    requistion_id=10000
    requistion_id,dates,id,name=staff_info(requistion_id)
main()
