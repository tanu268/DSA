# 01. Square Forest Pattern (N x N filled with '*')
# Example for n = 3:
# * * *
# * * *
# * * *
def square_forest(n: int) -> None:
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()


# 02. Right-Angled Star Triangle (Increasing '*')
# Example for n = 3:
# * 
# * * 
# * * *
def star_triangle(n: int) -> None:
    for i in range(n):
        for j in range(i + 1):
            print("*", end=" ")
        print()


# 03. Number Triangle (1 to i without space between numbers)
# Example for n = 3:
# 1
# 12
# 123
def number_triangle_nospace(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()


# 04. Repeating Number Triangle (i repeated i times with space)
# Example for n = 3:
# 1
# 2 2
# 3 3 3
def repeating_number_triangle(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(i):
            print(i, end=" ")
        print()


# To test any function individually, uncomment below lines:
# square_forest(3)
# star_triangle(3)
# number_triangle_nospace(3)
# repeating_number_triangle(3)
