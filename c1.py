def ohms_current(v,r):
    return v/r
def power_dissipated(I,r):
    return (I**2) * r

v=int(input("Enter the voltage"))
r=int(input("Enter the resistance"))

I=ohms_current(v,r)
P=power_dissipated(I,r)

print(f"the current is: {I}A")
print(f"the power dissipated is: {P}W")
