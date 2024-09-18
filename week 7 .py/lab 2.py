class Whitecliffe:
    def __init__(self):
        self.studentID= int(input("enter the student ID:"))
        self.lname=input("enter the last name of the student:")
        self.program=input("enter the program (bachelor/diploma):")
        self.studentlist=[]
        self.memberfshipcounter=500
        self.withdrawnstudentcounter=200
        self.registeredstudentcounter=300
        self.bachelorstudents=250
        self.diplomastudents=250
    
    def Membership(self):
        self.studentlist.append((self.lname,self.studentID,self.program))
        self.memberfshipcounter += 1
        print(f"hi {self.lname}, your memebership ID is: {self.memberfshipcounter}")

        if self.program.lower()== "bachelor":
            self.bachelorstudents += 1
        elif self.program.lower() == "diploma":
            self.diplomastudents += 1
        else:
            print("unknown program. no student added to bachelors or diploma counts.")
    
    def withdrawal(self):
        student=(self.lname,self.studentID,self.program)
        if student in self.studentlist:
            self.studentlist.remove(student)
            self.withdrawnstudentcounter += 1
            self.registeredstudentcounter -= 1
            print(f" student {self.lname} has been withdrawn.")
        else:
            print("student not found in the system.")

        if self.program.lower() == "bachelor":
            self.bachelorstudents -= 1
        elif self.program.lower()== "diploma":
            self.diplomastudents -= 1

        print(f" registered students :{self.registeredstudentcounter}")
        print(f" withdrawn student: {self.withdrawnstudentcounter}")
    def statistics(self):
        print(f"nummber of registerd student : {self.registeredstudentcounter}")
        print(f"student in diploma program: {self.diplomastudents}")
        print(f"student in bachelors program: {self.bachelorstudents}")
        print(f"number of student who have withdrawn: {self.withdrawnstudentcounter}")


def main():
        system = Whitecliffe()
        while True:
            choice= input("\n1. new mwbwership \n2. withdraw memebership \n3.statistics \n4. exit\nchoose an option:")

            if choice == "1":
                system.Membership()
            elif choice == "2":
                system.withdrawal()
            elif choice == "3":
                system.statistics()
            elif choice == "4":
                print("exiting program...")
                break
            else:
                print("invalid option. please choose again.")

if __name__=="__main__":
    main()