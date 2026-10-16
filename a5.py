#A5 smallest and largest resistor

R1=int(input("Enter resistor value"))
R2=int(input("Enter resistor value"))
R3=int(input("Enter resistor value"))

if R1<R2 and R1<R3:
    print("Smallest resistor is",R1,"Ohm")
elif R2<R1 and R2<R3:
    print("Smallest resistor is",R2,"Ohm")
elif R3<R1 and R3<R2:
    print("Smallest resistor is",R3,"Ohm")

if R1>R2 and R1>R3:
    print("Largest resistor is",R1,"Ohm")
elif R2>R1 and R2>R3:
    print("Largest resistor is",R2,"Ohm")
elif R3>R1 and R3>R2:
    print("Largest resistor is",R3,"Ohm")
