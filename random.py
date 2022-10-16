import random
import string

print("Ammount:")
amount = int(input("> "))

code = ('').join(random.choices(string.ascii_letters + string.digits, k=100000000))

print(code)

accounts = open("random.txt", "a")
accounts.write(code)
accounts.close