"""
    Introduction to Recursion – Understand Recursion by printing something N times
"""

def recursion(number):
    print(f"{number} : hello learners ")
    if number == 0 :
        return
    return recursion(number-1)

if __name__ == "__main__":
    # This is the driver code
    recursion(24)