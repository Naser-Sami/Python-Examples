
# number = int(input("Enter a Number: "))

# if number % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


def is_even_or_odd(number) -> bool:
    return "Even" if number % 2 == 0 else "Odd"

def is_even(number) -> bool:
    return number % 2 == 0

def is_odd(number) -> bool:
    return number % 2 == 1

print(is_even(10))
print(is_even(11))