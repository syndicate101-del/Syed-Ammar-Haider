total_resistors=int(input("Please enter the total resistors"))
Rtotal=0

for x in range (1, total_resistors+1):
    count=int(input(f"Enter R{x}:"))
    Rtotal=count+Rtotal
print("The total resistance=", Rtotal,"Ohm")
    
