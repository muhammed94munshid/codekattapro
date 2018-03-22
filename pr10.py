n = input()
ip = map(int,input().split(" "))
tot = 0
detect = []
for i in ip:
    if i > tot:
        detect.append(i)
    tot += i
    
print (sum(detect))
