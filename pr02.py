x=input("\nEnter the N number")
y=input("\nEnter the K number")
z=list(str(a))
e=y
while e>0:
    e=e-1
    del(z[e])
print(''.join(z))
