import re         # Import regex module for pattern matching
import sys        # Import sys to access command-line arguments
import os         # Import os to check file existence

# Define a regex pattern to match phone numbers with various formats
phone_pattern = re.compile(r'''
    (\+?\d{1,2}[\s-]?)?        # Optional country code, e.g. +1 or 44, followed by space or dash
    (\(?\d{3}\)?[\s.-]?)       # Area code, with or without parentheses, followed by space/dot/dash
    (\d{3}[\s.-]?)             # First 3 digits of the phone number, followed by space/dot/dash
    (\d{4})                    # Last 4 digits of the phone number
    (\s*(ext|x|ext.)\s*\d{2,5})?  # Optional extension: ext, x, or ext. followed by 2-5 digits
''', re.VERBOSE)               # VERBOSE lets us write the regex with comments and spacing for clarity

# Function to classify phone number type based on number string and nearby text context
def identify_type(number_str, context_str):
    # Common toll-free prefixes to check for in context text
    toll_free_codes = ["800", "888", "877", "866", "855", "844", "833", "822"]
    # Check if any toll-free code or phrase appears in context (case-insensitive)
    if any(code in context_str.lower() for code in toll_free_codes) or "toll-free" in context_str.lower():
        return "Toll-Free"            # Number is toll-free if matched
    elif '+' in number_str:
        return "International"       # If '+' sign in number, classify as international
    elif 'ext' in number_str or 'x' in number_str:
        return "With Extension"       # If extension keyword present, mark accordingly
    # Match legacy 7-digit numbers like '555-8891' (without area code)
    elif re.match(r'^\d{3}[\s.-]?\d{4}$', number_str):
        return "Legacy"
    else:
        return "Standard"             # Default classification for all other numbers

# Function to extract all phone numbers and their types from input text
def extract_phone_numbers(text):
    # Find all matches in the text according to phone_pattern regex
    matches = list(phone_pattern.finditer(text))
    results = []

    for match in matches:
        # Combine all matching regex groups into one full phone number string (filter out None)
        full_number = ''.join(filter(None, match.groups())).strip()
        # Get start and end positions of match in the text
        start, end = match.span()
        # Extract surrounding text (100 chars before and after) to help identify type
        context = text[max(0, start-100):min(len(text), end+100)]
        # Determine the type of phone number using helper function
        number_type = identify_type(full_number, context)
        # Add tuple of number and its type to results list
        results.append((full_number, number_type))
    return results

def main():
    print("Phone Number Extractor")
    print("======================")
    
    # If user provided a command-line argument (file path), try to read from file
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        # Check if file exists at given path
        if not os.path.isfile(filepath):
            print(f"Error: File '{filepath}' does not exist.")   # Inform if file not found
            return
        # Open and read the file contents
        with open(filepath, 'r', encoding='utf-8') as file:
            text = file.read()
    else:
        # If no file provided, prompt user to paste text directly
        print("No file path provided.")
        print("Paste your text below (finish input with an empty line):")

        lines = []
        while True:
            line = input()
            if line.strip() == '':   # Empty line signals end of input
                break
            lines.append(line)
        text = '\n'.join(lines)

        # If no text entered, exit program
        if not text.strip():
            print("No text entered. Exiting.")
            return

    # Extract phone numbers and types from the input text
    results = extract_phone_numbers(text)

    # Display results or notify if none found
    if not results:
        print("No phone numbers found.")
    else:
        print("\nExtracted phone numbers and their types:\n")
        for number, num_type in results:
            print(f"{number}  -->  Type: {num_type}")

# Only run main() if this script is executed directly (not imported as a module)
if __name__ == "__main__":
    main()
