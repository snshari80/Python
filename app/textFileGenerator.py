from pathlib import Path

desktop_path = Path.home() / 'OneDrive' / 'Desktop'
desktop_path.mkdir(parents=True, exist_ok=True)

data = {}
fields = {}

print('Happy Coding :) Please enter the contact details to convert as a file!')

def get_contact_details():

    columns_input = input('Enter the Total Fields number needs to be added: ')
    if columns_input.isdigit() and int(columns_input) > 0:
        columns = int(columns_input)
    else:
        print("Please enter a valid positive integer for the number of fields.")
        return get_contact_details()

    for i in range(columns):
        field = i
        value = input(f'Enter the field name: ')
        fields[field] = value 
    
    return validateData(data)

def validateData(data):
    for key, value in fields.items():
        data[value] = input(f'Enter value for {value}: ')

    for key, value in data.items():
        global file_Name
        if key.lower() == 'name':
            file_Name = value
        if not value:
            print(f"{key} is required. Please try again.")
            return validateData()
        if key.lower() in ('name') and not value.isalpha():
            print("Name should only contain alphabets. Please try again.")
            return validateData()
        if key.lower() in ('phone', 'mobile','number') and (not value.isdigit() or len(value) != 10):
            print("Phone number must be a 10-digit number. Please try again.")
            return validateData()
        if key.lower() == 'email' and ('@' not in value or '.' not in value):
            print("Invalid email format. Please try again.")
            return validateData()
        else:
            return convert_file(data, file_Name)

def convert_file(data, file_Name):
    filePath = desktop_path / f"{file_Name}.txt"
    print("Creating file at:", filePath)
    with open(filePath, 'a') as f:
         for key, value in data.items():
            f.write(f"{key}: {value}\n")
    print(f"Contact details saved to {filePath}")

get_contact_details()
