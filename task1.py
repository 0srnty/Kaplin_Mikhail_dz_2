def calculator():
    operator = input()
    if operator == '0':
        return "end"
    else:
        if operator in "+-*/":
            num_1 = int(input("1st num: "))
            num_2 = int(input("2nd num: "))
            if operator == '+':
                result = num_1 + num_2
                print(f"result {result}")
                return calculator()
            elif operator == '-':
                result = num_1 - num_2
                print(f"result {result}")
                return calculator()
            elif operator == '*':
                result = num_1 * num_2
                print(f"result {result}")
                return calculator()
            elif operator == '/':
                if operator != 0:
                    result = num_1 / num_2
                    print(f"result {result}")
                else:
                    print("wrong")
                return calculator()
        else:
            print("wrong")
            return calculator()


calculator()



