#User ekta name dibe. Tumi bolo oi nam er length even na odd.

name =(input("Enter Your name : "))
length = len(name)

if length %2== 0:
    print(f"Your name length is even ({length} letters).")
else:
    print(f"Your name length is odd ({length} letters).")