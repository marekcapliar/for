n=int(input("zaciatok intervalu: "))
x=int(input("koniec intervalu: "))
y=0
for i in range(n,x+1):
    if i%8==0:
        y+=1
print(y)
