def my_max(arr):
    mn = arr[0]
    for i in arr:
        if mn > i:
            mn = i
    return mn

def my_min(arr):
    mx = arr[0]
    for i in arr:
        if mx < i:
            mx = i
    return mx