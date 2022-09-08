# -------------------------------------
# Program Starts from here
# ------------------------------------- 

import os
from datetime import date
import rfunctions as rf

todays_date = date.today()
worldlist_path = "G:/metamask-bruteforce/wordlists/Raw/bip-0039-english.txt"
dump_file_name = "dump/dump_1.txt"
move_file_name = "check/check-1-{}.txt".format(todays_date)
end_time = "23:59:30"

while True: 
    os.system('cls')
    print(' Provide name of the file and time till \n when we want to run this script rest will be dumped on the file dump_x.txt\n \n type r to check dump_x.txt for repetation and avoid them \n type q and enter to quit\n')
    rf.main_get_all_words(worldlist_path, dump_file_name, move_file_name, end_time)