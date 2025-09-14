# /// script
# requires-python = ">=3.9"
# dependencies = [
# ]
# ///

from datetime import datetime


def start_coding():
    """A simple function to indicate the start of coding."""
    print("Add more Python code to this script to extend functionality!")


def date():
    """Return the current date and time."""
    current_datetime = datetime.now()
    return current_datetime


def main():
    """Main function to run the script."""
    start_coding()
    print(date())


if __name__ == "__main__":
    main()
