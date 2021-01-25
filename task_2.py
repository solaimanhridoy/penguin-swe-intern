def efficientJanitor(n, weight):
    trips = []
    i = 0
    while i < n-1:
        if weight[i]+weight[i+1] <= 3.00:
            trips.append(weight[i]+weight[i+1])
            i+=2
        else:
            trips.append(weight[i])
            i+=1
        
    return len(trips)


# n = 4
# weight = [1.01, 1.991, 1.32, 1.4]

# n = 5
# weight = [1.01, 1.99, 2.5, 1.5, 1.01]

weight = []
n = int(input())
for i in range(1, n+1):
    weight.append(float(input()))

print(efficientJanitor(n, weight))