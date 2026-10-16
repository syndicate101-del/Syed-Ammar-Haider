R1=0
R5=0
Rr=0

x= float(input("Enter the resistance(0 to stop)"))

while x!=0:
    if 99<=x<=101.0:
        R1+=1
    elif 95.0<=x<=105.0:
        R5+=1
    else:
        Rr+=1
    x=float(input("Enter the resistance(0 to stop)"))

print("1% tolerance:", R1)
print("5% tolerance", R5)
print("Rejected:", Rr)
