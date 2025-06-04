#Ekta program banao ja user er age input nie bujhte
#  parbe se minor, young, na senior.

age = int(input("Enter your age: "))

if age < 18:
    print("You are a Minor.")
elif 18 <= age < 50:
    print("You are a Young.")
elif 50 <= age < 65:
    print("You are a senior")
else:
    print("You are a Elder.")