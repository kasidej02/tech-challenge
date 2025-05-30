from parser.json_parser import load_json_file

def get_nested_value(data, path):
    """Get value from nested dictionary using path with '/' separator"""
    keys = path.split('/')
    result = data
    for key in keys:
        if isinstance(result, dict) and key in result:
            result = result[key]
        else:
            return None
    return result

# Get input from user
json_file = input("Enter JSON file path: ")
nested_path = input("Enter nested path (e.g. a/b/c) or leave empty: ")

try:
    # Load and parse the JSON file
    file_data = load_json_file(json_file)
    
    # If a path is provided, get and display the nested value
    if nested_path:
        value = get_nested_value(file_data, nested_path)
        if value is not None:
            print(f"\nValue at path {nested_path}:")
            print(value)
        else:
            print(f"Path '{nested_path}' not found in the JSON data")
    else:
        # Otherwise, display the entire parsed data
        print("\nParsed JSON file:")
        print(file_data)
except FileNotFoundError:
    print(f"\nFile not found. Please make sure '{json_file}' exists.")
except Exception as e:
    print(f"\nError parsing JSON file: {str(e)}")