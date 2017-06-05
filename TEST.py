import ctypes


# Funktioniert, ich kan die Main Methode aus dem C programm aufrufen, nachdem das C Programm manipuliert wurde, muss
# eine neue .so datei generiert werden
Libname = "HelloWorld.so"
Test = ctypes.CDLL(Libname)

Test.main()