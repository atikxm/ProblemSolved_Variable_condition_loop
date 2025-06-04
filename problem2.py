#User kichu number input dibe (1 theke N), 
# tumi loop diye total jog kore print korba.


n = int(input("Enter a number: "))
total=0

for i in range(1,n+1):
    total += i
print(f"Total sum: {total}")
