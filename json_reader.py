import json

def extract_strings_from_json(file_path):
    # Function to recursively extract strings from the JSON data
    def extract_strings(data):
        strings = []
        if isinstance(data, dict):
            for value in data.values():
                strings.extend(extract_strings(value))
        elif isinstance(data, list):
            for item in data:
                strings.extend(extract_strings(item))
        elif isinstance(data, str):
            strings.append(data)
        return strings

    # Read the JSON file
    with open(file_path, 'r') as file:
        json_data = json.load(file)

    # Extract strings from the JSON data
    string_values = extract_strings(json_data)
    return string_values

def save_strings_to_text(strings, output_file_path):
    # Save the extracted strings to a text file
    with open(output_file_path, 'w') as file:
        for string in strings:
            file.write(string + '\n')

# Example usage
file_path = '/home/necro/Desktop/ocr/new_bill_results.json'
strings = extract_strings_from_json(file_path)

# Specify the output file path
output_file_path = '/home/necro/Desktop/ocr/extracted_strings.txt'

# Save the strings to the output text file
save_strings_to_text(strings, output_file_path)

print(f"Strings have been saved to {output_file_path}")

