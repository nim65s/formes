#!/usr/bin/env python3
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

    def __init__(self, a: float):
        self.a = a

    def __str__(self) -> str:
        return f"rond de rayon {self.a} de couleur {self.couleur}"


class Quadrilatère(Forme):
    a: float
    b: float
    c: float
    d: float

    def __init__(self, a: float, b: float, c: float, d: float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def __str__(self) -> str:
        return (
            f"quadrilatère de côtés {self.a}, {self.b}, {self.c} "
            "et {self.d}  de couleur {self.couleur}"
        )


if __name__ == "__main__":
    f = Forme()
    print(f)
    r = Rond(10)
    print(r)
    q = Quadrilatère(2, 2, 2, 2)
    print(q)
