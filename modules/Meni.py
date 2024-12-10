from .DijakClasses import Dijak, DijakHandler


def print_list(dijaki: list[Dijak]):
    for d in dijaki:
        print(d)


def get_input() -> int:
    try:
        i = int(input("Vpiši izbiro: "))
    except ValueError:
        i = -1
    print()
    return i


def run_menu(dijaki: list[Dijak]) -> None:
    while main_menu(dijaki):
        pass


def main_menu(dijaki: list[Dijak]) -> bool:
    print("1. Izpiši dijake")
    print("2. Izpiši sortirane dijake")
    print("3. Dodaj dijaka")
    print("4. Izbriši dijaka")
    print("5. Popravi dijaka")
    print("6. Izračunaj povprečje")
    print("0. Izhod")

    option = get_input()
    match option:
        case 0:
            return False
        case 1:
            print_list(dijaki)
        case 2:
            sort_menu(dijaki)
        case 3:
            dodaj_menu(dijaki)
        case 4:
            izbrisi_menu(dijaki)
        case 5:
            popravi_menu(dijaki)
        case 6:
            povprecje_menu(dijaki)
        case _:
            print("Vnesi veljavno izbirno!")

    for _ in range(3):
        print()

    return True


def sort_menu(dijaki: list[Dijak]) -> None:
    if len(dijaki) == 0:
        print("Ni nobenih dijakov za sortirati!")
        return

    print("Sortiraj po:")
    print("1. Po imenu")
    print("2. Po priimku")
    print("3. Po starosti")
    print("4. Po spolu")
    print("5. Po višini")
    print("6. Po teži")

    option = get_input()
    if not 1 <= option <= 6:
        print("Vnesi veljavno izbiro!")
        return

    def izbira_spol() -> int:
        print("Sortiraj po?:")
        print("1. Ženski spol")
        print("2. Moški spol")

        option = get_input()
        if option not in [1, 2]:
            return -1
        return option

    def izbira_padajoce() -> int:
        print("Sortiraj meni padajoče ali narastajoče?:")
        print("1. Padajoče ")
        print("2. Narastajoče")

        option = get_input()
        if option not in [1, 2]:
            return -1
        return option

    if option != 4:
        padajoce = izbira_padajoce()
    else:
        padajoce = izbira_spol()

    if padajoce == -1:
        print("Vnesi veljavno izbiro!")
        return

    dh = DijakHandler()
    match option:
        case 1:
            print_list(dh.by_ime(dijaki, True if padajoce == 1 else False))
        case 2:
            print_list(dh.by_priimek(dijaki, True if padajoce == 1 else False))
        case 3:
            print_list(dh.by_starost(dijaki, True if padajoce == 1 else False))
        case 4:
            print_list(dh.by_spol(dijaki, True if padajoce == 1 else False))
        case 5:
            print_list(dh.by_visina(dijaki, True if padajoce == 1 else False))
        case 6:
            print_list(dh.by_teza(dijaki, True if padajoce == 1 else False))


def dodaj_menu(dijaki: list[Dijak]) -> None:
    ime = input("Ime novega dijaka: ")
    priimek = input("Priimek novega dijaka: ")
    dh = DijakHandler()
    if dh.dijak_obstaja(dijaki, ime, priimek):
        print("Dijak s tem imenom in priimkom ze obstaja!")
        return

    print("Spol dijaka: ")
    print("1. Ženski spol")
    print("2. Moški spol")
    spol = get_input()
    if spol not in [1, 2]:
        print("Vnesi veljavno izbiro!")
        return
    spol = "ž" if spol == 1 else "m"

    temp_podatki = []
    try:
        temp_podatki.append(int(input("Starost novega dijaka: ")))

        visina = input("Višina novega dijaka: ").replace(",", ".")
        temp_podatki.append(float(visina))

        teza = input("Teža novega dijaka: ").replace(",", ".")
        temp_podatki.append(float(teza))
    except ValueError:
        print("Napačen format vnosa!")
        return

    for podatek in temp_podatki:
        if podatek < 0:
            print("Številski ne morejo biti manjši od 0!")

    try:
        dijaki.append(
            Dijak(ime, priimek, temp_podatki[0], spol, temp_podatki[1], temp_podatki[2])
        )
        print(f"Dijak {ime} {priimek} je bil uspešno dodan.")
    except AssertionError:
        print("Vnešen spol je napačen!")
    except Exception:
        print("Prišlo je do napake pri ustvarjanju dijaka!")


