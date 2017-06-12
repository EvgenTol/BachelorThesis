'''

Author: Evgen Tolstykh
Date: 05.06.2017

Ziel dieses Programmes ist es, zu bestimmen wie ähnlich sich zwei Programme sind.
Die Eingabe sind zwei (entweder C oder Java) Programme, wovon eins sich im Ordner befindet und das zweite die Dekompilierte
version ist. Die Ergebniss der Analyse soll in einer Textdatei gespeichert werden, wo die Ergebnisse näher betrachtet werden
können

Main Class:

Der Nutzer wird in der Main Funktion nach den Pfaden zu den beiden Programmen gefragt, zusätzlich wird er gefragt um welche
Sprache es sich handelt (c oder java) und welches Programm das original Programm ist (! die Originalprogramme sind vorgegeben)
Danch wird die zugehörige Analyse Klasse ausgerufen, welche dann das zugehörige Programm analysiert.
'''

import os   # Zum überprüfen ob der Pfad existiert
import sys  # Zum verlassen des programms und importieren der UnterOrdner benötigt
import AnalyseClassC    # Wird benötigt, falls die Programme in C geschrieben sind (MUSS UMGESCHRIBEN WERDEN)
from AnalyseClassJava import ChooseAnaylsisClass # wird aufgerufen, wenn die Codes in java geschriben sind

PATH_TO_ORIGINAL_FILE = ""  # Stores the path to the Original C File
PATH_TO_DECOMPILED_FILE = ""  # Stores the path to the decompiled C File
MODE = ""   # Which Language, was the Original Language?
CLASS_CASE = "" # which Original Source Code was Used?

# TODO: Input from User is evaluated, Fix it
# TODO If the User provides the Paths twice wrong, the programm still continues
def main():
    print("Welcome")
    print("------------")
    print("Please enter the path to the Original Sourcecode, if it's in the same directory as this Script, just enter the name of it")
    global PATH_TO_ORIGINAL_FILE
    PATH_TO_ORIGINAL_FILE = input("Please enter -> ")
    if os.path.exists(PATH_TO_ORIGINAL_FILE):
        print("File Found!")
    else:
        print("File does NOT EXISTS! Please re-enter it")
        PATH_TO_ORIGINAL_FILE = input(" -> ")

    print("Now please enter the Path to the decompiled Sourcecode")
    global PATH_TO_DECOMPILED_FILE
    PATH_TO_DECOMPILED_FILE = input("Please enter -> ")
    if os.path.exists(PATH_TO_DECOMPILED_FILE):
        print("File Found!")
    else:
        print("File does NOT EXISTS!, please re-enter it")
        PATH_TO_DECOMPILED_FILE = input(" -> ")

    print(" What Language was used? Currently Supporting only C and Java") # Frage welcher Modus gewählt wird
    MODE = input(" -> ")
    if (MODE.lower() != "c" and MODE.lower() != "java"): #Sollte eine falsche Eingabe vorhanden sein, erneuert Fragen
        MODE = input("Wrong language. Please enter either C or Java")
        MODE = input(" -> ")
    if MODE.lower() == "java":
        print("What Original Source was used? Currently supporting fibo , casting , ..")
        CLASS_CASE = input(" -> ")
        # Check if input is valid
    # get CLASS_CASE for C and check its input


    if MODE.lower() == "c": #Abhängig vom Modus, die jeweilige Klasse ausführen
        AnalyseClassC.Analyse(PATH_TO_ORIGINAL_FILE, PATH_TO_DECOMPILED_FILE)
    elif MODE.lower() == "java":
        ChooseAnaylsisClass(CLASS_CASE, PATH_TO_ORIGINAL_FILE, PATH_TO_DECOMPILED_FILE)



if __name__ == "__main__":
    sys.path.append("AnalysisForJavaClasses")
    sys.path.append("JavaCode")
    main()
