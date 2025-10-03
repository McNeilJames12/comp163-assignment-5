print("=== Challenge 1: Collatz Conjecture ===")

current_number = int(input("Enter starting number: "))
print(f"Sequence: {current_number}", end="")
steps = 0
while current_number != 1:
    if current_number % 2 == 0:
        current_number = current_number // 2
    else:
        current_number = current_number * 3 + 1
    steps+=1
    print(" ", end="")
    print(current_number, end="")
print()
print(f"Steps: {steps}")
print()

# challenge 2
print("=== Challenge 2: Prime Number Checker ===")
n = int(input())
print(f"Enter a number: Testing divisors from 2 to {n - 1}...")
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime (divisible by 3)")
            break
    else:
        print(f"{n} is prime!")
print()
