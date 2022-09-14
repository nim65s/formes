class Forme:
    """Classe de base pour les autres formes.

    >>> f = Forme()
    >>> print(f)
    forme indéfinie de couleur noire
    """

    couleur: str = "noire"

    def __str__(self) -> str:
        return f"forme indéfinie de couleur {self.couleur}"


class Rond(Forme):
    a: float

    def __str__(self) -> str:
        return f"rond de rayon {self.a} de couleur {self.couleur}"


if __name__ == "__main__":
    f = Forme()
    print(f)
    r = Rond()
    print(r)
