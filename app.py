def calculate():
    valid_first_number = False
    while not valid_first_number:
        first_number = input("Enter first number: ")
        index1 = 0
        while index1 < len(first_number):
            if first_number[index1] in "1234567890.":
                valid_first_number = True
                index1 += 1
            else:
                valid_first_number = False
                index1 = len(first_number)
                print("Number invalid.")
    first_number = float(first_number)
    
    valid_operator = False
    while not valid_operator:
        operator = input("Input operator: ")
        if operator in "+-/*x":
            valid_operator = True
        else:
            print("Operator invalid.")
            
    valid_second_number = False
    while not valid_second_number:
        second_number = input("Enter second number: ")
        index2 = 0
        while index2 < len(second_number):
            if second_number[index2] in "1234567890.":
                valid_second_number = True
                index2 += 1
            else:
                valid_second_number = False
                index2 = len(second_number)
                print("Number invalid.")
    second_number = float(second_number)
    
    if operator == "+":
        print(first_number + second_number)
    elif operator == "-":
        print(first_number - second_number)
    elif operator in "*x":
        print(first_number * second_number)
    else:
        print(first_number / second_number)

while True:
    calculate()
    print("")
