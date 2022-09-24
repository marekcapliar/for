n=int(input("zadaj cislo: "))
x=0
for i in range(1,n+1):
    if i%4==0 and i%7==0:
        x+=1
print(x)
