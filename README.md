# Password Generator

This Python script generates a random password based on specified criteria using command-line arguments.

## Features

- Generate passwords of variable length.
- Include or exclude uppercase letters, lowercase letters, digits, and symbols in the password.
- Shuffle the characters in the password for added security.

## Usage

### Requirements

- Python 3.x
- `argparse` library (usually included in Python standard library)

### Command-line Arguments

- `-l, --length`: Length of the password (default: 12)
- `-u, --no-uppercase`: Exclude uppercase letters
- `-w, --no-lowercase`: Exclude lowercase letters
- `-d, --no-digits`: Exclude digits
- `-s, --no-symbols`: Exclude symbols

### Example

```bash
python password_generator.py --length 16 --no-symbols
```
This command will generate a 16-character password without including symbols.
(Replace password_generator.py with whatever you saved the source file as)

## How It Works

The script uses Python's `random` module to generate a password by:

1. Defining character sets based on user input.
2. Randomly selecting characters from the defined sets.
3. Shuffling the selected characters to enhance password strength.
4. Printing the generated password to the console.
