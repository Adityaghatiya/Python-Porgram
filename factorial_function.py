#It is used in import the permutation with factiorial
#Note:-It is used in another function
def fact(n):
    fact_n=1
    for i in range(1,n+1):
        fact_n*=i

    return(fact_n)
    
