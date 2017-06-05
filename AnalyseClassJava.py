'''
Diese Klasse ist für den Zugriff auf die Java Funktion und Bestandteile zuständig.
Die Java Programme müssen importiert werden und dann sollen die Klassen des Original Codes mit dem dekompilierten Verglichen werden

Da die Original Codes wahrscheinlich in verschiedene "Disziplinen" aufgeteielt werden, wird diese Klasse als eine Art
"Startklasse" fungieren, die dann die zugehörigen Analyse Klassen aufruft.

Analyse Klassen: Fibo, Casting und mehr (folgt)
'''

import start
import AnalysisForJavaClasses   # Package wo alle Java Analyse Klassen sind


def ChooseAnaylsisClass(): # TODO Parameter hinzufügen
    if start.CLASS_CASE.lower() == "fibo":
        AnalysisForJavaClasses.JavaFiboAnalyse()   # Wenn der User Fibo als CLASS_CASE angibt, so wird die JavaFiboAnalyse Klasse ausgerufen
    elif start.CLASS_CASE.lower() == "casting":
        AnalysisForJavaClasses.JavaCastingAnalyse()