'''

This Class starts the Analysis. First it retrieves the name of the Original C File and the Decomlied C File
From the Path, provied by the User, then it creates a shared libraray from the Decompiled File, which can be accessed with
Ctyped. 

'''

import ctypes    # use this module to call C Functions in Python
import start    # for the Path variables
import os   # for the terminal calls
import subprocess

'''
This Method should start the Analysis
'''
def Analyse(OriFilePath, DecFilePath):
    print("-- Creating Shared Librarys from the C Files --")
    # Creates for both C Files (Original Cile and Decompiled File) a shared libraray which can be accessed with ctyüed
    NameOfOriginalFile = CreateLibrary(OriFilePath) # Name of the Shared Library, of the original C File
    NameOfDecompiledFile = CreateLibrary(DecFilePath) # Creates a .so Library and gets the Name of the Decompiled File
    print("-- Importing the Shared Librarys into Python --")
    OriginalLib = ctypes.CDLL(NameOfOriginalFile)
    DecompiledLib = ctypes.CDLL(NameOfDecompiledFile)
    print("-- Librarys are ready to use --")
    OriginalLib.main()


'''
Functions takes the path to a C file as Argument and compiles it to a .so Libary, for using it in Python, with the ctypes lib
Returns the Name of the .so File
'''
def CreateLibrary(path):

    FileName = os.path.basename(path)

    LibName = os.path.splitext(FileName)[0] # split the name of the .C file into the name and the file extenshion
    LibName = "Lib" + LibName + ".so" #

    os.system("gcc -shared -o " + LibName + " -fPIC " + FileName) # creates a .so File from the .C file

    return LibName

