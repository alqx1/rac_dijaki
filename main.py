from modules import Meni
from modules import FileHandler


def main():
    if not FileHandler.check_file("podatki/dijaki.csv"):
        print("Datoteka ne obstaja, program se bo zaprl.")
        return
    dijaki = FileHandler.read_from_file("podatki/dijaki.csv")

    Meni.run_menu(dijaki)

    FileHandler.write_into_file("podatki/dijaki.csv", dijaki)


if __name__ == "__main__":
    main()
