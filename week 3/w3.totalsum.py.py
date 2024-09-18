def function1(n1, n2, n3):
    sum_value = n1 + n2 + n3  # Fix the sum calculation
    minimum = min(n1, n2, n3)
    return sum_value - minimum

n1 = int(input("number1: "))
n2 = int(input("number 2: "))
n3 = int(input("number3: "))
print(function1(n1, n2, n3))
