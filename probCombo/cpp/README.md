CPP Method

cppprobCombo.o to generate permutations in the form of numbers. Or you can compile cppprobCombo.cpp file to generate as per your desire .o extension file. This approach is based on generating numbers and later, you can assign the strings based on the each string index. It will create without any duplication with unordered list.

Inputs:

    Changes the value inside of the int main().

    n: total number of values or entities you have to create permutation. If you have 2048 numbers, then you can set n = 2048.

    k: total number of combined permutation you want to generate. If you want to generate 12 total combinations from 2048 entities, then you can set k = 12.

    a[]: an array of the list of the total values or entities. If you want to generate permutations of 1,2,3,4,5 then, you can assign them in form of array, int a[] = {1,2,3,4,5}

Commands :

    ./a.out | tee >(split --additional-suffix=.log -d -l 1000000 - numcppProbCombo.0)

        use below command to save the output of the permutations generated from above file in the txt file. Yor console should support tee and split functions. This will auto generate files based on reaching specific lines of generation.

        -l : after this, you can set number of line to split the output file and save into the file. If you set 1000000 then, 1 million of lines will be written by generated permutation and next file will be generated. This process will go on until and unless you stop the console. 

        ./a.out : this is the output of the compile of the c++ file. Place here the compile file path.

        numcppProbCombo.0 : this is the auto generated file name to save the output of the console. You can change the file name here but make sure to set .0 at last to keep name ends with 0.