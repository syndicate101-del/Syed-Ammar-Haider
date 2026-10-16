
def loaded_divider(vs, r1, r2, rl):
    voltage= vs*r2/(r1+r2)
    rtotal= r2*rl/(r2+rl)
    vloaded= vs*rtotal/(r1+rtotal)
    return voltage,vloaded
print(loaded_divider(12,1000,1000,500))
