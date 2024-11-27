from .DijakClasses import Dijak
from csv import DictReader


def check_file(filepath: str) -> bool:
    try:
        file = open(filepath)
        file.close()
        return True
    except FileNotFoundError:
        return False


def read_from_file(filepath: str) -> list[Dijak]:
    dijaki = []

    with open(filepath) as file:
        reader = DictReader(file)
        for line in reader:
            try:
                d = Dijak(
                    line["ime"],
                    line["priimek"],
                    int(line["starost"]),
                    line["spol"],
                    float(line["visina"]),
                    float(line["teza"]),
                )
                dijaki.append(d)
            except ValueError:
                print("Napačen format podakov v datoteki, dijak ne bo dodan!")
    print(f"Datoteka {filepath} je bila uspešno prebrana.\n")
    return dijaki


def write_into_file(filepath: str, dijaki: list[Dijak]):
    with open(filepath, "w") as file:
        file.flush()
        file.write("ime,priimek,starost,spol,visina,teza\n")
        lines = [d.to_csv_format() + "\n" for d in dijaki]
        file.writelines(lines)
    print(f"Dijaki so bili uspešno zapisani v {filepath}.")
