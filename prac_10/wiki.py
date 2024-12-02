"""
CP1404/CP5632 Practical - Wiki API
"""

import wikipedia

def main():
    """Run the Wikipedia search and summary program."""
    print("Wikipedia Search")
    print("Enter a blank line to exit.")
    while True:
        title = input("Enter page title or search phrase: ").strip()
        if not title:
            print("Thank you.")
            break

        try:
            page = wikipedia.page(title, autosuggest=True)
            print(f"\nTitle: {page.title}")
            print(f"Summary: {page.summary[:500]}...")  # Display first 500 characters
            print(f"URL: {page.url}\n")
        except wikipedia.DisambiguationError as e:
            print("\nWe need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.PageError:
            print("\nPage not found. Please try another title or phrase.")
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
