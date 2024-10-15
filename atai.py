
def atai_max(arr):
    mx = arr[0]
    for i in arr:
        if mx < i:
           mx = i
    return mx

def atai_min(arr):
   mn = arr[0]
   for i in arr:
     if mn > i:
       mn = i
   return mn
