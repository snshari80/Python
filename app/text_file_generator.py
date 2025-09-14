"""Module to collect contact details from user and save them as a text file on the Desktop."""
from pathlib import Path

desktop_path = Path.home() / 'OneDrive' / 'Desktop'
desktop_path.mkdir(parents=True, exist_ok=True)

def get_contact_details():
    """Prompt the user for field names and values, then validate and save them."""
    columns = None
    data = {}
    fields = {}
    columns_input = input('Enter the Total Fields number needs to be added: ')
    if columns_input.isdigit() and int(columns_input) > 0:
        columns = int(columns_input)
    else:
        print("Please enter a valid positive integer for the number of fields.")
        get_contact_details()
        return

    for i in range(columns):
        field = i
        value = input('Enter the field name: ')
        fields[field] = value
    validate_data(data, fields)

def validate_data(data, fields):
    """Validate the collected data and save to file if valid."""
    file_name = None

    condition_one = key.lower() in ('phone', 'mobile','number')
    condition_two = (not value.isdigit() or len(value) != 10)
    for key, value in fields.items():
        data[value] = input(f'Enter value for {value}: ')

    for key, value in data.items():
        if key.lower() == 'name':
            file_name = value
        if not value:
            print(f"{key} is required. Please try again.")
            return validate_data(data, fields)
        if key.lower() in ('name') and not value.isalpha():
            print("Name should only contain alphabets. Please try again.")
            return validate_data(data, fields)
        if condition_one and condition_two:
            print("Phone number must be a 10-digit number. Please try again.")
            return validate_data(data, fields)
        if key.lower() == 'email' and ('@' not in value or '.' not in value):
            print("Invalid email format. Please try again.")
            return validate_data(data, fields)
    if file_name:
        convert_file(data, file_name)

def convert_file(data, file_name):
    """Create a text file on the Desktop with the collected details."""
    file_path = desktop_path / f"{file_name}.txt"
    print("Creating file at:", file_path)
    with open(file_path, 'a', encoding='utf-8') as f:
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
    print(f"Contact details saved to {file_path}")

if __name__ == "__main__":
    print('Happy Coding :)\n'
          'This script will help you create a text file with your required details \n'
          'on the Desktop.')
    get_contact_details()
