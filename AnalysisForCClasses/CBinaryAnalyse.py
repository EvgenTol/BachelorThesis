'''
Die Klasse dinet dazu, die Binarys der beiden Programme zu vergleichen
Bei keinen Änderungen, wird die Höchstpunktzahl erreicht, bei unterschieden nicht
Vorgehen:
1)Compilieren der beiden Programme zu Binarys
2)Vergleich der Binarys
3)Definition der erreichten Punkte
'''


import os   #Zum Compilieren der Programme, zu Binarys

def CBinaryAnalye(pathOri, pathDec):
    print("--- Compiling the C Files to Binary ---")
    CompileToBinary(pathOri)
    CompareBinarys(pathDec)
    print("--- Compilation succesfull ---")


def getFileName(path):
    Filepath = os.path.abspath(path)
    return Filepath

def getBinaryName(path):
    OldName = getFileName(path)
    # remove .x extenshion and add a prefix

def CompileToBinary(path):
    CFileName = getFileName(path)
    os.system("gcc -o " + CFileName)
    pass



def CompareBinarys(file1, file2):
    pass