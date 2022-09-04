# -------------------------------------
# Program Starts from here
# ------------------------------------- 

# import itertools package
import itertools

#declaring empty lists
len3Lists = []
len4Lists = []
len5Lists = []
len6Lists = []
len7Lists = []
len8Lists = []

#opening wordlists file
#adding wordlists to variable
with open("G:/metamask-bruteforce/wordlists/Raw/len3Lists.txt", "r") as len3List:
    for line in len3List:
        len3Lists.append(line.strip())

with open("G:/metamask-bruteforce/wordlists/Raw/len4Lists.txt", "r") as len4List:
    for line in len4List:
        len4Lists.append(line.strip())

with open("G:/metamask-bruteforce/wordlists/Raw/len5Lists.txt", "r") as len5List:
    for line in len5List:
        len5Lists.append(line.strip())

with open("G:/metamask-bruteforce/wordlists/Raw/len6Lists.txt", "r") as len6List:
    for line in len6List:
        len6Lists.append(line.strip())

with open("G:/metamask-bruteforce/wordlists/Raw/len7Lists.txt", "r") as len7List:
    for line in len7List:
        len7Lists.append(line.strip())

with open("G:/metamask-bruteforce/wordlists/Raw/len8Lists.txt", "r") as len8List:
    for line in len8List:
        len8Lists.append(line.strip())

# combining all of lists
totalLists = len3Lists + len4Lists + len5Lists + len6Lists + len7Lists + len8Lists
print(totalLists)

#finding out permutation
permut = [p for p in itertools.permutations(totalLists, 12)]
print('Writing is on process! Please wait...')

#writing output to the file
with open("G:/metamask-bruteforce/probCombo/genProbCombo.txt", "w") as fp:
    fp.write('\n'.join('{} {} {} {} {} {} {} {} {} {} {} {}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11]) for x in permut))
    print('Writing is done!')
