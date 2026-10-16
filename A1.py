#A1
voltage=float(input("Please enter the voltage:"))
resistance=float(input("Please enter the resistance:"))

if resistance>0:
    current=voltage/resistance
    print("the current is", current)
    if current>2:
        print("the fuse will blow")
    else:
        print("Circuit is safe")
else:
    print("invalid resistance")
