import subprocess
from os import linesep as endl

#return your seed_words
def seed_words():
    return {} #you may put your own seed words here
  
#copy to clipboard
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
#get next permutation
def nextPermutation( arr):
        bPoint, n = -1, len(arr)
        for i in range(n-2,-1,-1):
            if arr[i] >= arr[i+1]: continue                   # Skip the non-increasing sequence
            bPoint = i                                        # Got our breakpoint
            for j in range(n-1,i,-1):                         # again traverse from end
                if arr[j] > arr[bPoint]:                      # Search an element greater the element present at the breakPoint.
                    arr[j], arr[bPoint] = arr[bPoint], arr[j] # Swap it
                    break                                     # We just need to swap once
            break                                             # Break this loop too
        arr[bPoint+1:] = reversed(arr[bPoint+1:])
        return arr   
#get nth permutation:
def getPermutation( n: int, k: int):
        nums = [i for i in range(1,n+1)]
        ret = []       
        while(n):
            f = factorial(n-1)
            index = (k-1)//f 
            ret += [nums[index]]
            nums.remove(nums[index])
            n -= 1
            k %= f
        return ret

def factorial(n: int)->int:
    if n==0: return 1
    elif n==1: return 1
    else: return n*factorial(n-1)

#Function to find min or max of string in list
#Two aruguments for this function
#List should be passed first and 'min' or 'max' for query arguments.
#returns the length of string 
def minMaxLen( list, query ):
    if query == 'min':
        # using len() + key argument + min()
        len_result = len(min(list, key = len))
    elif query == 'max':
        # using len() + key argument + max()
        len_result = len(max(list, key = len))
    else:
        len_result = 0
    return len_result

#writing file function
def fileWrite( path, list ):
    # open file in write mode
    with open(r"{}".format(path), "w") as fp:
        for item in list:
            # write each item on a new line
            fp.write("%s\n" % item)
        print('Writing is done!')


# algorith to find permutation
def permu(a,n,k,i):
    if i==0:
        for j in range(n,n+k):
            print(a[j], end = ' ')
        print(endl)

    for j in range(0,n):
        a[j], a[n-1] = a[n-1], a[j]
        permu(a,n-1,k,i-1)
        a[j], a[n-1] = a[n-1], a[j]