def izbrisi_menu(dijaki: list[Dijak]) -> None:
    if len(dijaki) == 0:
        print("Ni nobenih dijakov za zbrisati!")
        return

    ime = input("Ime dijaka: ")
    priimek = input("Priimek dijaka: ")
    dh = DijakHandler()
    if not dh.dijak_obstaja(dijaki, ime, priimek):
        print("Dijak s tem imenom in priimkom ne obstaja!")
        return

    for d in dijaki:
        if d.get_ime() == ime and d.get_priimek() == priimek:
            dijaki.remove(d)
            print(f"Dijak {ime} {priimek} je bil izbrisan!")
            return


def popravi_menu(dijaki: list[Dijak]) -> None:
    if len(dijaki) == 0:
        print("Ni nobenih dijakov za popraviti!")
        return

    ime = input("Ime dijaka za popravljanje: ")
    priimek = input("Priimek dijaka za popravljanja: ")

    dh = DijakHandler()
    if not dh.dijak_obstaja(dijaki, ime, priimek):
        print("Dijak s tem imenom in priimkom ne obstaja!")
        return

    print()
    print("Če ne želite spremeniti podatka, pustite vnos prazen!")
    print()

    nov_ime = input("Novo ime dijaka: ")
    nov_priimek = input("Nov priimek dijaka: ")

    print("Spol dijaka: ")
    print("1. Ženski spol")
    print("2. Moški spol")
    print("3. Ne spremeni")
    print("")
    spol = get_input()
    if spol not in [1, 2, 3]:
        print("Vnesi veljavno izbiro!")
        return
    match spol:
        case 1:
            spol = "ž"
        case 2:
            spol = "m"
        case 3:
            spol = ""

    try:
        starost = input("Starost novega dijaka: ").strip(" ")
        if starost != "":
            starost = int(starost)
            if starost < 0:
                print("Starost ne more biti negativna!")
                return

        visina = input("Višina novega dijaka: ")
        if visina != "":
            visina = visina.replace(",", ".")
            visina = float(visina)
            if visina < 0:
                print("Višina  ne more biti negativna!")
                return

        teza = input("Teža novega dijaka: ")
        if teza != "":
            teza = teza.replace(",", ".")
            teza = float(teza)
            if teza < 0:
                print("Teža ne more biti negativna!")
                return

    except ValueError:
        print("Napacen format vnosa!")
        return


    for d in dijaki:
        if d.get_ime() != ime or d.get_priimek() != priimek:
            continue

        if nov_ime != "":
            d.set_ime(nov_ime)
            
        if nov_priimek != "":
            d.set_priimek(nov_priimek)

        if spol != "":
            d.set_spol(True if spol == "ž" else False)

        if starost != "":
            d.set_starost(starost)

        if visina != "":
            d.set_visina(visina)

        if teza != "":
            d.set_teza(teza)

        break

    print(f"Dijak {ime} {priimek} uspešno spremenjen.")


def povprecje_menu(dijaki: list[Dijak]) -> None:
    if len(dijaki) == 0:
        print("Ni nobenih dijakov za izračunati povprečje!")
        return

    print("Izračunaj povprečje:")
    print("1. Višine")
    print("2. Starosti")
    print("3. Teže")

    option = get_input()
    if option not in range(1, 4):
        print("Vnesi ustrezno vrednost!")
        return

    print("Filtriraj po spolu?:")
    print("1. Ne")
    print("2. Moški")
    print("3. Ženski")
    spol = get_input()
    if spol not in range(1, 4):
        print("Vnesi ustrezno vrednost!")
        return

    if spol in [2, 3]:
        spol = "m" if spol == 2 else "ž"
    else:
        spol = ""

    dh = DijakHandler()
    match option:
        case 1:
            print(f"Povprečna višina: {dh.povprecna_visina(dijaki, spol):.2f} cm")
        case 2:
            print(f"Povprečna starost: {dh.povprecna_starost(dijaki, spol):.2f}")
        case 3:
            print(f"Povprečna teža: {dh.povprecna_teza(dijaki, spol):.2f} kg")
