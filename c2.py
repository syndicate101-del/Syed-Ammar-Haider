def parallel_resistance(r):
    rtotal=0
    rlen=len(r)
    for x in range (rlen):
        rtotal=rtotal+1/r[x]
    return 1/rtotal
R1=[10,10]
R2=[100,200,300]
c= parallel_resistance(R1)
v= parallel_resistance(R2)
print(c,"   ",v)
    
