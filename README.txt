# Rozpoznawanie cyfr przy pomocy sieci neuronowej na siatce 32 na 32

## Opis projektu

Program umożliwia rysowanie na siatce 32x32 piksele, w tym czyszczenie całej siatki.
Sieć neuronowa uczy się na podstawie zapisanych wcześniej przykładów i rozpoznaje narysowaną cyfrę.
Uczenie ma wpływ dopiero przy kolejnym włączeniu programu.

WAŻNE!:

Nie podawać błędnych odpowiedzi do narysowanych cyfr, bo program będzie miał gorszą celność, niż gdyby był losowym strzelaniem

Na podstawie podstawowych danych:
celność na danych treningowych: około 75-80%
celność na danych testowych: około 60% (6 razy lepiej niż przy losowym zgadywaniu)

Niestety byłem jedyną osobą która tworzyła dane testowe i stworzyłem zalewdie 500 cyfr, lecz aby miało sens więcej, potrzebowałbym więcej stylów pisma

# Rada
Dla zwiększenia celności liczbę powinno rysować się na środku wyznaczonej siatki


## Funkcje

- rysowanie cyfr
- rozpoznawanie cyfr
- dodawanie nowych przykładów uczących
- zapis modelu do JSON

## Uruchomienie

Uruchom:

python main.py