import numpy as np

a = int(input("Podaj liczbe wierszy i kolumn"))

tab1 = np.random.randint(0,10, size=(a, a));
tab2 = np.random.randint(0,10, size=(a, a));
print("Tabela 1 i 2")
print(tab1, tab2)
print("Dodawanie 1 i 2")
print(tab1 + tab2)
print("Mnozenie 1 i 2")
print(np.multiply(tab1, tab2))