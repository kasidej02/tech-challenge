"""
Custom JSON parser module without using any external libraries.
"""

def parse_json(json_str):
    """
    Parse a JSON string into Python objects.
    
    Args:
        json_str (str): A valid JSON string
        
    Returns:
        The parsed Python object (dict, list, str, int, float, bool, or None)
    """
    # Remove whitespace
    json_str = json_str.strip()
    
    # Parse JSON object
    if json_str.startswith('{') and json_str.endswith('}'):
        result = {}
        # Remove braces
        content = json_str[1:-1].strip()
        
        if not content:
            return {}
            
        # Split by commas not inside quotes or nested structures
        in_quotes = False
        brace_count = 0
        bracket_count = 0
        start = 0
        pairs = []
        
        for i, char in enumerate(content):
            if char == '"' and (i == 0 or content[i-1] != '\\'):
                in_quotes = not in_quotes
            elif not in_quotes:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                elif char == '[':
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1
                elif char == ',' and brace_count == 0 and bracket_count == 0:
                    pairs.append(content[start:i].strip())
                    start = i + 1
        
        # Add the last pair
        if start < len(content):
            pairs.append(content[start:].strip())
        
        # Process each key-value pair
        for pair in pairs:
            colon_pos = pair.find(':')
            if colon_pos != -1:
                # Extract key (remove quotes)
                key = pair[:colon_pos].strip()
                if key.startswith('"') and key.endswith('"'):
                    key = key[1:-1]
                
                # Extract value
                value = pair[colon_pos+1:].strip()
                result[key] = parse_json_value(value)
        
        return result
    
    # Parse JSON array
    elif json_str.startswith('[') and json_str.endswith(']'):
        result = []
        # Remove brackets
        content = json_str[1:-1].strip()
        
        if not content:
            return []
            
        # Split by commas not inside quotes or nested structures
        in_quotes = False
        brace_count = 0
        bracket_count = 0
        start = 0
        items = []
        
        for i, char in enumerate(content):
            if char == '"' and (i == 0 or content[i-1] != '\\'):
                in_quotes = not in_quotes
            elif not in_quotes:
                if char == '{':
                    brace_count += 1
                elif char == '}':
                    brace_count -= 1
                elif char == '[':
                    bracket_count += 1
                elif char == ']':
                    bracket_count -= 1
                elif char == ',' and brace_count == 0 and bracket_count == 0:
                    items.append(content[start:i].strip())
                    start = i + 1
        
        # Add the last item
        if start < len(content):
            items.append(content[start:].strip())
        
        # Process each item
        for item in items:
            result.append(parse_json_value(item))
        
        return result
    
    return json_str

def parse_json_value(value):
    """
    Parse a JSON value into its Python equivalent.
    
    Args:
        value (str): A JSON value as string
        
    Returns:
        The parsed Python value
    """
    value = value.strip()
    
    # String
    if value.startswith('"') and value.endswith('"'):
        return value[1:-1]
    
    # Number
    try:
        if '.' in value:
            return float(value)
        return int(value)
    except ValueError:
        pass
    
    # Boolean
    if value == 'true':
        return True
    if value == 'false':
        return False
    
    # Null
    if value == 'null':
        return None
    
    # Object or Array
    if (value.startswith('{') and value.endswith('}')) or (value.startswith('[') and value.endswith(']')):
        return parse_json(value)
    
    return value


def load_json_file(file_path):
    """
    Load and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        The parsed Python object
    """
    with open(file_path, 'r') as file:
        json_str = file.read()
    return parse_json(json_str)