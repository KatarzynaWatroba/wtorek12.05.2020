liczba_opuszczenia_petli = 42

licznik = 20

while licznik < liczba_opuszczenia_petli:
	print("W petli z licznikiem o wartosci: ", licznik)
	licznik = licznik + 1
	
	if licznik == 31:
		print("warunek brejkowy")
		break