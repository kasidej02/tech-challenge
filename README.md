# Tech Challenge

We have a nested dictionary/Json, we would like a function that you pass in the object and a key and get
back the value.

## Repository Structure
```
tech-challenge/
├── dictionary_1.json     # Sample JSON file with nested structure (a/b/c)
├── dictionary_2.json     # Sample JSON file with nested structure (x/y/z)
├── main.py              # Entry point with CLI interface for JSON parsing and navigation
├── parser/
│   └── json_parser.py   # Core JSON parsing implementation without external dependencies
├── README.md           # Project documentation
└── tests/
    └── test_main.py    # Test suite for main functionality
```

## Usage Instructions
### Prerequisites
- Python 3.6 or higher
- No additional packages required

### Installation
1. Clone the repository:
```bash
git clone <repository-url>
cd tech-challenge
```

2. No additional installation steps required as the project uses only Python standard library.

### Quick Start
1. Run the main script:
```bash
python main.py
```

2. When prompted:
   - Enter the path to your JSON file
   - Optionally enter a nested path using forward slashes (e.g., "a/b/c")

Example usage:
```python
Enter JSON file path: dictionary_1.json
Enter nested path (e.g. a/b/c) or leave empty: a/b/c
```

### More Detailed Examples
1. Parse and display entire JSON file:
```python
Enter JSON file path: dictionary_2.json
Enter nested path (e.g. a/b/c) or leave empty: 

Parsed JSON file:
{'x': {'y': {'z': 'a'}}}
```

2. Access nested value using path:
```python
Enter JSON file path: dictionary_2.json
Enter nested path (e.g. a/b/c) or leave empty: x/y/z

Value at path x/y/z:
a
```

### Troubleshooting
Common issues and solutions:

1. File Not Found Error
   - Error message: "File not found. Please make sure '[filename]' exists."
   - Solution: Verify the JSON file path and ensure it exists in the correct directory

2. Invalid JSON Format
   - Error message: "Error parsing JSON file: [specific error]"
   - Solution: Validate your JSON file format using a JSON validator

3. Path Not Found
   - Error message: "Path '[path]' not found in the JSON data"
   - Solution: Verify the path exists in your JSON structure
   - Use forward slashes (/) as separators
   - Check for exact key names (case-sensitive)

## Data Flow
The application processes JSON data through a custom parser that transforms JSON text into Python objects and provides path-based access to nested values.

```ascii
Input JSON File → Custom Parser → Python Object → Path Navigator → Nested Value
     [file.json]   [parse_json]    [dict/list]   [get_nested]    [result]
```

Component interactions:
1. The main script accepts user input for file path and nested path
2. JSON file is read and passed to the custom parser
3. Parser converts JSON text to Python objects without external libraries
4. Nested path navigator traverses the object structure using the provided path
5. Results are displayed to the user with appropriate error handling
6. The parser handles all standard JSON data types and nested structures
7. Path navigation uses forward slash notation for simplicity and clarity