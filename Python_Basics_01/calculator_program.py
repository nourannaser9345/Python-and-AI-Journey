Number1 = int (input("Please Enter your Calculs Number : ").strip())
Number2 = int(input("Please Enter your Calculs Number : ").strip())
Selection = input("Please Enter your math Opertion (+ , - , * , //) : ").strip()

if Selection == '+' :
    print(Number1 + Number2 )
elif Selection == '-':
    print(Number1 - Number2)
elif Selection == '*':
    print(Number1 * Number2)
elif Selection == '//':
   print(Number1 // Number2)
else:
    print("Invalid Operator")
