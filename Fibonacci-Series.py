print ("-----Generate Fibonacci series using If statement & WHILE LOOP-----------")
n=int(input("How many numbers??? : "))
f1=0
f2=1
c=2
if n==1:
    print (f1)
elif n==2:
    print (f1,'\n',f2)
else:
    print (f1,'\n',f2)

while c<n:
    f=f1+f2
    print (f)
    f1,f2=f2,f
    c+=1
