class Dijak:
    def __init__(
        self,
        ime: str,
        priimek: str,
        starost: int,
        spol: str,
        visina: float,
        teza: float,
    ):
        self._ime = ime
        self._priimek = priimek
        self._starost = starost
        assert spol in "mž"
        self._spol = spol
        self._visina = visina
        self._teza = teza

    # getters
    def get_ime(self) -> str:
        return self._ime

    def get_priimek(self) -> str:
        return self._priimek

    def get_starost(self) -> int:
        return self._starost

    def get_spol(self) -> str:
        return self._spol

    def get_visina(self) -> float:
        return self._visina

    def get_teza(self) -> float:
        return self._teza

    # setters
    def set_starost(self, starost: int) -> None:
        self._starost = starost

    def set_spol(self, moski: bool) -> None:
        self._spol = "m" if moski else "ž"

    def set_visina(self, visina: float) -> None:
        self._visina = visina

    def set_teza(self, teza: float) -> None:
        self._teza = teza

    def to_csv_format(self) -> str:
        s = f"{self._ime},"
        s += f"{self._priimek},"
        s += f"{self._starost},"
        s += f"{self._spol},"
        s += f"{self._visina:.2f},"
        s += f"{self._teza:.2f}"
        return s

    def __str__(self):
        s = f"{self._ime + " " + self._priimek:<15}, "
        s += f"Starost: {self._starost:>3}, "
        s += f"Spol: {self._spol}, "
        s += f"Visina: {self._visina:>6.2f} cm, "
        s += f"Teza: {self._teza:>6.2f} kg"
        return s


class DijakHandler:
    def dijak_obstaja(self, dijaki: list[Dijak], ime: str, priimek: str) -> bool:
        for d in dijaki:
            if d.get_ime() == ime and d.get_priimek() == priimek:
                return True
        return False

    def by_ime(self, dijaki: list[Dijak], isReversed: bool) -> list[Dijak]:
        return sorted(dijaki, key=(lambda x: x.get_ime().lower()), reverse=isReversed)

    def by_priimek(self, dijaki: list[Dijak], isReversed: bool) -> list[Dijak]:
        return sorted(
            dijaki, key=(lambda x: x.get_priimek().lower()), reverse=isReversed
        )

    def by_starost(self, dijaki: list[Dijak], isReversed: bool) -> list[Dijak]:
        return sorted(dijaki, key=(lambda x: x.get_starost()), reverse=isReversed)

    def by_spol(self, dijaki: list[Dijak], poZenskem: bool) -> list[Dijak]:
        return sorted(dijaki, key=(lambda x: x.get_spol()), reverse=poZenskem)

    def by_visina(self, dijaki: list[Dijak], isReversed: bool) -> list[Dijak]:
        return sorted(dijaki, key=(lambda x: x.get_visina()), reverse=isReversed)

    def by_teza(self, dijaki: list[Dijak], isReversed: bool) -> list[Dijak]:
        return sorted(dijaki, key=(lambda x: x.get_teza()), reverse=isReversed)

    def povprecna_visina(self, dijaki: list[Dijak], spol="") -> float:
        dijaki_filter = list(
            filter(lambda x: True if x.get_spol() == spol else False, dijaki)
        )
        sestevek = 0
        for d in dijaki if spol == "" else dijaki_filter:
            sestevek += d.get_visina()
        return sestevek / (len(dijaki) if spol == "" else len(dijaki_filter))

    def povprecna_teza(self, dijaki: list[Dijak], spol="") -> float:
        dijaki_filter = list(
            filter(lambda x: True if x.get_spol() == spol else False, dijaki)
        )
        sestevek = 0
        for d in dijaki if spol == "" else dijaki_filter:
            sestevek += d.get_teza()
        return sestevek / (len(dijaki) if spol == "" else len(dijaki_filter))

    def povprecna_starost(self, dijaki: list[Dijak], spol="") -> float:
        dijaki_filter = list(
            filter(lambda x: True if x.get_spol() == spol else False, dijaki)
        )
        sestevek = 0
        for d in dijaki if spol == "" else dijaki_filter:
            sestevek += d.get_starost()
        return sestevek / (len(dijaki) if spol == "" else len(dijaki_filter))
