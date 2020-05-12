najwieksza_liczba = -99999999
licznik = 0

while True:
    liczba = int(input("Wprowadź liczbę lub wpisz -1, aby zakończyć: "))
    if liczba == -1:
        break
    licznik += 1
    if liczba > najwieksza_liczba:
        najwieksza_liczba = liczba

if licznik != 0:
    print("Największa liczba wynosi", najwieksza_liczba)
else:
    print("Nie wprowadzono żadnej wartości.")


najwieksza_liczba = -99999999
licznik = 0

liczba = int(input("Wprowadź liczbę lub wpisz -1 aby zakończyć: "))

while liczba != -1:
    if liczba == -1:
        continue
    licznik += 1

    if liczba > najwieksza_liczba:
        najwieksza_liczba = liczba
    liczba = int(input("Wprowadź liczbę lub wpisz -1, aby zakończyć: "))

if licznik:
    print("Największa liczba wynosi", najwieksza_liczba)
else:
    print("Nie wprowadzono żadnej wartości.")

# Przykład przerwania

print("Instrukcja przerwania:")
for i in range(1, 6):
    if i == 3:
        break
    print("Wewnątrz pętli.", i)
print("Poza pętlą.")


# Przykład wznawiania

print("\nInstrukcja wznowienia:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Wewnątrz pętli.", i)
print("Poza pętlą.")
