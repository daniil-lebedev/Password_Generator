import random
import string
import time


"""function to take user input"""
def takeInput():
  #making inout global
  global x
  x = int(input("How many numbers is there going to be? :"))
  global y
  y = int(input("How many letters are there going to be? :"))
  global c
  c = int(input("How many Capital letters are there going to be? :"))
  if y==0 and x==0 and c==0:
    print("You gotta input a number in order to generate a password! Let's try again.")
    takeInput()
  ###lists###
  letters_low = string.ascii_lowercase
  letters_up = string.ascii_uppercase
  var_list = []
  password_list = []
  password_list.append(random.choice(letters_up))

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
  ###final stuff###
  password_list.extend(var_list)
  random.shuffle(password_list)
  password_list = [str(int) for int in password_list]
  password_list= "".join(password_list)
  print("Your password is {} !".format(password_list))

"""function to check the password"""
def checkPassword():
  #taking user input
  checking_passowrd = input("Type the password here: ")
  
  #checking the length of the password
  if len(checking_passowrd)<=5:
    print("The password is really short.")
  elif len(checking_passowrd)>5 and len(checking_passowrd)<=10:
    print("The length is ok.")
  elif len(checking_passowrd)>10:
    print("The length is good.")

"""function to decide what user wants to do"""
def start():
  print("Welcome user, what would u like to do?")
  time.sleep(2)
  print("To check password type 1")
  time.sleep(2)
  print("To create password type 2")
  taking_input = int(input("Type it here: "))
  
  #processing user request
  if taking_input == 1:
    checkPassword()
  else:
    takeInput()
start()








