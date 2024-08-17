def sum(n):
    if (n<=1):
        return n
    else:
        return n + sum(n-1)
      
ans = sum(10)
print(ans)
