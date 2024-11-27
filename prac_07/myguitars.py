
class Guitar:
    """Class representing a guitar."""

    def __init__(self, name, year, cost):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.year}) - ${self.cost:,.2f}"

    def __lt__(self, other):
        """Comparison for sorting by year."""
        return self.year < other.year


def load_guitars(file_path):
    """Load guitars from a CSV file."""
    guitars = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                try:
                    name, year, cost = line.strip().split(',')
                    guitars.append(Guitar(name, int(year), float(cost)))
                except ValueError as e:
                    print(f"Error parsing line: {line.strip()}. Skipping. ({e})")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    return guitars


def save_guitars(file_path, guitars):
    """Save guitars to a CSV file."""
    with open(file_path, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


def add_guitar():
    """Prompt the user to input a new guitar."""
    name = input("Enter guitar name: ").strip()
    while not name:
        print("Name cannot be empty.")
        name = input("Enter guitar name: ").strip()

    try:
        year = int(input("Enter year: "))
        cost = float(input("Enter cost: "))
        return Guitar(name, year, cost)
    except ValueError:
        print("Invalid input. Guitar not added.")
        return None


def display_guitars(guitars):
    """Display all guitars."""
    if not guitars:
        print("No guitars to display.")
        return

    print("\nYour Guitars:")
    for guitar in guitars:
        print(guitar)


def main():
    """Main function to manage the guitar collection."""
    file_path = "guitars.csv"
    guitars = load_guitars(file_path)
    guitars.sort()

    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    print("\nAdd a new guitar:")
    new_guitar = add_guitar()
    if new_guitar:
        guitars.append(new_guitar)
        guitars.sort()
        save_guitars(file_path, guitars)
        print("\nUpdated guitar collection:")
        display_guitars(guitars)


if __name__ == "__main__":
    main()
