
# Python program to display the Fibonacci sequence using a WHILE loop

num_1 = int(input("How many sequences do you want the algorithm to complete?"))
while num_1 <= 0:
    print("ERROR. Please enter a positive number.")
    num_1 = int(input("How many sequences do you want the algorithm to complete?"))

print("How many sequences are gonna be shown?", num_1)
a, b = 0, 1
i = 0
if num_1 > 0:
    print("Fibonacci sequence: ")
    while (i < num_1):
        fib = a + b
        print(a)
        a = b
        b = fib
        i += 1

# Python program to display the Fibonacci sequence using RECURSION

num_2 = int(input("How many sequences do you want the algorithm to complete?"))

def fib_recur(num_2):
    if num_2 <= 1:
        return(num_2)
    else:
        return(fib_recur(num_2-1) + fib_recur(num_2-2))

j = 0   
while num_2 <= 0:
    print("ERROR. Please enter a positive number.")
    num_2 = int(input("How many sequences do you want the algorithm to complete?"))
else:
    print("How many sequences are gonna be shown?", num_2)
    print("Fibonacci sequence:")
    while j < num_2:
        print(fib_recur(j))
        j += 1
