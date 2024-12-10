from modules import Meni
from modules import FileHandler


def main():
    if not FileHandler.check_file("dijaki.csv"):
        print("Datoteka za branje dijakov ne obstaja, program bo to datoteko ustvaril.")
        with open("dijaki.csv", "w") as file:
            file.write("ime,priimek,starost,spol,visina,teza")
    dijaki = FileHandler.read_from_file("dijaki.csv")

    Meni.run_menu(dijaki)

    FileHandler.write_into_file("dijaki.csv", dijaki)


if __name__ == "__main__":
    main()
