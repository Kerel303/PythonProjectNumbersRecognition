import tkinter as tk
from tkinter import simpledialog
import pixel_editor
import neuron
import neuron_layer


def recognize_callback(list):
    for row in list:
        print(row)

    editor.set_text("Działa")

def teach_callback():
    # Otwiera okienko z prośbą o wpisanie liczby (od 0 do 9)
    answer = simpledialog.askinteger(
        title="Klasyfikacja danych",
        prompt="Podaj wartość (jaką cyfrę narysowałeś?):",
        minvalue=0,
        maxvalue=9
    )

    # Sprawdzamy, czy użytkownik podał liczbę, czy kliknął "Cancel"
    if answer is not None:
        editor.set_text(f"Zapisano jako: {answer}")

        # Tutaj przekażemy answer do sieci, albo dopiero stworzymy nowy plik do uczenia się w następnym odpaleniu programu, jeszcze pomysłu nie mam
        
    else:
        editor.set_text("Anulowano uczenie")

if __name__ == '__main__':
    root = tk.Tk()
    editor = pixel_editor.Editor(root, recognize_callback=recognize_callback, teach_callback=teach_callback)
    root.mainloop()