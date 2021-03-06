/*******************************
    project: StudentVM_beta
    author: Alex Semin
    place: SPbU MM171
    date:  2013
*******************************/

#include <stdio.h>
#include <string.h>
#include <time.h>

#include "vm.h"


int main(int argc, char **argv)
{
    const unsigned int maxDirectiveLen = 2;
    unsigned int sizeOfMemory = maxMemorySize;
    int i = 0;
    char *param;
    char *fileName;
    time_t timeStart = time(NULL);
    time_t timeEnd = timeStart;

    for (i = 0; i < argc; ++i)
    {
        param = argv[i];
        if (strlen(param) > 1 && strlen(param) <= maxDirectiveLen && *param == '-')
        {
            if (param[1] == 'm')
            {
                sizeOfMemory = (unsigned int) atoi(argv[++i]);
            }
            else if (param[1] == 'f')
            {
                fileName = argv[++i];
            }
        }
    }
    runVM(fileName, sizeOfMemory);
    timeEnd = time(NULL);
    printf("Time of executing (%0.10g sec)\n", difftime(timeEnd, timeStart));
    return 0;
}

