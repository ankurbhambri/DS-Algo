def fibonacci(n):
    if n <= 1:
        return n
    
    prev1, prev2 = 0, 1
    
    for i in range(2, n + 1):
        prev1, prev2 = prev2, prev1 + prev2
        
    return prev2

print(fibonacci(13))
print(fibonacci(7))
