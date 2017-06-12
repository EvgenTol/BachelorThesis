'''
Diese Klasse wird aufgerufen, wenn der Nutzer Java  als Sprache wählt und Fibo als Original Klasse (in start.py)

Diese Klasse ist speziell auf die Fibo Klasse angepasst, wird also eine andere Klasse übergeben, so wird das Ergebniss nonsense

Wie vergleiche ich beide Programme? 
- !! die decompilierte Klasse muss noch compiliert werden
- zuerst mit random input fuzzen? und gucken wo die Ausgabe bei beiden programmen gleich ist?
- Metriken anwenden
- Laufzeit der beiden programme vergleichen (100 mal ausführen -> Durchschnittszeit berechnen
'''

import random # für fuzzing der eingaben
import os # zum compilieren der Decompilierten java Klasse
import sys
import subprocess # wird benötigt um auf die Java Funktionen zuzugreifen



def JavaFiboAnalyse(OriginalPath, DecompiledPath):
    CompileJava(OriginalPath)   # wird compiliert
    CompileJava(DecompiledPath) # original source geht, decompilierter nicht
    ExecuteAndGetOutput(OriginalPath)


def CompileJava(Path):
    Filepath = os.path.abspath(Path)
    os.system("javac " + Filepath) # funktioniert

def GetJavaFileName(Path):
    FileName = os.path.basename(Path)
    NameWOExtenshion = os.path.splitext(FileName)[0]
    return NameWOExtenshion

def ExecuteAndGetOutput(Path):
    NameOfFile = GetJavaFileName(Path)
    TerminalInput = os.system("java " + os.path.basename(Path) + " 10")
    output = subprocess.Popen(TerminalInput, stdout=subprocess.PIPE).communicate()[0]
    print(output)

def __init__(self):
    pass