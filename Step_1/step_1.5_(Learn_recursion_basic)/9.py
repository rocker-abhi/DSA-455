"""
    Print Fibonacci Series up to Nth term
"""

def fabo(n):
    initial_series = [0,1]
    
    for i in range(n):
        num = initial_series[-1] + initial_series[-2]
        initial_series.append(num)
    
    return initial_series

if __name__ == "__main__":
    number = 10
    print(fabo(number))    