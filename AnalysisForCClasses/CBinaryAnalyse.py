'''
Die Klasse dinet dazu, die Binarys der beiden Programme zu vergleichen
Bei keinen Änderungen, wird die Höchstpunktzahl erreicht, bei unterschieden nicht
Vorgehen:
1)Compilieren der beiden Programme zu Binarys
2)Vergleich der Binarys
3)Definition der erreichten Punkte
'''


# TODO 1) diese Klasse muss getestet werden
# TODO 2) Punktesystem ausdenken (0-9 oder doch lieber 0-5?)
# TODO 3) Zum Thema Binarys informieren, wie sind die aufgebaut und wie Unterschieden die sich?


import os   #Zum Compilieren der Programme, zu Binarys
import subprocess # Zum Vergleich der beiden Binarys

Punkte = 0 # Die Punktzhal repräsentiert, wie ähnlich sich beide Binarys sind, eine 9 ist die höchstpunktzahl, eine 0 bedeutet, dass beide Programme komplett verschieden sind

def CBinaryAnalye(pathOri, pathDec):
    print("--- Compiling the C Files to Binary ---")
    OriBinary = CompileToBinary(pathOri)    # Compile the Original C File to a Binary
    DecBinary = CompileToBinary(pathDec)    # Compile the Decompiled C File to a Binary
    CompareBinarys(OriBinary, DecBinary)     # Compare the Binarys of both C Files
    print("--- Compilation succesfull ---")


def getFileName(path):
    Filepath = os.path.abspath(path)
    return Filepath


'''
Kann raus, oder? Funktionalität ist ja schon in der CompileToBinary Funktion
def getBinaryName(path):
    OldName = getFileName(path)
    # remove .x extenshion and add a prefix
'''

def CompileToBinary(path):
    CFileName = getFileName(path)   # Entferne den Pfad der Datei, zurücl bleibt nur der Name inkl. Endung
    NameOfBinary =  os.path.splitext(CFileName)[0]  # Entferne die Endung der Datei, also das .c
    NameOfBinary = NameOfBinary + ".bin"    # füge die Binary Endung hinzu
    os.system("gcc -o " + NameOfBinary + " " + CFileName) # Compiliert das C Programm zu einer Binary
    return NameOfBinary



def CompareBinarys(file1, file2):
    output = subprocess.check_output("diff " + file1 + " " + file2, shell=True)
    if output is None:
        Punkte = 9
        # generie die Ausgabedatei und verlasse das Programm
    else:   # Hier alle möglichen Fällen abklappern und die Punktzahl berechnen
        pass
