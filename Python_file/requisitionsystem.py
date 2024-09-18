"""
author- Gurpreet Singh
studentID= 20230782
Data Requisition sysytem (to collect data from staff , and item and its price , so manager can approved it or not according to the market )
"""

class Requisitionsystem:
    def __init__(self):
        print("printing requisition:")
        self.date=input("date:")
        self.staffname=input("please enter your name:")
        self.staffID=input('StaffID')
        self.requisitionid=1000
        self.product=[]
        self.total=0
        self.approved_request=500
        self.pending_request=1000
        self.not_approved=3500
        self.request=[] # list to store all request
    
    def colect_id(self):
        requisitionid=requisitionid+1
        print(f"requisitionalID: {self.requisitionid}")


    def Satff_info(self):
        self.staffID +=1

    def Requisitions_details(self):
        self.product=[]
        self.total=0
        while True:
            item=input("enter the item ('enter exit when finish)")
            if item.lower == 'exit':
                break
            price=float(input("enter the price of item"))
            self.product.append((item,price)) # to store both item and price as tuple
            self.total+=price
            
        self.referenceid=self.staffname[-3:] +str (self.staffID)[-3:] # to genetrate id
        self.Staff_info()
        return self.product, self.total, self.referenceid
    
    def Requisition_approval(self):
        if self.total<500:
            self.status='approved'
            self.approved_request +=1
        else:
            self.status='pending'
            self.pending_request +=1
        print(f"total:{self.total}")
        print(f"requsitation status{self.status}")


        request={
            "name": self.staffname,
            "total": self.total,
            "referenceid": self.referenceid,
            "status": self.status,
            "products": self.product
        }
        self.request.append(request) # add the request to the list
    
    def respond_requsition(self,manager_respond):
        if manager_respond.lower() =='approved':
            self.status ='approved'
        else:
            self.status='not approved'
            return self.status
        
    def display_requisition(self):
        if not self.request:
            print("no request has been subbited yet")
        else:
              print("-" * 30)
              print("       All Requests      ")
              print("-" * 30)
        for req in self.request:
                print(f"Name: {req['name']}, Total: ${req['total']}, "
                      f"Approval reference: {req['referenceid']}, Status: {req['status']}")
                print("-" * 30)
    def requisition_statistic(self):
        print(f'approved request{self.approved_request}')
        print(f"pending request {self.pending_request}")
        print(f"request not approved {self.not_approved}")

def main():
     system = Requisitionsystem()
     while True:

        choice = input("\n1. Submit Request\n2. Display Requests\n3. View Statistics\n4. Exit\nChoose an option: ")
        if  choice == "1":
            system.Requisitions_details()
            system.Requisition_approval()
        elif choice == "2":
            system.display_requisition()
        elif choice == "3":
            system.requisition_statistic()
        elif choice == "4":
            break
        else:
            print("invalid option, please try again")
            

if __name__ == "__main__":
 main()