
def star_to_delta(a,b,c):
    k=a * b + b * c + c * a
    x=k / c
    y=k / a
    z=k / b
    return x, y, z

print(star_to_delta(10, 20, 30))
