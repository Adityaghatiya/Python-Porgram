import time

def fact(n):
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i
        
    return(fact_n)
f=fact(5)
stime=time.time()
print(f)
etime=time.time()
total=etime-stime
print(total)
print("Required time will be",stime,etime)
