def magnitude_descriptors():
    magnitude=float(input("enter the magnitude of earth"))

    if (magnitude<2.0):
        print("micro")
    elif(magnitude>2.0 and magnitude<3.0):
         print("very minor")
    elif(magnitude>3.0 and magnitude<4.0):
         print("minor")
    elif(magnitude>4.0 and magnitude<5.0):
         print("light")
    elif(magnitude>5.0 and magnitude<6.0):
         print("moderate")
    elif(magnitude>6.0 and magnitude<7.0):
         print("strong")
    elif(magnitude>7.0 and magnitude<8.0):
         print("major")
    elif(magnitude>8.0 and magnitude<10.0):
         print("great")
    else:
        print("meteroic")
magnitude_descriptors()     