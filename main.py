import tkinter as tk
from pathlib import Path
from tkinter import simpledialog
import pixel_editor
import neuron_layer
import sample
import random


classes = [i for i in range(0, 10)]
samples = []
layer = neuron_layer.NeuronLayer(classes, 32*32)
epochs = 200

train_data = []
test_data = []

def create_network():
    print(f"Klasy: {classes}")


def get_data():
    global train_data, test_data

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
                if len(vector) != 1024:
                    print(
                        f"Błąd pliku {i}-{j}.txt "
                        f"({len(vector)} zamiast 1024)"
                    )
                    continue
                print(f"Vector: {vector}")
                samples.append(sample.Sample(i, vector))
    random.shuffle(samples)
    split = int(len(samples)*0.8)
    train_data = samples[:split]
    test_data = samples[split:]


def train_network():
    print("Uczenie rozpoczęte")
    layer.train(train_data, epochs)

    print(f"Celność na treningowych: {layer.accuracy(train_data)*100:.2f}%") #:.2f oznacza aby dawał tylko dwa miejsca po przecinku ^^
    print(f"Celność na testowych: {layer.accuracy(test_data) * 100:.2f}%")  #:.2f oznacza aby dawał tylko dwa miejsca po przecinku ^^



def recognize_callback(data):
    sample_obj = sample.Sample(None, data)
    editor.set_text(layer.classify(sample_obj))

    # a potem do wypisania w konsoli
    results = layer.classify_all(sample_obj)

    print("Wyniki neuronów: ")
    for digit, score in results.items():
        print(f"{digit}: {score:.4f}")

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
            file.write(str(row))

if __name__ == '__main__':
    create_network()
    get_data()
    train_network()

    root = tk.Tk()
    editor = pixel_editor.Editor(root, recognize_callback=recognize_callback, teach_callback=teach_callback)
    root.mainloop()