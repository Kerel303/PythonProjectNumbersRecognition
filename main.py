import tkinter as tk
from pathlib import Path
from tkinter import simpledialog
import pixel_editor
import neuron_layer
import sample


classes = [i for i in range(0, 10)]
samples = []
layer = neuron_layer.NeuronLayer(classes, 32*32)
epochs = 200

def create_network():
    print(f"Klasy: {classes}")


def get_data():
    print("Wczytywanie danych: ")
    for i in range(0, 10):
        folder_path = Path(f"Data/{i}")
        folder_path.mkdir(parents=True, exist_ok=True)
        how_many_files = sum(1 for x in folder_path.iterdir() if x.is_file())
        for j in range(1, how_many_files+1):
            with open(f"{folder_path}/{i}-{j}.txt", "r") as file:
                data = file.read()
                print(f"{i}-{j}:{data}")
                vector = [int(x) for x in data.strip()]
                print(f"Vector: {vector}")
                samples.append(sample.Sample(i, vector))






def train_network():
    print("Uczenie rozpoczęte")
    layer.train(samples, epochs)



def recognize_callback(list):
    for row in list:
        print(row)

    # editor.set_text("Działa")
    sample_obj = sample.Sample(None, list)
    editor.set_text(layer.classify(sample_obj))

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

        # Tutaj dopiero stworzymy nowy plik do uczenia się w następnym odpaleniu programu
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
    create_network()
    get_data()
    train_network()

    root = tk.Tk()
    editor = pixel_editor.Editor(root, recognize_callback=recognize_callback, teach_callback=teach_callback)
    root.mainloop()