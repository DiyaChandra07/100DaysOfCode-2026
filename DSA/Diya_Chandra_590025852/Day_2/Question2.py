def largest(arr):
    max_val=arr[0]
    for i in arr:
        if i > max_val:
            max_val = i
    return max_val

print(largest([24,52,13,24,66,42,2,4,6,7,33,4,56,100,23,45,67,89,90]))
