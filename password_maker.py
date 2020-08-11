import random
import string

password_list = []
###user input###
x = int(input("How many numbers and letters are there going to be? :"))

for i in range(0,x):
    val_list = random.randint(0,10)
    password_list.append(val_list)
    
    letters = string.ascii_lowercase

    for x in range(0,x):
        password_list.append(random.choice(letters))

k = random.sample(password_list,len(password_list))
k = [str(int) for int in k]
k = "".join(k)

print(k)