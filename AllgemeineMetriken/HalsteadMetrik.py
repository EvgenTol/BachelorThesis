'''
Diese Klasse berechnet die Halstead Kennzhalen, des übergebenen Programmes
Vorgehen:
1)Umwandeln der .c oder .class Datei in eine .txt Datei
2) Einlesen der .txt Datei
3) Scannen der .txt Datei nach den relevanten Keywords (mit regex?)
4) Zusammenfassung der Ergebnisse
5) Ausgabe der Ergebnisse in einer .txt Datei
'''
import math

SumDiffUsedOperatoren = 0     #n1, Anzahl der unterschiedlichen verwendendeten Operatoren
SumDiffUsedOperanden = 0        # n2, Anzahl der unterschiedlichen verwendeten Operanden

VokabularGröße = SumDiffUsedOperanden + SumDiffUsedOperatoren   # Summe von n1 und n2 ist die Vokubaluargröße

SumSameUsedOperatoren = 0 # N1, Anzahl der insgesamt verwendeten Operatoren
SumSameUsedOperanden = 0    # N2, Anzahl der insgesamt verwendeten Operanden

ImplementierungsLänge = SumSameUsedOperanden + SumSameUsedOperatoren # Implementierungslänge, ist die Summe von N1 und N2


def HalsteadLength(n1, n2):
    length = (n1* math.log(n1, 2)) + (n2 * math.log(n2, 2))
    return length

def HalsteadVolumen(N, n):
    vol = N * math.log(n, 2)
    return vol

# Der Aufwand beträgt, Schwierigkeit(Difficulty) * Halstead-Volumen
def Effort(diffi, volu):
    return diffi * volu

# Die Schwierigkeit (es zu schreiben oder zu verstehen)
def Difficulty(n1, n2, N2):
    difficulty = (n1/2) * (N2/n2)
    return difficulty

# Die Ziet, um das Programm zu schreiben, beträgt Effort / 18 sekunden
def TimeReqToProgramm(effort):
    return (effort/18)

# Das C Programm in bereitschaft bringen
# .c -> .txt
def setUp(file):
    pass

# Diese Methode soll, die Anzahl der unterschiedlichen verwendeten Operatoren ermittlen
def GetSumOFDiffOperatoren(file):
    pass

# Diese Methode soll, die Anzahl der unterschiedlichen verwendeten Operanden ermittlen
def GetSumOfDiffOperanden(file):
    pass

# Diese Methode soll, die Anzahl der insgesamt verwendeten Operatoren ermittlen
def GetSumOfSameOperatoren(file):
    pass

# Diese Methode soll, die Anzahl der insgesamt verwendeten Operanden ermitteln
def GetSumOfSmageOperanden(file):
    pass