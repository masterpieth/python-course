def plus(a, b):
  return a + b

def minus(a, b):
  return a - b

def multiply(a, b):
  return a * b

def divide(a, b):
  return a / b

def negation(a):
  return -a

def power(a, b):
  return pow(a, b)

def remainder(a, b):
  return a % b
  
calculator = {
  "1" : plus,
  "2" : minus,
  "3" : multiply,
  "4" : divide,
  "5" : negation,
  "6" : power,
  "7" : remainder,
}

#if input is empty, return False
def check_input_is_empty(input):
  if bool(input):
    return input
  else:
    return False

#select menu: it will return menu number when user input vaild number
#if user input nothing, will return True for while loop keep looping in main()
#return False for stop looping in main() when user choose '0' which means quit menu
def select_menu():
  print("select menu.\n1.plus\n2.minus\n3.multiply \n4.divide\n5.negation\n6.power\n7.remainder\n0.quit")
  
  choice = check_input_is_empty(input())

  if choice == '0':
    return False
  elif choice == False:
    print("please select again")
    return True
  else:
    return choice

#convert str to int, if input is not int format it will return False
def str_to_int(input):
  try:
    input = int(input)
  except:
    return False
  else:
    return input

#format alert
def alert():
    print("please enter valid number")
  
#return input numbers in list format
def input_num_list(menu):

  flag = True
  input_num_list = []
  
  while(flag):
    print("input first number")
    a = input()

    if str_to_int(a) == False:
      alert()
      continue
    else:
      input_num_list.append(str_to_int(a))
      break
      
  while(flag):
    print("enter second number if needed(if not, just press enter)")
    b = input()

    if menu != "5" and len(b) == 0:
      print("input second number")
      continue
    elif len(b) == 0:
      flag = False
    elif str_to_int(b) == False:
      alert()
      continue
    else:
      input_num_list.append(str_to_int(b))
      flag = False
      
  return input_num_list

#main function
def main():
  
  flag = True
  result = 0
  
  while(flag):
    flag = select_menu()
    
    if type(flag) == bool:
      continue
    elif str_to_int(flag) == False:
      alert()
      continue
    else:
      list = input_num_list(flag)
      
      if len(list) == 1:
        result = calculator[flag](list[0])
      else:
        result = calculator[flag](list[0], list[1])
    print("Result:  " + str(result))

main()
