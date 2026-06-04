class Sample:
    def __init__(self, class_of_sample, data):
        self.class_of_sample = class_of_sample
        self.data = data

    def __len__(self):
        return len(self.data)

    def get_input(self):
        return self.data

    def get_label(self):
        return self.class_of_sample