import tkinter as tk
from pathlib import Path
from tkinter import simpledialog
import pixel_editor
import neuron
import neuron_layer
import sample


def train_network():
    print("Uczenie rozpoczęte")

    


def recognize_callback(list):
    for row in list:
        print(row)

    editor.set_text("Działa")

def teach_callback(data):
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
        create_file(answer, data)
        
    else:
        editor.set_text("Anulowano uczenie")



def create_file(class_of_sample, data):
    folder_path = Path(f"Data/{class_of_sample}")
    folder_path.mkdir(parents=True, exist_ok=True)
    how_many_files = sum(1 for x in folder_path.iterdir() if x.is_file())
    how_many_files += 1

    with open(f"{folder_path}/{class_of_sample}-{how_many_files}.txt", "w") as file:
        for row in data:
            for el in row:
                file.write(str(el))



if __name__ == '__main__':
    train_network()

    root = tk.Tk()
    editor = pixel_editor.Editor(root, recognize_callback=recognize_callback, teach_callback=teach_callback)
    root.mainloop()