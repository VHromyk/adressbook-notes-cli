import pickle

def load_data(filename: str):
    with open(filename, "rb") as file:
        return pickle.load(file)