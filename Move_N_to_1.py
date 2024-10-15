def neg(n):
    """
    Function to print numbers from n to 0 by adding 1 to n
    if n is negative.
    """
    while n <= 0:
        print(n)
        n += 1  # Increment n by 1

def pos(n):
    """
    Function to print numbers from n-1 to 0 by subtracting 1 from n
    if n is positive.
    """
    for i in range(n-1, -1, -1):
        print(i)

# Main execution starts here
n = int(input("Enter a number: "))

# Check if the number is negative or positive and call the respective function
if n < 0:
    neg(n)
else:
    pos(n)
