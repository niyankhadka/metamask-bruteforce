# metamask-bruteforce

Commands:

    Running:

        CPP :
            cppprobCombo.o to generate permutations to numcppProbCombo
            ./a.out | tee >(split --additional-suffix=.log -d -b 10000000 - numcppProbCombo.1)