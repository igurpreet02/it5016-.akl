def get_price(child, adult):
    child_price=10
    adult_price=25
    group_size=3
    group_rate=0.9

    cost=(child*child_price+adult*adult_price)

    if child+adult>group_size:
       cost=cost*group_rate
    return cost
def main():
    num_child=int(input("enter the number of childrens")) 
    num_adults=int(input("enter the nuber of adults"))   
    cost=get_price(num_child,num_adults)
    print("the cost of your tickets is : $"+str(cost))
main()