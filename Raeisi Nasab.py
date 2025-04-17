def calculator_emami():
    print("calculator app")
    
    while True:
        operation = input(" chosse a (+, -, *, /): ")
        
        if operation == "exit":
            print("exit at app.")
            break
        
        if operation not in ['+', '-', '*', '/']:
            print(" EROR!")
            continue
        
        try:
            num1 = float(input(" first number: "))
            if num1 ==""
            else 
            num2 = float(input("second number: "))
            
            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("EROR!")
                result = num1 / num2
                
            print("equal:", result)
        except ValueError:
            print("EROR!")
        except ZeroDivisionError as e:
            print(e)