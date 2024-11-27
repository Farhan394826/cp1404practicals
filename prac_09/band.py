
from prac_09.musician import Musician

class Band:
    """Represent a Band that contains multiple musicians."""

    def __init__(self, name):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the band, including its musicians."""
        return f"{self.name} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Make each musician in the band play their instrument or notify if they lack one."""
        for musician in self.musicians:
            print(musician.play())
