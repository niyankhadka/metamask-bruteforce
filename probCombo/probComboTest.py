# importing sys
import sys

# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'G:/metamask-bruteforce')

#this file 'functions.py' is in the same folder. it is required for this program to run
import functions as mf 

# -------------------------------------
# Program Starts from here
# ------------------------------------- 

# import itertools package
import itertools

n = 4 
k = 3
a = ['a','b','c','d']

# allwordlistTest = []

# with open("G:/metamask-bruteforce/wordlists/wordlistTest.txt", "r") as wordlistTest:
#     for line in wordlistTest:
#         allwordlistTest.append(line.strip())

# combining all of lists
#print(allwordlistTest)
#print("processing....")

mf.permu(a, n, k, k)

























# #declaring empty lists
# test3List = []
# test4List = []
# test5List = []
# test6List = []
# test7List = []
# test8List = []

# #opening wordlists file
# #adding wordlists to variable
# with open("G:/metamask-bruteforce/wordlists/test3.txt", "r") as test3:
#     for line in test3:
#         test3List.append(line.strip())

# with open("G:/metamask-bruteforce/wordlists/test4.txt", "r") as test4:
#     for line in test4:
#         test4List.append(line.strip())

# with open("G:/metamask-bruteforce/wordlists/test5.txt", "r") as test5:
#     for line in test5:
#         test5List.append(line.strip())

# with open("G:/metamask-bruteforce/wordlists/test6.txt", "r") as test6:
#     for line in test6:
#         test6List.append(line.strip())

# with open("G:/metamask-bruteforce/wordlists/test7.txt", "r") as test7:
#     for line in test7:
#         test7List.append(line.strip())

# with open("G:/metamask-bruteforce/wordlists/test8.txt", "r") as test8:
#     for line in test8:
#         test8List.append(line.strip())

# # combining all of lists
# totalTestlists = test3List + test4List + test5List + test6List + test7List + test8List
# print(totalTestlists)
# print("processing....")

# #finding out permutation
# permut = [p for p in itertools.permutations(totalTestlists, 12)]
# print("writing....")

# #writing output to the file
# with open("G:/metamask-bruteforce/probCombo/genProbCombo.txt", "w") as fp:
#     fp.write('\n'.join('{} {} {} {} {} {} {} {} {} {} {} {}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11]) for x in permut))
#     print('Writing is done!')













    

# totalList = [test1List, test2List, test3List]

# combList = list(map(list, product(test1List, repeat=3)))

# print('\n'.join(map(str, combList)))





# open file in write mode
# with open(r"G:/metamask-bruteforce/probCombo/genProbCombo.txt", "w") as fp:
#     for item in combList:
#         # write each item on a new line
#         fp.write("%s\n" % item)
#     print('Writing is done!')
