# 📞 Phone Number Extractor with Regex

This project is a Python script that extracts phone numbers from unstructured text using regular expressions. It showcases practical use of Python’s built-in `re` module to build and test patterns that match various phone number formats, including:

- Standard formats like `555-555-5555`, `(555) 555-5555`, `555.555.5555`, and `555 555 5555`  
- Numbers with country code prefix such as `+1 555-555-5555`  
- Numbers with extensions like `555-555-5555 ext. 123` or `555-555-5555 x1234`  
- Legacy or old-school 7-digit formats such as `555-1234`  

---

## 🔍 Why I Built This

I initially found regular expressions confusing, especially when I first tried using them in Python over a year ago. But while working helpdesk, I began encountering real-world use cases—particularly in PowerShell scripts and log analysis—that helped me develop confidence and curiosity around regex. That hands-on exposure eventually made Python’s implementation click.

As I’ve grown more skilled with web scraping, scripting, and cybersecurity simulations, I’ve come to see regex as an essential tool for both technical and everyday automation tasks like data cleanup and pattern detection.

---

## 🧠 What I Learned

- How to build flexible regex patterns to handle multiple phone number formats  
- How to use escape characters like `\s`, `+`, and others correctly  
- How to compile regex patterns and apply them to multiline text inputs  
- How to structure reusable code with functions and conditional logic for clean, maintainable scripts  
- The value of tools like [regex101](https://regex101.com) for testing and debugging patterns  
- Practical use of Python’s `argparse` module to improve script flexibility with CLI parameters  

---

## 🧠 Why This Script Matters

Ideal for data cleanup, lead generation, and content parsing — this tool quickly extracts phone numbers from raw text, making it useful for businesses, marketers, and analysts who need accurate contact information without manual work.

---

## 📂 Example Input & Output

To try the script quickly, use the included sample files:

- `sample_input.txt`: Example text containing various phone number formats  
- `sample_output.txt`: Expected extracted phone numbers and their classified types

Run the script with the sample input file:

```bash
python3 phone_number_extractor.py --file sample_input.txt
