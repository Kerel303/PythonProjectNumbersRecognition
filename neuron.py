import math
import random

class Neuron:
    def __init__(self, input_size, learning_rate):
        self.bias = (random.random() * 2)-1
        self.learning_rate = learning_rate
        self.weights = []
        for i in range(input_size):
            self.weights.append((random.random() * 2)-1)

    # Funkcja aktywacji

    def sigmoid(self, x):
        if x >= 0:
            z = math.exp(-x)
            return 1.0/(1.0+z)
        else:
            z = math.exp(x)
            return z/(1.0+z)

    # Predykcja

    def predict(self, data):
        if(len(data) != len(self.weights)):
            raise ValueError(
                f"Spodziewano się {len(self.weights)} wejść, otrzymano {len(data)}"
            )

        weighted_sum = 0

        for i in range(len(self.weights)):
            weighted_sum += self.weights[i] * data[i]

        weighted_sum += self.bias

        return self.sigmoid(weighted_sum)

    # Klasyfikacja

    def classify(self, data):
        if self.predict(data) >= 0.5:
            return 1
        else:
            return 0

    # Uczenie neuronu

    def train(self, data, real_answer):
        output = self.predict(data)
        error = output - real_answer

        delta = error * output * (1-output)

        for i in range(len(self.weights)):
            self.weights[i] -= self.learning_rate * delta * data[i]

        self.bias -= self.learning_rate * delta


