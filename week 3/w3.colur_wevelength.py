def wavelength():
    colur=int(input("enter the nanometers"))
    if(colur>620 and colur<750):
        print(f"thank you, the wavelength that you enter is nanometer:{colur},your colur is red")
    elif(colur>590 and colur<620):
        print(f"thank you, the wavelength that you enter is nanometer:{colur},your colur is orange")
    elif(colur>570 and colur<590):
        print(f"thank you, the wavelenght that you enter is nanometer:{colur},your colur is yellow")
    elif(colur>495 and colur<570):
        print(f"thank you , the wavelength in nanometers is;{colur},your colur is green")
    elif(colur>450 and colur<495):
        print(f"thank you, the wavelength  in nanometer is:{colur}, your colur is blue")
    elif(colur>380 and colur<450):
        print(f"thank you, the wavelenght in nanometer is:{colur},your colur is voilet")
    else:
        print("out of order")
wavelength()


