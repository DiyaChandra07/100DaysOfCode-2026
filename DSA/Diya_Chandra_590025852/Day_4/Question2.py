def rotateArr(arr, k):
    k = k % len(arr)
    arr[:] = arr[-k:] + arr[:-k]

rotateArr([1,2,3,4,5,6,7], 3)