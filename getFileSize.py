import os
import json
import sys
import errno
import datetime
from collections import OrderedDict
from operator import itemgetter

__author__ = "Hasan"


def getdisk():
    path = ''
    # validate if path is actually supplied
    try:
        path = sys.argv[1]
    except IndexError as indEx:
        if str(indEx) == 'list index out of range':
            print('Error ! Path not supplied, supply path after script name')
            sys.exit(1)

    # Directory validation
    try:
        os.chdir(path)
    except OSError as directoryEx:
        # in case direcory does not exist
        if directoryEx.errno == errno.ENOENT:
            print("The supplied path does not exist " + sys.argv[1])
            sys.exit(1)

        #if path supplied is not a directory
        if directoryEx.errno == errno.ENOTDIR:
            print("The path supplied is not a directory!")
            sys.exit(1)


    print('\nThe path is ', path)

    sizeDict = dict()

    for root, _, files in os.walk(path, topdown=True):
        '''
        Using topdown as True, 
        so that we get size of files
        which are present immediately in the mount point
        '''
        for name in files:
            try:
                #in case the file is being used by a process or not available for processing
                sizeDict[os.path.join(root, name)] = os.stat(os.path.join(root, name)).st_size
            except Exception as e:
                #print('Exception occured on this File, The execption is ->'+
                #      str(e),' ',os.path.join(root, name))
                sizeDict[str(os.path.join(root, name))] = 'Exception occured on this File, The execption is ->'+str(e)

    #sorting the dict by file size, so that file with biggest size is on top
    sizeDict = OrderedDict(sorted(sizeDict.items(), key = itemgetter(1), reverse = True))

    #using list of tuples, so that order is preserved to be used in orderedDict
    FinalDict = OrderedDict([('pathSupplied',path),
                            ('date_captured',str(datetime.datetime.now())),
                             ('files', sizeDict)])

    if len(FinalDict['files']) == 0:
        print('\nSupplied folder seems empty')

    #Wrirting the output to a file for later use
    with open('FileSizeDump.txt','a') as FileSizeDump:
        FileSizeDump.write(json.dumps(FinalDict, indent=4)+'\n\n\n')

    print('\nPrinting the json for temporary reference, '
           'json will be appended & dumped '
          'in a text file with the name FileSizeDump.txt')
    print(json.dumps(FinalDict, indent=4))

getdisk()
