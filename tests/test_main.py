"""
Minimal test for main.py with automatic input using dictionary_1.json
No imports used
"""

# Test inputs and expected results
test_cases = [
    {"inputs": ["dictionary_1.json", "a/b/c"], "expected": "d", "name": "Find existing nested value"},
    {"inputs": ["dictionary_1.json", "a/d"], "expected": "Path 'a/d' not found in the JSON data", "name": "Not found path in JSON data"},
    {"inputs": ["dictionary_1.json", "e"], "expected": "Path 'e' not found in the JSON data", "name": "Not found key in JSON data"},
    {"inputs": ["dictionary_1.json", "a/b/x"], "expected": "not found", "name": "Handle missing path"},
    {"inputs": ["nonexistent.json", ""], "expected": "File not found", "name": "Handle missing file"}
    
]

# Flatten inputs for the input function
inputs = []
for case in test_cases:
    inputs.extend(case["inputs"])

# Mock input function
input_index = 0
def custom_input(prompt):
    global input_index
    value = inputs[input_index]
    print(f"{prompt}{value}")
    input_index += 1
    return value

# Replace built-in input
__builtins__.input = custom_input

# Track results
results = []

# Run main.py for each test case
for i, test_case in enumerate(test_cases):
    print(f"\n--- Test {i+1}: {test_case['name']} ---")
    
    # Capture output
    original_stdout = __builtins__.print
    output = []
    
    def capture_print(*args, **kwargs):
        output.append(" ".join(str(arg) for arg in args))
        original_stdout(*args, **kwargs)
    
    __builtins__.print = capture_print
    
    try:
        exec(open("main.py").read())
        output_text = "\n".join(output)
        
        # Check if expected text is in output
        if test_case["expected"] in output_text:
            results.append(True)
            print(f"✓ PASS: {test_case['name']}")
        else:
            results.append(False)
            print(f"✗ FAIL: {test_case['name']} - Expected '{test_case['expected']}' not found in output")
    except Exception as e:
        if "File not found" in str(e) and test_case["expected"] == "File not found":
            results.append(True)
            print(f"✓ PASS: {test_case['name']} (Expected exception)")
        else:
            results.append(False)
            print(f"✗ FAIL: {test_case['name']} - Error: {e}")
    
    # Restore print
    __builtins__.print = original_stdout

# Print summary
print("\n--- Test Summary ---")
passed = results.count(True)
failed = results.count(False)
print(f"Total: {len(results)}, Passed: {passed}, Failed: {failed}")

for i, (result, test_case) in enumerate(zip(results, test_cases)):
    status = "✓ PASS" if result else "✗ FAIL"
    print(f"{status}: Test {i+1} - {test_case['name']}")