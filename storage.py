import json

def save_model(layer, path="model.json"):
    data = {
        "classes": layer.classes,
        "weights": [layer.neurons[i].weights for i in range(len(layer.neurons))],
    }
    with open(path, "w") as f:
        json.dump(data, f)

def load_model(path="model.json"):
    with open(path, "r") as f:
        return json.load(f)