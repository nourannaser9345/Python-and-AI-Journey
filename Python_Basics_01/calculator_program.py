Number1 = float(input("Please Enter your Calculs Number : ").strip())
Number2 = float(input("Please Enter your Calculs Number : ").strip())
Selection = input("Please Enter your math Opertion (+ , - , * , /) : ").strip()

if Selection == '+' :
    print(round(Number1 + Number2 , 3))
elif Selection == '-':
    print(round(Number1 - Number2 , 3))
elif Selection == '*':
    print(round(Number1 * Number2 , 3))
elif Selection == '/':
   print(round(Number1 / Number2 , 3))
else:
    print("Invalid Operator")
