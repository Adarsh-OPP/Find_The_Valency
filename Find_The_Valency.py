atomic_number = int(input("Enter the atomic number: "))
x= atomic_number - 2
o = 0
while True:
    if x >= 8:
       x = x-8
    else:
        break
if(x > 4):
    x=8 - x
    print("Valency is",x)
else:
    print("Valency is",x) 






