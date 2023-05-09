n = int(input())  
a = list(map(int, input().split()))   
x = int(input())   

count = 0   
for i in range(n):
    if a[i] == x:
        count += 1

print(count)   
