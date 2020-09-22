import random


def recur_method(count, numb):
    print(f"try №{count}")
    answer = int(input("input: "))
    if count == 10 or answer == numb:
        if answer == numb:
            print("correct")
        print(f"number: {numb}")
    else:
        if answer > numb:
            print(f"number less then {numb}")
        else:
            print(f"number more then {numb}")
        recur_method(count + 1, numb)


recur_method(1, random.randint(0, 100))