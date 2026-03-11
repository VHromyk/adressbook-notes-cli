import pickle


def save_data(book, filename: str) -> None:
    with open(filename, "wb") as file:
        pickle.dump(book, file)