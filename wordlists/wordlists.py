# importing sys
import sys

# adding Folder_2/subfolder to the system path
sys.path.insert(0, 'G:/metamask-bruteforce')

#'functions.py' is required to run this program
import functions as mf 

# -------------------------------------
# Program Starts from here
# ------------------------------------- 

#declaring empty lists
len3Lists = []
len4Lists = []
len5Lists = []
len6Lists = []
len7Lists = []
len8Lists = []

#opening wordlists file
with open("G:/metamask-bruteforce/wordlists/bip-0039-english.txt", "r") as wordlist:
    for line in wordlist:
        if len(line.strip()) == 3:
            len3Lists.append(line.strip())
            mf.fileWrite( path="G:/metamask-bruteforce/wordlists/len3Lists.txt", list = len3Lists )
        elif len(line.strip()) == 4:
            len4Lists.append(line.strip())
            mf.fileWrite( path="G:/metamask-bruteforce/wordlists/len4Lists.txt", list = len4Lists )
        elif len(line.strip()) == 5:
            len5Lists.append(line.strip())
            mf.fileWrite( path="G:/metamask-bruteforce/wordlists/len5Lists.txt", list = len5Lists )
        elif len(line.strip()) == 6:
            len6Lists.append(line.strip())
            mf.fileWrite( path="G:/metamask-bruteforce/wordlists/len6Lists.txt", list = len6Lists )
        elif len(line.strip()) == 7:
            len7Lists.append(line.strip())
            mf.fileWrite( path="G:/metamask-bruteforce/wordlists/len7Lists.txt", list = len7Lists )
        elif len(line.strip()) == 8:
            len8Lists.append(line.strip())
            mf.fileWrite( path="G:/metamask-bruteforce/wordlists/len8Lists.txt", list = len8Lists )
