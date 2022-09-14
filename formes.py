class Forme:
    """Classe de base pour les autres formes."""

    couleur: str = "noire"

    def __str__(self) -> str:
        return f"forme indéfinie de couleur {self.couleur}"
