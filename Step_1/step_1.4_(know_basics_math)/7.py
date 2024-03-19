"""
    check the prime number .
"""

number = int(input("Please enter the number : "))
is_a_prime = True

for i in range(2, number):
    if number%i == 0:
        print(i)
        is_a_prime = False
        break

if is_a_prime:
    print(f"This is a prime number .")
else:
    print("this is not a prime .") 