def fibonacci(n):
    if n <= 1:
        return n
    
    prev1 = 0
    prev2 = 1
    
    for i in range(2, n+1):
        curr = prev1 + prev2
        prev1 = prev2
        prev2 = curr
        
    return prev2

print(fibonacci(13))
print(fibonacci(7))
