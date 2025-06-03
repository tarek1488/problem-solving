'''

---

**1. Parallel Processing**

A computer has a certain number of cores and a list of files that need to be executed. 
If a file is executed by a single core, the execution time equals the number of lines of code in the file.
If the lines of code can be divided by the number of cores, another option is to execute the file in parallel using all the cores,
in which case the execution time is divided by the number of cores. However,
there is a limit as to how many files can be executed in parallel. Given the lengths of the code files,
the number of cores, and the limit, what is the minimum amount of time needed to execute all the files?

For example, let's say that there are *n* = 5 files, where *files* = \[4, 1, 3, 2, 8]
\(indicating the number of lines of code in each file),
*numCores* = 4, and *limit* = 1. Even though both the first and fifth files can be executed in parallel,
you must choose only one of them because the limit is 1. The optimal way is to parallelize the last file,
so the minimum execution time required is 4 + 1 + 3 + 2 + (8/4) = 12. Therefore, the answer is 12.

'''





def minTime(files, numCores, limit):
    minTime = 0
    # Write your code here
    files.sort(reverse=True)
    for i in range(len(files)):
        if(limit != 0):
            if(files[i] % numCores == 0):
                minTime += files[i] / numCores
                limit -=1
                continue
        minTime += files[i]
    return int(minTime)
        
    
    