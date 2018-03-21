n=int(input("number of players:"))
a=[]
ans=1
count=0
while(ans<=n):
	a.append(ans)
	ans=ans*2
for x in range(1,n+1):
	if x not in a:
		count=count+1
print(count)
