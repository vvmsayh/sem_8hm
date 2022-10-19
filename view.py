def get_name():
    with open("File1.txt", "r") as f:
        return str(f.readlines()[0]) 

def get_number():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[1])

def what_to_do():
    with open('file.txt', 'r') as f:
        return str(f.readlines()[2])


def export_book(book: dict):
    with open('newfile.txt','a') as newfile:
        for k, v in book.items():
            newfile.write(f"{k}, {v}")

def print_dict(book: dict):
    for k, v in book.items():
        print(f"{k}, {v}")