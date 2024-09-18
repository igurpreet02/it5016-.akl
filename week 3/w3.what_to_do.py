def what_to_do_know():
    message="time to go to"
    prompt="enter selection(1,2or3):"
    user_choice=int(input(prompt))

    if user_choice==1:
       print(message,"time to go to gym")
    elif user_choice==2:
        print(message,"time to go to college")
    elif user_choice==3:
        print(message,"its time to go home") 
    else:
        print("incorrect selection")
what_to_do_know()