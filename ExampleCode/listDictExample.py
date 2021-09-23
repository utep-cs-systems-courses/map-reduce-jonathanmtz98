#!/usr/bin/env python3
import time
import pymp

# This exmaple shows how to create
# shared lists and shared dictionaries

def newListAndDict():
    # create a shared list
    listRet = pymp.shared.list()

    # create a shared dict
    dictRet = pymp.shared.dict()
    
    with pymp.Parallel() as p:
        # add thread number to list
        listRet.append(p.thread_num)

        # add the number of 'A's equal to the thread
        # number to the dictionary
        dictRet[str(p.thread_num)] = 'A' * p.thread_num

    return listRet, dictRet
        
def main():
    """
    main function for when running as a script
    """

    newList, newDict = newListAndDict()

    print(f'newList {newList}')
    print(f'newDict {newDict}')
    
if __name__ == '__main__':
    # execute only if run as a script
    main()

