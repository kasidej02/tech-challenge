"""
Example usage of the custom JSON parser.
"""
from parser.json_parser import parse_json, load_json_file

# Method 2: Load JSON from file
# try:
file_data = load_json_file('dictionary_2.json')

def get_nested_value(data, path):
    """Get value from nested dictionary using path with '/' separator"""
    keys = path.split('/')
    result = data
    for key in keys:
        result = result[key]
    return result

# Example usage
path = 'x'
value = get_nested_value(file_data, path)
print(f"\nValue at path {path}:")
print(value)
