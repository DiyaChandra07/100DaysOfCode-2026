def noOfOccurences(arr,target):
    count=0
    for i in arr:
        if i==target:
            count+=1
    return count

print(noOfOccurences([1,2,3,3,4,5,2,3,6,7,3,6,2,2,2,7,2,4,2,9],2))