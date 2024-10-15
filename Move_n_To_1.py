def neg(n):
    while n <= 0:
        print(n)
        n += 1

def pos(n):
    for i in range(n-1, -1, -1):
        print(i)

# Test the functions
n = int(input("Enter a number: "))
if n < 0:
    neg(n)
else:
    pos(n)

