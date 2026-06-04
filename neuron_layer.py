import random

from neuron import Neuron
from utils import sample_generator


class NeuronLayer:
    def __init__(self, classes, input_size):
        if classes is None:
            raise ValueError(
                "Lista klas jest pusta. Anulowanie tworzenia warstwy neuronów"
            )

        self.classes = list(classes)
        self.input_size = input_size
        self.learning_rate = 0.01

        self.neurons = {}

        for c in self.classes:
            self.neurons[c] = Neuron(input_size, self.learning_rate)


    # Uczenie wszystkich neuronów w warstwie
    def train(self, data, epochs):
        if not data:
            raise ValueError("Lista danych jest pusta")
        if len(data[0]) != self.input_size:
            raise ValueError("Zły rozmiar wektora wejściowego")

        for _ in range(epochs):
            self.teach_neurons(data)

    def teach_neurons(self, data):
        shuffled = list(data)
        random.shuffle(shuffled)

        for sample in sample_generator(shuffled): # używamy generatora
            x = sample.get_input()
            label = sample.get_label()

            for c, neuron in self.neurons.items():
                if label == c:
                    y = 1.0
                else:
                    y = 0.0
                neuron.train(x, y)

    # Przewidywanie

    def classify(self, sample):
        x = sample.get_input()

        best_class = None
        best_score = float("-inf")

        for c, neuron in self.neurons.items():
            score = neuron.predict(x)

            if score > best_score:
                best_score = score
                best_class = c
        if best_class is None:
            raise RuntimeError("Nie udało się sklasyfikować danych dla tej klasy")

        return best_class

    def classify_all(self, sample):
        x = sample.get_input()


        # Do rozpisania bardziej po ludzku
        return {
            clazz: neuron.predict(x)
            for clazz, neuron in self.neurons.items()
        }


    # Określenie dokładności

    def accuracy(self, data):
        correct = 0

        for sample in data:
            if self.classify(sample) == sample.get_label():
                correct += 1

        return correct / len(data)

    # Gettery

    def get_classes(self):
        return self.classes

    def get_input_size(self):
        return self.input_size