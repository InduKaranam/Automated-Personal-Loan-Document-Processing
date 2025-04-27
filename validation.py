def validate_data(extracted_data):
    errors = []
    if not extracted_data.get('Name'):
        errors.append('Missing Name')
    if not extracted_data.get('Address'):
        errors.append('Missing Address')
    if not extracted_data.get('Income Details'):
        errors.append('Missing Income Details')
    if not extracted_data.get('Loan Amount'):
        errors.append('Missing Loan Amount')

    return errors
