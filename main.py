from replit import clear

def sum(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1*n2

def divide(n1, n2):
  return n1/n2

operations = {
  "+" : sum,
  "-" : subtract,
  "*" : multiply,
  "/" : divide
}

def stop():
  print("Thank you, bye bye!")

def ask_again(n3):
  again = input("Stop, continue or restart?\n")
  if again.lower() == "continue":
    clear()
    print(f"Your previous result was: {n3}")
    ask(n3)
  elif again.lower() == "restart":
    clear()
    n1 = int(input("What is the first number? \n"))
    ask(n1)
  elif again.lower() == "stop":
    clear()
    stop()
  else:
    print("Invalid input")
    ask_again(n3)

def calc(n1, n2, operation): 
  print(f"The result of the calculation of {n1} {operation} {n2} is: {operations[operation](n1,n2)}")
  ask_again(operations[operation](n1,n2))
  return operations[operation](n1,n2)

def ask(n1):

  print("Which operation would you like to do? \n")
  for op in operations:
    print(f"{op}\n")

  operation = input("Write the operation symbol: ")
  
  n2 = int(input("What is the next number? \n"))

  calc(n1, n2, operation)

n1 = int(input("What is the first number? \n"))
ask(n1)
