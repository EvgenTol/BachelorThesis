'''
Diese Klasse berechnet die Halstead Kennzhalen, des übergebenen Programmes

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




