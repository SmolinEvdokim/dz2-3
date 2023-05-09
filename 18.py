n = int(input())   
a = list(map(int, input().split()))  
x = int(input())  

min_diff = abs(a[0] - x)  
result = a[0]  

for i in range(1, n):
    diff = abs(a[i] - x)   
    if diff < min_diff:
        min_diff = diff  # 
        result = a[i]  

print(result)   
