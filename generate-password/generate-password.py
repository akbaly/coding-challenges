print("This program creates a random password from a given full name")
name = input("Please enter your full name (without any spaces): ").lower()
list_name = list(name)
import random
result = ""
k = 1
while k < 8:
    if k < 4:
        i = random.randint(0, (len(list_name) - 1))
        result += list_name[i]
    else:
        randomnumber = str(random.randint(0,9))
        result += randomnumber
    k += 1
print(result)






