#import time # LINIA I

# Napisz pętlę for, która liczy do pięciu.
    # Ciało pętli: wyświetl w oknie konsoli numer iteracji i słowo "Mississippi".
   # time.sleep(1) # LINIA II

# Napisz funkcję print, która wyświetli wiadomość końcową.
#i = Missisipi

'''Scenariusz

Czy wiesz, czym jest Mississippi? Cóż, to nazwa jednego ze stanów i rzek w Stanach Zjednoczonych. Rzeka Mississippi ma około 2340 mil długości, co czyni ją drugą najdłuższą rzeką w Stanach Zjednoczonych (najdłuższą jest rzeka Missouri). Jest tak długa, że jedna kropla wody potrzebuje 90 dni, aby przepłynąć ją całą od źródła do ujścia!

Słowo Mississippi jest również używane do nieco innego celu: do tzw. liczenia Mississippi.

Jeśli nie znasz tego sposobu liczenia, nie przejmuj się - już wyjaśniamy: otóż liczenie Mississippi jest używane w Stanach Zjednoczonych do liczenia czasu, a konkretniej - sekund.

Ideą jest dodanie słowa Mississippi do liczby przy odliczaniu sekund na głos, co sprawia, że długość wypowiadanej frazy zbliża się do faktycznej długości sekundy, w związku z tym wypowiedzenie na głos "one Mississippi, two Mississippi, three Mississippi" zajmie w przybliżeniu rzeczywiste trzy sekundy! Metoda ta jest często używana przez dzieci bawiące się w chowanego, aby mieć pewność, że poszukujący liczy w sposób uczciwy.

Twoje zadanie jest bardzo proste: napisz program, który używa pętli for do liczenia w ten sposób - do liczby pięć. Po policzeniu do pięciu, program powinien wyświetlić na ekranie końcową wiadomość "Ready or not, here I come!", co można bardzo niezobowiązująco przetłumaczyć jako "Szukam!".

'''
import time
#for i in range (2, 6, 1):
nazwy_cyfr = ["one", "two", "three", "four", "five"]
print(nazwy_cyfr[1])
for i in range(			5):
    print(nazwy_cyfr[i] ,  "Missisipi")
    time.sleep(3)
print("redy or not, here i come!")
