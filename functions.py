import subprocess
from os import linesep as endl

#copy to clipboard
def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)


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


# algorithm to find permutation
def permu(a,n,k,i):
    if i==0:
        for j in range(n,n+k):
            print(a[j], end = ' ')
        print(endl)

    for j in range(0,n):
        a[j], a[n-1] = a[n-1], a[j]
        permu(a,n-1,k,i-1)
        a[j], a[n-1] = a[n-1], a[j]