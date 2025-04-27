import pytesseract

def extract_text(image):
    text = pytesseract.image_to_string(image)
    return text

def extract_key_fields(text):
    extracted = {
        "Name": None,
        "Address": None,
        "Income Details": None,
        "Loan Amount": None
    }

    lines = text.split('\n')
    for line in lines:
        if 'name' in line.lower():
            extracted['Name'] = line.split(":")[-1].strip()
        elif 'address' in line.lower():
            extracted['Address'] = line.split(":")[-1].strip()
        elif 'income' in line.lower():
            extracted['Income Details'] = line.split(":")[-1].strip()
        elif 'loan amount' in line.lower():
            extracted['Loan Amount'] = line.split(":")[-1].strip()

    return extracted
