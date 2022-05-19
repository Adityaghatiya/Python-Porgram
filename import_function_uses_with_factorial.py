#permutation and combination with import
import factorial_function as f
n=int(input("Enter the required n: "))
r=int(input("Enter the required r: "))
fn=f.fact(n)
fr=f.fact(r)
p=fn/fr
print("Thus the required factorial be",p)
