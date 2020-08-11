import random
import string

password_list = []
###user input###
def password_maker(x):
    for i in range(0,x):
        val_list = random.randint(0,10)
        password_list.append(val_list)
    
    letters = string.ascii_lowercase

    for x in range(0,x):
        password_list.append(random.choice(letters))


password_maker(x = int(input("How long should the password be:")))
k = random.sample(password_list,len(password_list))
k = [str(int) for int in k]
k = "".join(k)



print(k)
