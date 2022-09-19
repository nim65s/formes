#!/usr/bin/env python3
class Forme:
    """Classe de base pour les autres formes.

    >>> f = Forme()
    >>> print(f)
    forme indéfinie de couleur noire
    """

    couleur: str

    def __init__(self, couleur="noire"):
        self.couleur = couleur

    def __str__(self) -> str:
        return f"forme indéfinie de couleur {self.couleur}"


class Rond(Forme):
    a: float

    def __init__(self, a: float, **kwargs):
        self.a = a
        super().__init__(**kwargs)

    def __str__(self) -> str:
        return f"rond de rayon {self.a} de couleur {self.couleur}"

    def __add__(self, other):
        return Rond(self.a + other.a)


class Quadrilatère(Forme):
    a: float
    b: float
    c: float
    d: float

    def __init__(self, a: float, b: float, c: float, d: float, **kwargs):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        super().__init__(**kwargs)

    def __str__(self) -> str:
        return (
            f"{self.specialite()} de côtés {self.a}, {self.b}, {self.c} "
            f"et {self.d}  de couleur {self.couleur}"
        )

    def specialite(self) -> str:
        if self.a == self.b == self.c == self.d:
            return "carré"
        if self.a == self.c and self.b == self.d:
            return "parallélogramme"
        return "quadrilatère"


def show(*dimensions, **kwargs):
    if len(dimensions) == 1:
        instance = Rond(dimensions[0], **kwargs)
    if len(dimensions) == 4:
        instance = Quadrilatère(*dimensions, **kwargs)
    print(instance)


if __name__ == "__main__":
    f = Forme()
    print(f)
    r = Rond(10)
    print(r)
    q = Quadrilatère(2, 2, 2, 2)
    print(q)

    #

    show(4.3, couleur="vert")
    show(2, 2, 2, 2, couleur="jaune")
    show(2, 2, 3, 2, couleur="violet")
