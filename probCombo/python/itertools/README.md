Itertools Method

This method will generate permutations from the python library called itertools and permutation. This will generate without any duplication with unordered list.

Inputs:

    totalLists: This holds all the data or entities you want to generate permutations from. You can assign it manually or link from the wordlists.

    itertools.permutations(totalLists, 12)]: On this line, you can change 12 number to x number as per your desire output of the combination you want to create. 

    with open("G:/metamask-bruteforce/probCombo/genProbCombo.txt", "w") as fp: On this line, give path where you want to create the filename and to save the output of the program.

    fp.write('\n'.join('{} {} {} {} {} {} {} {} {} {} {} {}'.format(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11]) for x in permut)): On this line, change the structure as per the output of the combinations. From above, there are 12 different combinations, so it has structured with 12 {} and x[0] to x[11].

Commands :

    run the program with command 
        python pyprobCombo.py

    