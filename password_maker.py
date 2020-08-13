import random
import string


###user input###
x = int(input("How many numbers is there going to be? :"))
y = int(input("How many letters are there going to be? :"))
c = int(input("How many Capital letters are there going to be? :"))

###lists###
letters_low = string.ascii_lowercase
letters_up = string.ascii_uppercase
var_list = []
password_list = []

def password():
  if x==0 and y==0 and c==0:
    pass
  for i in range(0,x):
    if x==0:
      pass
    var_list.append(random.randrange(10))

  for i in range(0,y):
    if y==0:
      pass
    password_list.append(random.choice(letters_low))
  
  for i in range(0,c):
    if c==0:
      pass
    password_list.append(random.choice(letters_up))
   
password()

password_list.extend(var_list)
random.shuffle(password_list)
password_list = [str(int) for int in password_list]
password_list= "".join(password_list)
print("Your password is {} !".format(password_list))