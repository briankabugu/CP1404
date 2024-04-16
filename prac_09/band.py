"""
CP1404/CP5632 Practical
Band class
"""

class Band:
    """Band class to represent a musical band."""

    def __init__(self, name):
        """Construct a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add_musician(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first (or no) instrument."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return '\n'.join(result)


if __name__ == '__main__':
    from musician import Musician
    from guitar import Guitar

    # Create a Band instance
    band = Band("Extreme")

    # Create Musician instances and add instruments to them
    nuno_bettencourt = Musician("Nuno Bettencourt")
    nuno_bettencourt.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno_bettencourt.add(Guitar("Takamine acoustic", 1986, 1200.00))

    gary_cherone = Musician("Gary Cherone")

    pat_badger = Musician("Pat Badger")
    pat_badger.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.00))

    kevin_figueiredo = Musician("Kevin Figueiredo")

    # Add Musicians to the Band
    band.add_musician(nuno_bettencourt)
    band.add_musician(gary_cherone)
    band.add_musician(pat_badger)
    band.add_musician(kevin_figueiredo)

    # Print Band information and musicians playing instruments
    print(band)
    print(band.play())
